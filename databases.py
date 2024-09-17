from pymongo import MongoClient

# Подключитесь к вашему серверу MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Замените URL на ваш

# Получите информацию о текущих операциях
current_ops = client.admin.command("currentOp")

# Выводим активные подключения
active_connections = [
    op for op in current_ops.get("inprog", []) if op.get("op") == "query"
]

for conn in active_connections:
    print(f"Connection ID: {conn.get('opid')}")
    print(f"Operation: {conn.get('op')}")
    print(f"Namespace: {conn.get('ns')}")
    print(f"Query: {conn.get('query')}")
    print(f"Client: {conn.get('client')}")
    print("-" * 40)
