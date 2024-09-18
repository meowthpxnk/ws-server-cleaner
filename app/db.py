from pymongo import MongoClient


def analyse_db():
    cl = MongoClient()

    print(cl.list_database_names())
    ...
