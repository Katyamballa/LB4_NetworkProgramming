import socket

def start_echo_server():
    # Создание сокета
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 65432)  # Хост и порт
    server_socket.bind(server_address)

    print("Сервер запущен и ожидает подключения...")
    server_socket.listen(1)  # Прослушивание подключений

    while True:
        # Ожидание подключения
        connection, client_address = server_socket.accept()
        try:
            print(f"Подключение от {client_address}")

            while True:
                data = connection.recv(1024)  # Получение данных от клиента
                if data:
                    print(f"Получено: {data.decode()}")
                    connection.sendall(data)  # Отправка данных обратно клиенту
                else:
                    print("Клиент отключился.")
                    break
        finally:
            connection.close()

if __name__ == "__main__":
    start_echo_server()