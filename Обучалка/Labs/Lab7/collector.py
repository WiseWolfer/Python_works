import email
from imaplib import IMAP4_SSL
from time import sleep
import logging


# читаем из .env файлов логин и пароль
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
        elif d == 'PERIOD_CHECK':
            period_check = dictionary[d]
            counter += 1
        elif counter == 3:
            break

with IMAP4_SSL("imap.gmail.com", 993) as M:
    rc, resp = M.login(login, password)
    # Выводит список папок в почтовом ящике.
    # Подключаемся к папке "входящие".
    M.select('inbox')
    while True:
        # выбираем последние письма
        # начинаем с поиска с входящих при помощи функции поиска
        typ, data = M.search(None, 'ALL')
        ids = data[0]   # Получаем строку номеров писем
        id_list = ids.split()   # Разделяем ID писем
        latest_email_id = id_list[-1]   # Берем последний ID
        result, data = M.fetch(latest_email_id, "(RFC822)") # Получаем тело письма (RFC822) для данного ID
        raw_email = data[0][1] # Тело письма в необработанном виде
        # включает в себя заголовки и альтернативные полезные нагрузки
        try:
            # конвертируем сообщение в объект EmailMessage
            email_message = email.message_from_string(raw_email.decode())
            ID = email_message['Subject']
            print('ID: ' + ID)
            logging.basicConfig(filename="success_request.log", level=logging.INFO, filemode='w')
            logging.info(f'No errors. ID: {ID}')
        except:
            logging.basicConfig(filename="error_request.log", level=logging.ERROR, filemode='a')
            logging.error('Error! Can\'t reach an ID.')
        sleep(int(period_check))