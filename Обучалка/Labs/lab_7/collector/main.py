import email
from imaplib import IMAP4_SSL
from time import sleep
import logging
from decouple import config


login = config('EMAIL_LOGIN')
password = config('EMAIL_PASSWORD')
with IMAP4_SSL("imap.gmail.com", 993) as M:
    rc, resp = M.login(login, password)
    M.select('inbox')
    while True:
        typ, data = M.search(None, 'ALL')
        ids = data[0]
        id_list = ids.split()
        latest_email_id = id_list[-1]
        result, data = M.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1]
        try:
            email_message = email.message_from_string(raw_email.decode())
            ID = email_message['Subject']
            print('ID: ' + ID)
            logging.basicConfig(filename="success_request.log", level=logging.INFO, filemode='w')
            logging.info(f'No errors. ID: {ID}')
        except:
            logging.basicConfig(filename="error_request.log", level=logging.ERROR, filemode='a')
            logging.error('Error! Can\'t reach an ID.')
        sleep(int(config('PERIOD_CHECK')))
