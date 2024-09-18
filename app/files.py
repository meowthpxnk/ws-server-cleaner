from app.utils.devices_settings import get_devices_folders, ROOT_PATH


def clear_folder(acitve_phones):
    print(acitve_phones)
    devices = get_devices_folders()
    print(devices)
