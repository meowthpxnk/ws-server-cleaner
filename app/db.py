from pymongo import MongoClient

from app.utils.database_analyse import analyse_db, clear_db

LOCAL_DBS = ["admin", "config", "local"]


def get_phone_from_db_name(db_name):
    db_name = db_name.replace("WA_MD_", "")
    db_name = db_name.replace("_1", "")
    return db_name


def drop_inactive_dbs():
    cl = MongoClient()
    databases = cl.list_database_names()

    for db_name in databases:
        if db_name in LOCAL_DBS:
            continue
        phone = get_phone_from_db_name(db_name)
        analyse = analyse_db(phone, cl=cl)
        print(analyse)

        if analyse.is_empty:
            print(f"DB dropped {db_name}")
            cl.drop_database(db_name)


def clear_all_dbs():
    cl = MongoClient()

    databases = cl.list_database_names()

    for db_name in databases:
        if db_name in LOCAL_DBS:
            continue
        phone = get_phone_from_db_name(db_name)
        clear_db(phone, cl)


def analyse_dbs():
    phone = "13392177155"

    clear_db(phone)

    analyse = analyse_db(phone)
    print(analyse)
    ...
