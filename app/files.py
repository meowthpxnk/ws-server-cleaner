from app.utils.devices_settings import get_devices_folders, ROOT_PATH
import os
import shutil


def clear_folder(acitve_phones):
    folders = get_devices_folders()

    to_remove = []
    for folder in folders:
        if folder not in acitve_phones:
            to_remove.append(folder)

    for rem_folder in to_remove:
        print(f"Removing folder for device {rem_folder}")
        shutil.rmtree(os.path.join(ROOT_PATH, rem_folder))
