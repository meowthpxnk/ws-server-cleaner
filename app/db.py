from pymongo import MongoClient

from app.utils.database_analyse import analyse_db, clear_db


def analyse_dbs():
    # cl = MongoClient()

    # print(cl.list_database_names())

    phone = "12059906323"

    clear_db(phone)

    analyse_db("12059906323")
    ...
