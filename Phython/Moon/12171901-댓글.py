import requests
from bs4 import BeautifulSoup
import time
import urllib.request 
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import datetime as dt





delay = 3
browser = Chrome()
browser.implicitly_wait(delay)

start_url="https://www.youtube.com/watch?v=0egKOXHb65w"
browser.get(start_url)
browser.maximize_window()

body = browser.find_element_by_tag_name('body')#스크롤하기 위해 소스 추출

pagedowns = 2
#10번 밑으로 내리는 것
while pagedowns:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)
    pagedowns -= 1

html0 = browser.page_source
soup = BeautifulSoup(html0, 'lxml')

video_list0 = soup.find_all('yt-formatted-string', id='content-text')
# print(video_list0)
comments=[]
for list in video_list0:
    comment = list.text
    comments.append(comment)
print(comments)


# video_list1 = soup.select('div#content > #content-text')
# print(video_list1,'%%%%%')
# for list in video_list1:
#     print(list.extract())