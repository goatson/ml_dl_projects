import urllib.request, time
from bs4 import BeautifulSoup

#벅스에서 차트 노래제목 가져오기 + 순위도 함께
url = "https://music.bugs.co.kr/chart"

response = urllib.request.urlopen(url)
soup = BeautifulSoup(response, "html.parser")
print(soup)

results1 = soup.select("th > p > a")
results2 = soup.select("td > div > strong")


for result in results1:
    print(result.text)

for result in results2:
    print(result.text)