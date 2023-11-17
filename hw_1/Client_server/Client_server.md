Вот пример простого скрипта на Python, который использует сокеты для передачи файла между двумя блокнотами. Для удобства я буду использовать библиотеку socket и простой протокол:

Сначала, на стороне сервера (получателя файла), создайте файл server.py:


'
import socket

def receive_file(server_address, server_port):
    # Создаем сокет
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Привязываем сокет к адресу и порту
        server_socket.bind((server_address, server_port))
        # Начинаем прослушивание
        server_socket.listen()

        print(f"Сервер слушает на {server_address}:{server_port}")

        # Принимаем соединение
        client_socket, client_address = server_socket.accept()
        print(f"Установлено соединение с {client_address}")

        with client_socket:
            # Получаем имя файла
            file_data = client_socket.recv(1024)
            file_name = file_data.decode('utf-8')
            
            # Открываем файл для записи
            with open(file_name, 'wb') as file:
                print(f"Получен файл: {file_name}")
                while True:
                    # Продолжаем получать данные и записывать их в файл
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    file.write(data)

    print("Передача файла завершена")

    if __name__ == "__main__":
    receive_file('127.0.0.1', 12345)

'

Теперь, на стороне клиента (отправителя файла), создайте файл client.py:

'
import socket

def send_file(server_address, server_port, file_path):
    # Создаем сокет
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # Устанавливаем соединение с сервером
        client_socket.connect((server_address, server_port))

        # Получаем имя файла из пути
        file_name = file_path.split('\\')[-1]
        # Отправляем имя файла
        client_socket.send(file_name.encode('utf-8'))

        # Открываем файл для чтения в бинарном режиме
        with open(file_path, 'rb') as file:
            # Читаем и отправляем файл по частям
            for data in iter(lambda: file.read(1024), b''):
                client_socket.sendall(data)

    print("Файл успешно отправлен")

    if __name__ == "__main__":
    # Укажите путь к файлу, который хотите отправить
    send_file('127.0.0.1', 12345, 'путь_к_файлу\\имя_файла')

'

Обратите внимание, что необходимо указать путь к файлу в client.py в строке send_file('127.0.0.1', 12345, 'путь_к_файлу\\имя_файла'). Пожалуйста, замените 'путь_к_файлу\\имя_файла' в send_file на путь к файлу, который вы хотите отправить.

Запустите server.py на блокноте, который будет принимать файл, и client.py на блокноте, который будет отправлять файл. Передача файла будет происходить через локальную сеть по адресу 127.0.0.1 и порту 12345.

Далее, попробуйте сделать то же самое в колаб Блокнотах, которые будут расположены в одной папке.
