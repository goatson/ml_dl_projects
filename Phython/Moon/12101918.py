# curl "https://openapi.naver.com/v1/papago/n2mt" \
#     -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" \
#     -H "X-Naver-Client-Id: {rcsY_s0nZ7RMgqXAgQ8I}" \
#     -H "X-Naver-Client-Secret: {vXaF2xoeRd}" \
#     -H "source=ko&target=en&text=만나서 반갑습니다." -v

import os
import sys
import urllib.request
client_id = "wXwfUz40FmfaOt799l1I"
client_secret = "ZD4oDwymd9"
encQuery = urllib.parse.quote("만나서 반갑습니다")
data = "query=" + encQuery
url = "https://openapi.naver.com/v1/papago/detectLangs"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)