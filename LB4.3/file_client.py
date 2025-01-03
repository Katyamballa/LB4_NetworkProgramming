import socket

def send_file_to_server(file_path):
    # Создание сокета
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 65433)  # Хост и порт сервера

    print("Подключение к серверу...")
    client_socket.connect(server_address)

    try:
        with open(file_path, "rb") as file:
            print(f"Отправка файла '{file_path}' на сервер...")
            while chunk := file.read(1024):  # Чтение файла порциями по 1024 байта
                client_socket.sendall(chunk)
            print("Файл успешно отправлен.")
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
    finally:
        print("Отключение от сервера.")
        client_socket.close()

if __name__ == "__main__":
    file_path = input("Введите путь к текстовому файлу для отправки: ")
    send_file_to_server(file_path)
