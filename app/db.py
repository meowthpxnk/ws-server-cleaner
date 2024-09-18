from pymongo import MongoClient

from app.utils.database_analyse import analyse_db, clear_db


def get_phone_from_db_name(db_name):
    db_name = db_name.replace("WA_MD_", "")
    db_name = db_name.replace("_1", "")
    return db_name


def clear_all_dbs():
    cl = MongoClient()

    databases = cl.list_database_names()

    print(get_phone_from_db_name(databases[0]))


def analyse_dbs():
    phone = "13392177155"

    clear_db(phone)

    analyse = analyse_db(phone)
    print(analyse)
    ...
