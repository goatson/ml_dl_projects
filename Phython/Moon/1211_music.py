import urllib.request, time
from bs4 import BeautifulSoup

url = "https://music.bugs.co.kr/chart"
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response, 'lxml')

results = soup.select(" #CHARTrealtime > table > tbody > tr > th > p > a")
for i in results:
    print(i.text)

    