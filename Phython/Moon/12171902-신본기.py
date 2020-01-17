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
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome('./chromedriver.exe', options=chrome_options)
driver.get("https://www.youtube.com/")
time.sleep(1)


driver.find_element_by_xpath('//*[@id="search"]')
driver.find_element_by_xpath('//*[@id="search"]').send_keys('신본기')
driver.find_element_by_xpath('//*[@id="search"]').send_keys(Keys.ENTER)
time.sleep(1)

url = driver.current_url
# url = "https://www.youtube.com/results?search_query=KBO+%EB%A0%88%EC%A0%84%EB%93%9C"
# print(url)
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response, 'lxml')
# print(response)

results = soup.select('h3 > a')
# print(type(results))
result = results[0:2]
# print(results)
kbo_title=[]
kbo_link=[]
kbo_commentlink=[]  ##댓글을 크롤링을 위한 주소
for video in result:
    # print(video)
    # link = video.attrs['href'].replace('/watch?v=','/embed/')
    link = video.attrs['href']  #링크 크롤링
    title = video.attrs['title'] #제목 크롤링
    # print(link, title)
    kbo_commentlink.append(link)
    kbo_link.append(link.replace('/watch?v=','/embed/'))
    kbo_title.append(title)
# print(kbo_link)
# print(kbo_commentlink)    
driver.close()

# with open('./kbo_title.json','wt') as f:
#     json.dump(kbo_title,f)    
# with open('./kbo_link.json','wt') as f:
#     json.dump(kbo_link,f)    


### 유투브 댓글 크롤링 ###
kbo_bonki=[]
for li in kbo_commentlink:
    delay = 2
    browser = Chrome()
    browser.implicitly_wait(delay)

    start_url="https://www.youtube.com" + li
    browser.get(start_url)
    browser.maximize_window()
    print(start_url)
    time.sleep(3)
    body = browser.find_element_by_tag_name('body')

    pagedowns = 2  #2번 밑으로
    while pagedowns:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        pagedowns -= 1
    time.sleep(3)    
    print('@@@@@@@여기까지 정상')


    html0 = browser.page_source
    soup = BeautifulSoup(html0, 'lxml')

    comment_list = soup.find_all('yt-formatted-string', id='content-text', limit=5)
    comments=[]
    for list in comment_list:
        comment = list.text
        comments.append(comment) # 영상마다 1차 리스트 생성
    print(comments,'@@@1차리스트@@')
    kbo_bonki.append(comments) # 영상 다 합쳐서 2차 리스트 생성
    browser.close()
    
print(kbo_bonki, '####2차리스트####')


with open('./kbo_bonki.json','wt') as f:
    json.dump(kbo_bonki,f)       
    
#톰 탱고 포인트는 ESPN 예측보다 훨씬 쉬운 계산법을 쓴다.
#  투구 이닝을 2로 나눈 수치에서 자책점을 빼고, 여기에 탈삼진을 10으로 나눈 수치와 승수 등 세 항목을 더해 점수를 계산하는 방식이다.
#  더 많은 이닝을 던지면서 자책점이 적고 탈삼진과 승수가 높을수록 점수를 많이 얻게 된다.






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