from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib.request, time


driver = webdriver.Chrome('./chromedriver.exe')
kbo = driver.get("https://www.youtube.com/")
time.sleep(1)


driver.find_element_by_xpath('//*[@id="search"]')
driver.find_element_by_xpath('//*[@id="search"]').send_keys('KBO 레전드')
driver.find_element_by_xpath('//*[@id="search"]').send_keys(Keys.ENTER)
time.sleep(2)

url = driver.current_url
# url = "https://www.youtube.com/results?search_query=KBO+%EB%A0%88%EC%A0%84%EB%93%9C"
print(url)
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response, 'lxml')
print(response)



# results = soup.find_all('h3')
# print(type(results))
# print(results[3:8])
# for result in results[3:8]:
#     print('링크' , result.attrs['href'])


results = soup.select('h3 > a')
# print(type(results))
result = results[3:8]
for video in result:
    # print(video)
    print(video.attrs['href'])
    
# results = driver.find_element_by_xpath('//*[@id="contents"]')
# print(results)


# print(soup.find_all('li'))
# print(soup.find_all('li'))









        

