from pymongo import MongoClient
from datetime import datetime, timedelta


DB_NAME = "WA_MD_{phone}_1"


DB_SEND = "sentMessages"
DB_CONT = "contacts"
DB_FAILED = "failedMessages"
DB_READ = "readMessages"
DB_IN = "inMessages"
DB_META = "meta"
DB_FROM_WA = "fromWaQueue"

DB_COLLECTIONS = [
    DB_SEND,
    DB_CONT,
    DB_FAILED,
    DB_READ,
    DB_IN,
    DB_META,
    DB_FROM_WA,
]


class Contact:
    jid: str

    # sent_updated: datetime
    # read_updated: datetime

    def __repr__(self):
        return f"<Contact: jid={self.jid}>"


class Timestapm:
    dt: datetime

    def __init__(self, timestamp):
        if isinstance(timestamp, int):
            pass
        elif isinstance(timestamp, dict):
            timestamp = timestamp.get("low")
            if not timestamp:
                raise ValueError("Not valid timestamp dict")
        else:
            raise TypeError("Timestamp must be int or dict")

        self.dt = datetime.fromtimestamp(timestamp)

    def __repr__(self) -> str:
        return f"<Timestamp: dt={self.dt}>"


def get_delta_timestamp_days(days=1, type_dt=False):
    delta = datetime.now() - timedelta(days=days)

    if type_dt:
        return delta
    return int(delta.timestamp())


def get_in_messages_query():
    delta = get_delta_timestamp_days()
    query = {
        "$or": [
            {"messageTimestamp": {"$lt": delta}},  # Фильтрация по timestamp
            {
                "messageTimestamp.low": {"$lt": delta},
            },  # Фильтрация по словарю
        ]
    }
    return query


def get_db(phone, cl=None):
    if not cl:
        cl = MongoClient()

    db_name = DB_NAME.format(phone=phone)
    db = cl[db_name]
    return db


def clear_in_messages(db):
    query = get_in_messages_query()
    db[DB_IN].delete_many(query)


def clear_out_messages(db):
    jid_list = get_active_jid_list(db)
    query = get_jids_for_delete_query(jid_list)

    db[DB_CONT].delete_many(query)
    db[DB_READ].delete_many(query)
    db[DB_SEND].delete_many(query)


def clear_db(phone, cl=None):
    print(f"Start clearing database {phone}")
    db = get_db(phone, cl)

    clear_in_messages(db)
    clear_out_messages(db)


def get_last_messages_query():
    delta = get_delta_timestamp_days(14, type_dt=True)
    return {"updated": {"$gte": delta}}


def get_last_sent_messages(db):
    return db[DB_SEND].find(get_last_messages_query())


def get_last_read_messages(db):
    return db[DB_READ].find(get_last_messages_query())


def get_active_jid_list(db):

    sent = get_last_sent_messages(db)
    read = get_last_read_messages(db)

    jid_list = []

    for m in sent:
        jid = m["jid"]
        if jid not in jid_list:
            jid_list.append(jid)

    for m in read:
        jid = m["jid"]
        if jid not in jid_list:
            jid_list.append(jid)

    return jid_list


def print_coll_counts(db):
    print("-" * 20)
    for coll_name in DB_COLLECTIONS:

        coll = db[coll_name]

        print(f"Coll - {coll_name} count {cont_collection(coll)}")
    print("-" * 20)


def cont_collection(collection):
    return len(list(collection.find()))


def get_jids_for_delete_query(jid_list):
    return {"jid": {"$nin": jid_list}}


class DBAnalyse:
    phone: str

    contacts_count: int
    sent_count: int
    read_count: int
    in_count: int

    @property
    def is_empty(self):
        return not (
            self.contacts_count
            and self.sent_count
            and self.read_count
            and self.in_count
        )

    def __repr__(self) -> str:
        return f"<DBAnalyse: phone={self.phone} Contacts: {self.contacts_count} Sent: {self.sent_count} Read: {self.read_count} In: {self.in_count} $empty: {self.is_empty}\n>"


def analyse_db(phone, count_cols=True, cl=None):
    db = get_db(phone, cl)

    analyse = DBAnalyse()
    analyse.phone = phone

    analyse.contacts_count = cont_collection(db[DB_CONT])
    analyse.sent_count = cont_collection(db[DB_SEND])
    analyse.read_count = cont_collection(db[DB_READ])
    analyse.in_count = cont_collection(db[DB_IN])

    return analyse


if __name__ == "__main__":
    phone = "994512306000"
    # clear_db(phone)
    analyse_db(phone, count_cols=True)
