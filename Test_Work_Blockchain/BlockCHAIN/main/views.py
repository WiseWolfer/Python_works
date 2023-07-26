import bitcoinrpc.authproxy
import pycoin.networks.bitcoinish
from django.shortcuts import render
from bitcoinrpc.authproxy import AuthServiceProxy
import requests
from pycoin.networks.bitcoinish import create_bitcoinish_network
from pycoin.symbols.btc import network




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

        network = create_bitcoinish_network(symbol="ARG", network_name="Argentum",
                                            subnet_name="mainnet", wif_prefix_hex="97",
                                            address_prefix_hex="17", pay_to_script_prefix_hex="05",
                                            bip32_prv_prefix_hex="0488ade4", bip32_pub_prefix_hex="0488b21e")

        # Получение вывода неизрасходованных транзакций UTXO через API
        response_UTXO = requests.api.get('https://bcschain.info/api/address/BEWRJgEgTBHSN8hndXnbjh1EnYT3jBFETc/utxo')
        print(response_UTXO.text)

        # генерация транзакции и ее подписание с помощью приватного ключа
        # L1cVGCBhdeWrULDyndqLeoMkeADfx8CGm9APHKtb7KJ12YQ7Z81J - приватный ключ
        my_wallet = 'BEWRJgEgTBHSN8hndXnbjh1EnYT3jBFETc'

        # Генерация транзакции
        money = 0.00000001
        MY_ADDRESS = ['BEWRJgEgTBHSN8hndXnbjh1EnYT3jBFETc']
        key = pycoin.networks.bitcoinish.Key('BEWRJgEgTBHSN8hndXnbjh1EnYT3jBFETc')
        print(key)
        tx = 'ed980aeca8f1fd127ffaddd833ddb67feb761477d490a12ade2f5f7bb178173c'
        signed_tx = pycoin.networks.bitcoinish.sign_tx(network, tx, ['L1cVGCBhdeWrULDyndqLeoMkeADfx8CGm9APHKtb7KJ12YQ7Z81J'])
        print(signed_tx)
        # отправка в блокчейн с помощью апи
        url = 'https://bcschain.info/pushtx'
        hex_tx = ''
        x = requests.post(url, data={'tx': hex_tx})
        result = x.text
        print(result)

        # возврат на сайт во фронтенде
        return render(request, 'main/index.html')
