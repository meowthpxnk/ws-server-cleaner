from pymongo import MongoClient

from app.utils.database_analyse import analyse_db, clear_db


def analyse_dbs():
    # cl = MongoClient()

    # print(cl.list_database_names())

    phone = "13392177155"

    # clear_db(phone)

    analyse = analyse_db(phone)
    print(analyse)
    ...
