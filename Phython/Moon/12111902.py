import urllib.request, time
from bs4 import BeautifulSoup

url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"

response = urllib.request.urlopen(url)
soup = BeautifulSoup(response, "html.parser")
print(soup)

results1 = soup.select("strong.title")
results2 = soup.select("strong.percent > span")

for result in results1:
    print(result.text)

for result in results2:
    print(result.text)