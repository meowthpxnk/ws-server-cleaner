import os
import yaml

ROOT_PATH = "/clicker/users"
SETTINGS_PATH = "clicker_settings.yaml"


class Settings:
    port: int
    phone: str

    def __repr__(self) -> str:
        return f"<ClSettings: phone={self.phone} port={self.port}>"


def parse_settings(settings_s):

    settings = yaml.safe_load(settings_s)

    s = Settings()
    whatsapp = settings.get("whatsapp")
    common = settings.get("common")

    if common:
        s.phone = common.get("device_number")

    if whatsapp:
        s.port = whatsapp.get("port")

    return s


def get_devices_folders():
    return os.listdir(ROOT_PATH)


def get_devices_settings():
    device_names = get_devices_folders()

    settings_list = []

    for device_name in device_names:
        settings_file = os.path.join(ROOT_PATH, device_name, SETTINGS_PATH)

        with open(settings_file) as f:
            settings_s = f.read()
            settings = parse_settings(settings_s)
            # print(settings)
            settings_list.append(settings)

    return settings_list


if __name__ == "__main__":
    settings = get_devices_settings()
