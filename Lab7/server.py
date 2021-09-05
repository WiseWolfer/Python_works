import socket
from hashlib import md5
import smtplib
import urllib.parse


def check(address):
    if "@" in address:
        return True
    else:
        return False


filename = "spisok.env"
selfy_dictionary = []
with open(filename, 'r', encoding="utf8") as file:
    for item in file:
        result = item.strip("\n").split("=")
        selfy_dictionary.append(result)
    dictionary = dict()
    for item in selfy_dictionary:
        for j in range(len(selfy_dictionary)):
            dictionary[selfy_dictionary[j][0]] = selfy_dictionary[j][1]
    counter = 0
    for d in dictionary.keys():
        if d == "EMAIL_LOGIN":
            login = dictionary[d]
            counter +=1
        elif d == 'EMAIL_PASSWORD':
            password = dictionary[d]
            counter += 1
        elif counter == 2:
            break
HOST = '127.0.0.1'
PORT = 50007
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print("Connected by", addr)
    while True:
      mail = conn.recv(1024)
      if check(mail.decode()) == True:
      # b - это байты, по байтам передаем OK
        conn.send(b'OK')
        break
      else:
        conn.send(b'Error occurred!')

    message = conn.recv(1024)
    # шифруем id с помощью алгоритма md5 (формируем id)
    id = int(md5(message).hexdigest(), 16) % (10 ** 10)
    mail = mail.decode()
    message = message.decode()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(login, password)
        message = 'Subject: ' + str(id) + '\n\n' + message
        # отправляем сообщение на почту администратора с его же почты
        smtp.sendmail(login, login, message)
        message = 'Subject: ' + str(id)
        # отправляем сообщение на почту пользователя с почты администратора
        smtp.sendmail(login, mail, message)