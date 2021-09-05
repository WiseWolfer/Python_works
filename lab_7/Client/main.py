import socket
from decouple import config


mail = input('Input mail: ')
message = input('Input message: ')
username = config('EMAIL_LOGIN')
password = config('EMAIL_PASSWORD')
HOST = '127.0.0.1'
PORT = 50007
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.send(mail.encode())
        data = s.recv(1024)
        print(data.decode())
        if data.decode() != 'OK':
            print('Error!')
            mail = input('Input mail: ')
            message = input('Input message: ')
        else:
            break
    s.send(message.encode())
