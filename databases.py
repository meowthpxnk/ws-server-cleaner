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
            connections.append(op)
    return connections


if __name__ == "__main__":
    connections = get_database_connections()
    print(f"Connections count: {len(connections)}")
