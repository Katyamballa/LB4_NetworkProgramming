import socket

def start_file_server():
    # Создание сокета
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 65433)  # Хост и порт
    server_socket.bind(server_address)

    print("Сервер запущен и готов принимать файлы...")
    server_socket.listen(5)  # Ожидание подключений

    while True:
        connection, client_address = server_socket.accept()
        print(f"Подключение от клиента: {client_address}")

        try:
            with open("received_file.txt", "wb") as file:
                print("Начало приема файла...")
                while True:
                    data = connection.recv(1024)  # Получение данных по 1024 байта
                    if not data:
                        break
                    file.write(data)
                print("Файл успешно принят и сохранен как 'received_file.txt'.")
        finally:
            connection.close()

if __name__ == "__main__":
    start_file_server()
