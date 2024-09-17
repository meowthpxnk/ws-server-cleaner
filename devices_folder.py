import os
import yaml

ROOT_PATH = "/clicker/users"
SETTINGS_PATH = "clicker_settings.yml"


def get_devices_folders():
    device_names = os.listdir(ROOT_PATH)

    for device_name in device_names:
        settings_file = os.path.join(ROOT_PATH, device_name, SETTINGS_PATH)

        with open(settings_file) as f:
            s = f.read()
            s = yaml.safe_load(s)
            print(s)


if __name__ == "__main__":
    folders = get_devices_folders()
