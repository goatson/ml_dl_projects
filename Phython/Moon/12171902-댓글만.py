import requests
from bs4 import BeautifulSoup
import time
import urllib.request 
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import datetime as dt
import json

## 유투브 재생을 위한 링크, 제목 크롤링 ##

### 유투브 댓글 크롤링 ###
# kbo_commentlink = ["/watch?v=0egKOXHb65w", "/watch?v=A5vCPtjOe8Q", "/watch?v=4e-wna5zkMA", "/watch?v=bQU_2ifYdrA", "/watch?v=arTzBrLAUjs", "/watch?v=YTxL6SsmVus", "/watch?v=2TdnV4KFlkQ", "/watch?v=QTLLGiWGWm0", "/watch?v=gzi30ZmSdEw", "/watch?v=3Q9hSVtdBcs"]
kbo_commentlink = ["/watch?v=0egKOXHb65w", "/watch?v=A5vCPtjOe8Q", "/watch?v=4e-wna5zkMA"]
kbo_comments=[]
for li in kbo_commentlink:
    delay = 3
    browser = Chrome()
    browser.implicitly_wait(delay)

    start_url="https://www.youtube.com" + li
    browser.get(start_url)
    browser.maximize_window()
    print(start_url)
    time.sleep(3)
    body = browser.find_element_by_tag_name('body')

    pagedowns = 1  #2번 밑으로
    while pagedowns:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        pagedowns -= 1
    time.sleep(3)    
    print('@@@@@@@여기까지 정상')


    html0 = browser.page_source
    soup = BeautifulSoup(html0, 'lxml')

    
    comment_list = soup.find_all('yt-formatted-string', id='content-text')
    comments=[]
    for list in comment_list:
        comment = list.text
        comments.append(comment) # 영상마다 1차 리스트 생성
    print(comments,'@@@1차리스트@@')
    kbo_comments.append(comments) # 영상 다 합쳐서 2차 리스트 생성
    browser.close()
    
print(kbo_comments, '####2차리스트####')


# with open('./kbo_comments.json','wt') as f:
#     json.dump(kbo_comments,f)       
    







# delay = 3
# browser = Chrome()
# browser.implicitly_wait(delay)

# start_url="https://www.youtube.com/watch?v=0egKOXHb65w"
# browser.get(start_url)
# browser.maximize_window()

# body = browser.find_element_by_tag_name('body')#스크롤하기 위해 소스 추출

# pagedowns = 2
# #10번 밑으로 내리는 것
# while pagedowns:
#     body.send_keys(Keys.PAGE_DOWN)
#     time.sleep(2)
#     pagedowns -= 1

# html0 = browser.page_source
# soup = BeautifulSoup(html0, 'lxml')

# video_list0 = soup.find_all('yt-formatted-string', id='content-text')
# # print(video_list0)
# comments=[]
# for list in video_list0:
#     comment = list.text
#     comments.append(comment)
# print(comments)






# video_list1 = soup.select('div#content > #content-text')
# print(video_list1,'%%%%%')
# for list in video_list1:
#     print(list.extract())