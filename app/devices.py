from app.utils.list_processes import get_processes
from app.utils.devices_settings import get_devices_settings


class Device: ...


def analyse_devices():
    processes = get_processes()
    settings = get_devices_settings()
    # print(processes)
    # print(len(processes))

    # for p in processes:
    #     if not p.port:
    #         print(p)
    # print(settings)

    process_preparing = {process.port: process for process in processes}
    print(process_preparing)
