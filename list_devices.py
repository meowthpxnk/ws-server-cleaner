import psutil

for proc in psutil.process_iter(["pid", "name", "cmdline"]):
    print(proc.name())
