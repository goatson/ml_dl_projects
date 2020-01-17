
import urllib.request, time
from bs4 import BeautifulSoup

url = "http://www.cgv.co.kr/movies/"
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response, 'lxml')
#contents > div.wrap-movie-chart > div.sect-movie-chart
result_t = soup.select('strong.title')
result_p = soup.select('strong.percent')

# result = soup.select("#contents > div.wrap-movie-chart > div.sect-movie-chart > ol > li > div ")

for i in result_t:
    print(i.text)

for j in result_p:
    print(j.text)

# for k in result:
#     title = k.find(class_='title').text
#     percent = k.find(class_='percent').text
#     print(title)
#     print(percent)

