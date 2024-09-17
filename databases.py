from pymongo import MongoClient

# Подключаемся к серверу MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Замените URL на ваш

# Получаем информацию о текущих операциях
current_ops = client.admin.command("currentOp")

# Извлекаем текущие операции
operations = current_ops.get("inprog", [])

# Выводим информацию о текущих операциях и клиентах
for op in operations:
    opid = op.get("opid", "N/A")
    op_type = op.get("op", "N/A")
    ns = op.get("ns", "N/A")
    query = op.get("query", "N/A")
    client_info = op.get("client", "N/A")

    # Извлекаем clientMetadata
    client_metadata = op.get("clientMetadata", {})
    driver_name = client_metadata.get("driver", {}).get("name", "N/A")
    driver_version = client_metadata.get("driver", {}).get("version", "N/A")

    print(f"Operation ID: {opid}")
    print(f"Operation Type: {op_type}")
    print(f"Namespace: {ns}")
    print(f"Query: {query}")
    print(f"Client: {client_info}")
    print(f"Driver Name: {driver_name}")
    print(f"Driver Version: {driver_version}")
    print("-" * 40)
