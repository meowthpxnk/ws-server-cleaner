import psutil


class Process:
    pid: int
    # port: int

    def __repr__(self) -> str:
        return f"<ClProcess: pid={self.pid}>"


def get_processes():
    processes = []
    for proc in psutil.process_iter(["pid", "name", "cmdline"]):

        if proc.name() == "node":

            connections = proc.connections(kind="inet")
            for conn in connections:
                print(conn.laddr.ip)
            # ports = [conn.laddr.port for conn in connections]

            # print(ports)
            print(connections)

            p = Process()
            p.pid = proc.pid
            processes.append(p)
    return processes


if __name__ == "__main__":
    processes = get_processes()
    print(processes)
    print(f"Processes count: {len(processes)}")
