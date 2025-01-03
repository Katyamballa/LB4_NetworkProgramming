import socket
import threading

def handle_client(connection, client_address):
    """Обработка запросов клиента."""
    print(f"Подключение от клиента: {client_address}")

    try:
        while True:
            data = connection.recv(1024)  # Получение данных от клиента
            if data:
                print(f"Получено от {client_address}: {data.decode()}")
                connection.sendall(data)  # Отправка данных обратно клиенту
            else:
                print(f"Клиент {client_address} отключился.")
                break
    finally:
        connection.close()

def start_multi_client_server():
    # Создание сокета
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 65432)  # Хост и порт
    server_socket.bind(server_address)

    print("Сервер запущен и готов принимать подключения...")
    server_socket.listen(5)  # Сервер может слушать до 5 подключений в очереди

    while True:
        # Ожидание нового подключения
        connection, client_address = server_socket.accept()

        # Создание нового потока для обработки клиента
        client_thread = threading.Thread(target=handle_client, args=(connection, client_address))
        client_thread.start()

if __name__ == "__main__":
    start_multi_client_server()
