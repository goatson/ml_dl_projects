from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib.request, time
from pytube import YouTube


driver = webdriver.Chrome('./chromedriver.exe')
kbo = driver.get("https://www.youtube.com/")
time.sleep(1)


driver.find_element_by_xpath('//*[@id="search"]')
driver.find_element_by_xpath('//*[@id="search"]').send_keys('KBO 레전드')
driver.find_element_by_xpath('//*[@id="search"]').send_keys(Keys.ENTER)
time.sleep(2)

url = driver.current_url
# url = "https://www.youtube.com/results?search_query=KBO+%EB%A0%88%EC%A0%84%EB%93%9C"
# print(url)
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response, 'lxml')
# print(response)

results = soup.select('h3 > a')
# print(type(results))
result = results[3:8]

# kbo_legend=[]
for video in result:
    # print(video)
    print(video.attrs['href'])
    # kbo_legend.append(video.attrs['href'])
# print(kbo_legend)
    yt = YouTube("https://www.youtube.com" + video.attrs['href'])
    print(yt)
    yt.streams.first().download()



# for key in kbo_legend:
#     yt = YouTube("https://www.youtube.com" + key)
#     yt
    





    url_1 = "https://www.youtube.com/watch?v=SQmrWr8YuC8&feature=emb_logo"
    response_1 = urllib.request.urlopen(url_1)
    soup_1 = BeautifulSoup(response_1, 'lxml')
    comment1 = soup_1.select('#content-text')
    print(comment1)


    

