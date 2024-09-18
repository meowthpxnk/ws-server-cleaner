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


def get_delta_timestamp():
    delta = datetime.now() - timedelta(days=1)
    return int(delta.timestamp())


def get_in_messages_collection(db):
    return db[DB_IN]


def get_query():
    delta = get_delta_timestamp()
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


def analyse_db(phone):
    db = get_db(phone)

    print(f"-" * 20 + " Analyse db phone: {phone}" + "-" * 20)

    # print(f"Analyse database for phone: {phone}")

    print("-" * 40)
    for coll_name in DB_COLLECTIONS:

        coll = db[coll_name]

        records = coll.find()
        print(f"Coll - {coll_name} count {len(list(records))}")

    print()

    # contacts analytic
    c = db[DB_READ]
    cursor = c.find()
    print(cursor[0])
    print(cursor[1])
    print(cursor[2])
    print(cursor[3])

    print("-" * 40)


if __name__ == "__main__":
    phone = "79251396383"
    # clear_db(phone)
    analyse_db(phone)
