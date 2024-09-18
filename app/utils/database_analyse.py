from pymongo import MongoClient
from datetime import datetime


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

    for coll in DB_COLLECTIONS:

        if coll is not DB_IN:
            continue
        coll = db[coll]
        # print(coll.__dir__())
        records = coll.find()
        # print(len(list(records)))

        for rec in records:
            ts = rec["messageTimestamp"]
            ts = Timestapm(ts)
            print(ts)
            # print()

    # print(db.list_collection_names())


if __name__ == "__main__":
    analyse_db("79014355936")
