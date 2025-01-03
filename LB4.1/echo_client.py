import socket

def start_echo_client():
    # Создание сокета
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 65432)  # Хост и порт сервера

    print("Подключение к серверу...")
    client_socket.connect(server_address)

    try:
        while True:
            message = input("Введите сообщение (или 'exit' для выхода): ")
            if message.lower() == 'exit':
                break

            client_socket.sendall(message.encode())  # Отправка данных серверу

            # Получение ответа от сервера
            data = client_socket.recv(1024)
            print(f"Ответ от сервера: {data.decode()}")
    finally:
        print("Отключение от сервера.")
        client_socket.close()

if __name__ == "__main__":
    start_echo_client()
