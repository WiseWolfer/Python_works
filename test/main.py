import requests, json


if __name__ == '__main__':
    #Создаю постоянное HTTP соединение
    session = requests.Session()
    method = 'net_version'
    params = []
    payload = {"jsonrpc": "2.0",
               "method": method,
               " параметры": params,
               "идентификатор": 1}
    headers = {'Content - type': 'application/json'}

    response =session.post('http://localhost:7545', json=payload, headers=headers)
    print('raw json response: {}'.format(response.json()))
    print('network id: {}'.format(response.json()['result']))