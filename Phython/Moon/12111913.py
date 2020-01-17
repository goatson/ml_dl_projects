import requests
from bs4 import BeautifulSoup

service_key = '13YeikAe1cuHvEhclv1cGimbw%2BK0gC4f7M3DLONxaC%2B94AbL1%2FtLhvW2BdJtwrArZwv1%2Bysib7B6RNCXH3Xz%2BA%3D%3D'
open_api = 'http://apis.data.go.kr/B553077/api/open/sdsc/storeZoneOne?key=573&ServiceKey=' + service_key
# http://apis.data.go.kr/B553077/api/open/sdsc/baroApi?resld=storezone&key=573&ServiceKey=

res = requests.get(open_api)
# print(res.text)
soup = BeautifulSoup(res.content, 'html.parser')

data = soup.find_all('item')
for item in data:
    bizesId = item.find('bizesid')
    bizesNm = item.find('bizesnm')
    print(bizesId.get_text(), bizesNm.get_text())
    # stationname = item.find('stationname')
    # pm10grade = item.find('pm10grade')
    # print(stationname.get_text(), pm10grade.get_text())
    

