from app.utils.list_processes import get_processes
from app.utils.devices_settings import get_devices_settings


def analyse_devices():
    processes = get_processes()
    # settings = get_devices_settings()
    print(processes)
    print(len(processes))

    # for p in processes:
    #     if not p.port:
    #         print(p)
    # print(settings)
