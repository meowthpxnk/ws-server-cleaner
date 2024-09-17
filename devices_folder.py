import os

ROOT_PATH = "/clicker/users"
SETTINGS_PATH = "clicker_settings.yml"


def get_devices_folders():
    device_names = os.listdir(ROOT_PATH)

    for device_name in device_names:
        settings_file = os.path.join(ROOT_PATH, device_name, SETTINGS_PATH)

        print(settings_file)


if __name__ == "__main__":
    folders = get_devices_folders()
