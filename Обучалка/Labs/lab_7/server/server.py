import socket
import smtplib
from decouple import config
from hashlib import md5


def check(s):
    if s.find("@") > 0:
        return True
    else:
        return False


login = config('EMAIL_LOGIN')
password = config('EMAIL_PASSWORD')
HOST = '127.0.0.1'
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)
    while True:
        mail = conn.recv(1024)
        if check(mail.decode()) == True:
            conn.send(b'OK')
            break
        else:
            conn.send(b'Error occurred!')
    message = conn.recv(1024)
    id = int(md5(message).hexdigest(), 16) % (10 ** 10)
    mail = mail.decode()
    message = message.decode()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(login, password)
        message = 'Subject: ' + str(id) + '\n\n' + message
        smtp.sendmail(login, login, message)
        message = 'Subject: ' + str(id)
        smtp.sendmail(login, mail, message)