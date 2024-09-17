from pymongo import MongoClient

DB_NAME = "WA_MD_{phone}_1"


def analyse_db(phone):
    cl = MongoClient()
    db_name = DB_NAME.format(phone=phone)
    # db = cl[db]
    # print(db_name)


if __name__ == "__main__":
    analyse_db("7999")
