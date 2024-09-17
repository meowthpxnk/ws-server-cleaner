import psutil


class Process:
    pid: int
    port: int

    def __init__(self):
        self.port = None
        self.pid = None

    def __repr__(self) -> str:
        return f"<ClProcess: pid={self.pid}, port={self.port}>"


def get_processes() -> list[Process]:
    processes = []
    for proc in psutil.process_iter(["pid", "name", "cmdline"]):

        if proc.name() == "node":
            p = Process()

            connections = proc.connections(kind="inet")
            for conn in connections:
                if conn.status == "LISTEN":
                    p.port = conn.laddr.port

            p.pid = proc.pid
            processes.append(p)
    return processes


if __name__ == "__main__":
    processes = get_processes()
    print(processes)
    print(f"Processes count: {len(processes)}")
