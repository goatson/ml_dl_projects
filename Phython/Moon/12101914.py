from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options   # 크롬창 안뜨게

from bs4 import BeautifulSoup

url = "https://www.daum.net"

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome('chromedriver', options=chrome_options)
driver.get(url)


soup = BeautifulSoup(driver.page_source, 'lxml')
items = soup.select('#mArticle > div.cmain_tmp > div.section_media > div.hot_issue.issue_mini > div.hotissue_layer > ol > li')

# print(items)

for item in items:
    rank = item.find("span", {"class": "ir_wa"}).text
    ten = item.find("span", attrs={"class": "txt_issue"}).text  # find니까 첫번째꺼 들고온다.
    print(rank, ten)

#     description = item.find('p').text
#     print("t+" +title)
#     print("d" +description)