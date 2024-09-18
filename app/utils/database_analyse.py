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

    print(len(list(in_messages.find)))


def analyse_db(phone):
    db = get_db(phone)

    print(f"Analyse database for phone: {phone}")

    # delta = get_delta_timestamp()
    # print(f"Delta: {delta}")

    for coll_name in DB_COLLECTIONS:

        coll = db[coll_name]

        records = coll.find()
        print(f"Coll - {coll_name} count {len(list(records))}")

        # if coll_name is not DB_IN:
        #     continue

        # print(coll.__dir__())

        # q = coll.find(query)
        # print(len(list(q)))

    #     timestamps = []

    #     for rec in q:
    #         ts = rec["messageTimestamp"]
    #         # print(rec)
    #         ts = Timestapm(ts)
    #         timestamps.append(ts)
    #         print(ts)
    #         # break
    #     print(f"Count timestamps: {len(timestamps)}")

    # print("-" * 40)

    # print(db.list_collection_names())


if __name__ == "__main__":
    analyse_db("79014355936")

    clear_db("79014355936")
