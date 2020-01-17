from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

url = "https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx"

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome('chromedriver', options=chrome_options)
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')
lists = soup.select("#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr" )
print(lists)

for li in lists :
    player = li.text
    print(player)