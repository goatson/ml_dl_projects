import urllib.request, time
from bs4 import BeautifulSoup

url = "https://www.yna.co.kr/"
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response, 'lxml')


results = soup.select("#content > div.column-wrap > div.col-cont.column-headline > div.column-area01 > div > ul > li > div.news-con")
for i in results:
    print(i.text)