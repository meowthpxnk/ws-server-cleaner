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


def analyse_db(phone):
    cl = MongoClient()
    db_name = DB_NAME.format(phone=phone)
    db = cl[db_name]

    delta = datetime.now() - timedelta(hours=2)
    delta = int(delta.timestamp())

    # print("-" * 40)
    print(f"ANALYSE FOR DB {db_name}")

    for coll_name in DB_COLLECTIONS:

        coll = db[coll_name]

        records = coll.find()
        print(f"Coll - {coll_name} count {len(list(records))}")

        if coll_name is not DB_IN:
            continue

        # print(coll.__dir__())

        print(f"Delta: {delta}")

        query = {
            "$or": [
                {
                    "messageTimestamp": {"$lt": delta}
                },  # Фильтрация по timestamp
                {
                    "messageTimestamp.low": {"$lt": delta},
                },  # Фильтрация по словарю
            ]
        }

        q = coll.find(query)
        print(len(list(q)))

        for rec in coll.find(query):
            ts = rec["messageTimestamp"]
            # print(rec)
            ts = Timestapm(ts)
            print(ts)
            # break

    print("-" * 40)

    # print(db.list_collection_names())


if __name__ == "__main__":
    analyse_db("79014355936")
