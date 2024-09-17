from pymongo import MongoClient


def analyse_db(db_name):
    cl = MongoClient()
    db = cl[db]
    print(db)
