import os

PATH = "/clicker/users"


def get_devices_folders():
    all_entries = os.listdir(PATH)
    print(all_entries)


if __name__ == "__main__":
    folders = get_devices_folders()
