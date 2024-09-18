from app.utils.list_processes import get_processes, Process
from app.utils.devices_settings import get_devices_settings, Settings


class Device:
    process: Process
    settings: Settings

    def __repr__(self) -> str:
        return f"<Device: settings={self.settings}, process={self.process}>"


def analyse_devices():
    processes_list = get_processes()
    settings_list = get_devices_settings()
    # print(processes)
    # print(len(processes))

    # for p in processes:
    #     if not p.port:
    #         print(p)
    # print(settings)

    settings_prep = {settings.port: settings for settings in settings_list}
    # print(process_preparing)

    devices = []

    for process in processes_list:
        device = Device()
        device.process = process
        device.settings = settings_prep.get(process.port)
        devices.append(device)
        print(device)

    # print(devices)
