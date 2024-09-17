from pymongo import MongoClient

# Подключаемся к серверу MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Замените URL на ваш

# Получаем информацию о статусе сервера
server_status = client.admin.command("serverStatus")

# Извлекаем информацию о текущих подключениях
connections = server_status.get("connections", {})

# Выводим информацию о текущих подключениях
print(f"Total Connections: {connections.get('current', 'N/A')}")
print(f"Available Connections: {connections.get('available', 'N/A')}")
print(f"Total Created Connections: {connections.get('totalCreated', 'N/A')}")
