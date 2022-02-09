from django.shortcuts import render
import pycoin
import requests, json
from bitcoinrpc.authproxy import AuthServiceProxy


def index(request):
    return render(request, 'main/index.html')


def transactions(request):
    if request.method == "GET":
        rpc_user = 'bcs_tester'
        rpc_password = 'iLoveBCS'

        # соединяюсь и авторизуюсь через rpc_user и rpc_password,
        # timeout - ждем подключение 120 секунд
        rpc_connection = AuthServiceProxy("http://%s:%s@45.32.232.25:3669" %
                                                                (rpc_user,
                                                                rpc_password),
                                                                timeout=120)

        # получаю новый адрес (первый аргумент -метка(label)( с именем(строка, если нет ее
        # тогда присваивается сама), второй аргумент - строка(адрес))
        # Адрес может быть либо p2sh-segwit, либо bech32.
        new_address = rpc_connection.getnewaddress("label", "p2sh-segwit")
        print(new_address)
        print('-----------------------------------')
        status = rpc_connection.getblockchaininfo()
        print(status)
        print('------------------------------------')

        # запись транзакций в переменную в формат json и вывод их на экран(20 штук)
        # * - возврат всех транзакций, второй аргумент число возвращаемых входящих транзакций
        transactions = rpc_connection.listtransactions("*", 20)
        print(transactions)

        # возврат на сайт во фронтенде
        return render(request, 'main/index.html')