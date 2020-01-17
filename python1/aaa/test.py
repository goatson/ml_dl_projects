import requests
from bs4 import BeautifulSoup
res = requests.get('http://www.naver.com')
soup = BeautifulSoup(res.content, 'html.parser')  # BeautifulSoup에는 html.parser라는 명령어가 있다.
mydata = soup.find('h3', "ah_ltit") #title이라는 data만 가져온다
print(mydata.get_text())