from pymongo import MongoClient


def analyse_db():
    cl = MongoClient()

    print(cl.__dir__())
    ...
