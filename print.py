from app.devices import analyse_devices
from app.db import analyse_dbs, clear_all_dbs, drop_inactive_dbs, get_db_phones
from app.files import clear_folder

# analyse_devices()

# analyse_dbs()
phones = get_db_phones()
clear_folder(phones)
