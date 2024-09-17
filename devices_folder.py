import os
import yaml

ROOT_PATH = "/clicker/users"
SETTINGS_PATH = "clicker_settings.yaml"


class Settings:
    port: int

    def __repr__(self) -> str:
        return f"<ClSettings: port={self.port}>"


def parse_settings(settings_s):

    settings = yaml.safe_load(settings_s)

    s = Settings()
    whatsapp = settings.get("whatsapp")

    if whatsapp:
        s.port = whatsapp.get("port")

    return s


def get_devices_folders():
    device_names = os.listdir(ROOT_PATH)

    for device_name in device_names:
        settings_file = os.path.join(ROOT_PATH, device_name, SETTINGS_PATH)

        with open(settings_file) as f:
            settings_s = f.read()
            settings = parse_settings(settings_s)
            print(settings)


if __name__ == "__main__":
    folders = get_devices_folders()
