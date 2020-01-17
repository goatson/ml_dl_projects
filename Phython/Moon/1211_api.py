import requests
from bs4 import BeautifulSoup

service_key ="6o38RyzdWEzqjYYmC3ygvZYm4gaLQ0bqt6kOTUEchGga7QehtVFaQIp1QS%2FQ2iepln6KRWliIZOhcUvW3rvpEA%3D%3D"
open_api =f"http://apis.data.go.kr/6260000/BusanPopulationStaticService/getPopulationInfo?serviceKey={service_key}&numOfRows=5&pageNo=1"
# &resultType=json

res = requests.get(open_api)
# print(res.content)
soup = BeautifulSoup(res.content, 'lxml')
# print(soup)
data = soup.find_all('item') 
print(data)



# for item in data:
#     gugun = item.find('gugun').text
#     totPopCnt = item.find('totPopCnt').text
#     print(gugun,totPopCnt)
