import requests
from bs4 import BeautifulSoup

url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"

r = requests.get(url)

bs = BeautifulSoup(r.text, "html.parser")

movies = bs.find_all("strong")

print(movies)