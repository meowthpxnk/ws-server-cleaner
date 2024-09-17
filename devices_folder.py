import os

PATH = "/clicker/users"


def get_devices_folders():
    all_entries = os.listdir(PATH)
    print(all_entries)
