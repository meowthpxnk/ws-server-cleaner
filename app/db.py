from pymongo import MongoClient

from app.utils.database_analyse import analyse_db, clear_db


def get_phone_from_db_name(db_name):
    db_name = db_name.replace("WA_MD_", "")
    db_name = db_name.replace("_1", "")
    return db_name


# def drop_inactive_dbs():
#     cl = MongoClient()
#     databases = cl.list_database_names()

#     for db in databases:
#         phone = get_phone_from_db_name(databases[0])
#         analyse = analyse_db(phone)
#         if analyse.is_empty:
#             cl


#     ...


def clear_all_dbs():
    cl = MongoClient()

    databases = cl.list_database_names()

    for db_name in databases:
        phone = get_phone_from_db_name(db_name)
        print(phone)
        # clear_db(phone)


def analyse_dbs():
    phone = "13392177155"

    clear_db(phone)

    analyse = analyse_db(phone)
    print(analyse)
    ...
