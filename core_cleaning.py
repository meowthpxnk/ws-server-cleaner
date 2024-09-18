from app.devices import analyse_devices
from app.db import analyse_dbs, clear_all_dbs, drop_inactive_dbs, get_db_phones
from app.files import clear_folder


def core_cleaning():
    clear_all_dbs()
    drop_inactive_dbs()
    phones = get_db_phones()
    clear_folder(phones)


if __name__ == "__main__":
    core_cleaning()
