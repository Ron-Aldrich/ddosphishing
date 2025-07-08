import requests
import time

cookies = {
    'PHPSESSID': 'dlord7l684c2oru18p0kvamdnl',
    'cf_clearance': '.rZBvNvpw_Q2gyKxVO2uxyohVoS1WbO0hsCubK0uuRA-1751641756-1.2.1.1-n2io47ecxZr6avceTYMHmlrorb.6oK1fICB3dozQUj8zZxW7TgY3bMLUqLry7hF6mD_idUK849JcCPIMbDEcVpu_K0WWyUhQcTqSxjPkuLTqYhczV4T1Wgst.7tp8MDEfofRoYLqzjJF6uONEbyWsTsb0j9.c6.V8fPScHfW1QeK0HJ6XiZatiOQg7KA4M.kj5AAAqfsVMOQRQe8IPbB5CPZV3268Bqgt_BhB5AnZXw',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-PH,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://zelo-store.com',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'PHPSESSID=dlord7l684c2oru18p0kvamdnl; cf_clearance=.rZBvNvpw_Q2gyKxVO2uxyohVoS1WbO0hsCubK0uuRA-1751641756-1.2.1.1-n2io47ecxZr6avceTYMHmlrorb.6oK1fICB3dozQUj8zZxW7TgY3bMLUqLry7hF6mD_idUK849JcCPIMbDEcVpu_K0WWyUhQcTqSxjPkuLTqYhczV4T1Wgst.7tp8MDEfofRoYLqzjJF6uONEbyWsTsb0j9.c6.V8fPScHfW1QeK0HJ6XiZatiOQg7KA4M.kj5AAAqfsVMOQRQe8IPbB5CPZV3268Bqgt_BhB5AnZXw',
}

data = {
    'email': 'cnhs@gmail.com',
    'password': 'Youcanefoolme',
    'login': 'Google',
    'nox': '8049984216',
}

for x in range(90000):
    response = requests.post('https://zelo-store.com/F-2/MG/sender1.php', cookies=cookies, headers=headers, data=data)
    print("[!]Status: ", response.status_code)
    print("Attempts: ", x)
    time.sleep(5)
