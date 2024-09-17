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
    # Также можно попытаться извлечь информацию о драйверах
    driver_info = op.get(
        "desc", "N/A"
    )  # Описание может включать информацию о драйвере

    print(f"Operation ID: {opid}")
    print(f"Operation Type: {op_type}")
    print(f"Namespace: {ns}")
    print(f"Query: {query}")
    print(f"Client: {client_info}")
    print(f"Driver Info: {driver_info}")
    print("-" * 40)
