import socket
from smtplib import SMTP
from decouple import config
import configparser


def send_request():
    host = '127.0.0.1'
    port = 50007    
    msg = input("Введите сообщение: ")
    email = input("Введите вашу почту: ")

    # создаем TCP/IP сокет
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            s.send(email.encode())
            data = s.recv(1024)
            print(data.decode())
            if data.decode() == "OK":
                break
            else:
                print("Error!!")
                email = input("Введите вашу почту: ")
                msg = input("Введите сообщение снова: ")
        s.send(msg.encode())


def main():
    send_request()


if __name__ == '__main__':
    main()

