from pymongo import MongoClient

from app.utils.database_analyse import analyse_db


def analyse_dbs():
    # cl = MongoClient()

    # print(cl.list_database_names())

    analyse_db("12059906323")
    ...
