import psutil


def get_devices():
    devices = []
    for proc in psutil.process_iter(["pid", "name", "cmdline"]):
        if proc.name() == "node":
            devices.append(proc)
    return devices


if __name__ == "__main__":
    devices = get_devices()
    print(devices)
