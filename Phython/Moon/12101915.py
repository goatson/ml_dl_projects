##네이버 Open API 사용하기  /  lxml 속도 비교

import requests
import pprint

client_id = 'wXwfUz40FmfaOt799l1I'
client_secret = 'ZD4oDwymd9'

naver_open_api = 'https://openapi.naver.com/v1/search/shop.json?query=스마트'
header_params = {"X-Naver-Client-Id":client_id, "X-Naver-Client-Secret":client_secret}
res = requests.get(naver_open_api, headers=header_params)


if res.status_code == 200:
    data = res.json()
    for index, item in enumerate(data['items']):
        print (index + 1, item['title'], item['link'])
else:
    print("Error Code:", res.status_code)