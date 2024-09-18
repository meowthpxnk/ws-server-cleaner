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


# def get_delta_timestamp():
#     delta = datetime.now() - timedelta(days=1)
#     return int(delta.timestamp())


def get_delta_timestamp_days(days=1, type_dt=False):
    delta = datetime.now() - timedelta(days=days)

    if type_dt:
        return delta
    return int(delta.timestamp())


def get_in_messages_collection(db):
    return db[DB_IN]


def get_query():
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


def get_db(phone):
    cl = MongoClient()
    db_name = DB_NAME.format(phone=phone)
    db = cl[db_name]
    return db


def clear_db(phone):
    db = get_db(phone)
    in_messages = get_in_messages_collection(db)
    query = get_query()

    in_messages.delete_many(query)


def get_last_messages_query():
    delta = get_delta_timestamp_days(14, type_dt=True)
    return {"updated": {"$gte": delta}}


def get_last_sent_messages(db):
    return db[DB_SEND].find(get_last_messages_query())


def get_last_read_messages(db):
    return db[DB_READ].find(get_last_messages_query())


def get_active_jits(db):

    sent = get_last_sent_messages(db)
    read = get_last_read_messages(db)

    active_jits = []

    for m in sent:
        jit = m["jit"]
        if jit not in active_jits:
            active_jits.append(jit)

    for m in read:
        jit = m["jit"]
        if jit not in active_jits:
            active_jits.append(jit)

    return active_jits

    # upd.update({
    #     sent["jid"]:
    # })


def analyse_db(phone):
    db = get_db(phone)

    print(f"-" * 20 + f" Analyse db phone: {phone}" + "-" * 20)

    # print(f"Analyse database for phone: {phone}")

    print("-" * 40)
    for coll_name in DB_COLLECTIONS:

        coll = db[coll_name]

        records = coll.find()
        print(f"Coll - {coll_name} count {len(list(records))}")

    print()

    # send messages analytic
    c = db[DB_SEND]
    cursor = c.find()

    # lsm = get_last_sent_messages(db)
    # for m in lsm:
    #     print(m)
    # print(len(list(cursor)))
    # print(len(list(get_last_sent_messages(db))))
    # print(len(list(get_last_read_messages(db))))

    jits = get_active_jits(db)
    print(jits)
    # print(cursor[0])
    # print(cursor[1])
    # print(cursor[2])
    # print(cursor[3])
    # jids = []
    # for r in cursor:
    #     if r["jid"] not in jids:
    #         jids.append(r["jid"])
    #     # print(r)

    # print(len(list(c.find())))
    # print(len(jids))

    print("-" * 40)


if __name__ == "__main__":
    phone = "994512306000"
    # clear_db(phone)
    analyse_db(phone)
