from pymongo import MongoClient


def get_database_connections():
    # Подключаемся к серверу MongoDB
    client = MongoClient("mongodb://localhost:27017/")  # Замените URL на ваш

    # Получаем информацию о текущих операциях
    current_ops = client.admin.command("currentOp")

    # Извлекаем текущие операции
    operations = current_ops.get("inprog", [])

    connections = []

    # Выводим информацию о текущих операциях и клиентах
    for op in operations:
        client_metadata = op.get("clientMetadata", {})
        driver_name = client_metadata.get("driver", {}).get("name", "N/A")
        if driver_name == "nodejs":
            op_info = {
                "opid": op.get("opid", "N/A"),
                "client": op.get("client", "N/A"),
                "ns": op.get("ns", "N/A"),
                "op": op.get("op", "N/A"),
                "query": op.get("query", "N/A"),
                "command": op.get("command", "N/A"),
            }
            connections.append(op_info)
    return connections


if __name__ == "__main__":
    connections = get_database_connections()
    print(f"Connections count: {len(connections)}")

    for conn in connections:
        print(f"Connection ID: {conn['opid']}")
        print(f"Client: {conn['client']}")
        print(f"Namespace: {conn['ns']}")
        print(f"Operation: {conn['op']}")
        print(f"Query: {conn['query']}")
        print(f"Command: {conn['command']}")
        print("-" * 40)
