from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
# 야구 선수기록 URL
url = "https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx"

chrome_options = Options()
chrome_options.add_argument("--headless")


# 뷰티풀숩 객체 생성 lxml 파서 사용
driver = webdriver.Chrome('chromedriver', options=chrome_options)
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')
lists = soup.select("#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr")
# select 함수로

# print(lists)

for list in lists:
    player = list.text
    print(player)




# lists 요소만큼 반복
# for player in players:
#     # lists의 요소인 li(tr) 요소 하위에 td 태그인 요소의 text값을 player에 저장
#     player = li.find_all
#     print(player)
    
