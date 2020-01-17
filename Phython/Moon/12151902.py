from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib.request, time





driver = webdriver.Chrome('./chromedriver.exe')
driver.get("https://www.youtube.com/")
time.sleep(1)


driver.find_element_by_xpath('//*[@id="search"]')
driver.find_element_by_xpath('//*[@id="search"]').send_keys('KBO 레전드')
driver.find_element_by_xpath('//*[@id="search"]').send_keys(Keys.ENTER)
time.sleep(1)

youtube1 = driver.find_element_by_xpath('//*[@id="video-title"]')
youtube1.click()


url = driver.current_url
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response, 'lxml')

body = soup.find('body')
# print(body)
comment = body.select('div#contents > yt-formatted-string#content-text')
# comment1 = body.find_all('div', class_='style-scope ytd-item-section-renderer', id='contents')
print(comment, "@@@@@@")
# print(comment1, '!!!!!!')

for i in comment:
    print(i,"~~~~~")

# for j in comment1:
#     print(j,"%%%%%%")    






