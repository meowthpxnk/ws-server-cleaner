from pymongo import MongoClient

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


def analyse_db(phone):
    cl = MongoClient()
    db_name = DB_NAME.format(phone=phone)
    db = cl[db_name]

    for coll in DB_COLLECTIONS:
        coll = db[coll]

        # print(coll.__dir__())

        records = coll.find()

        print(len(list(records)))

    # print(db.list_collection_names())


if __name__ == "__main__":
    analyse_db("79014355936")
