from app.utils.devices_settings import get_devices_folders, ROOT_PATH


def clear_folder(acitve_phones):
    folders = get_devices_folders()
    print(len(acitve_phones))
    print(len(folders))

    to_remove = []
    for folder in folders:
        if folder not in acitve_phones:
            to_remove.append(folder)

    print(len(to_remove))
