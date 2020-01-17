from selenium import webdriver
import requests, time
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver.exe')
starbugs = driver.get('https://www.istarbucks.co.kr/store/store_map.do')
time.sleep(1)

loca = driver.find_element_by_class_name('loca_search')
loca.click()
time.sleep(1)

sido = driver.find_element_by_class_name('sido_arae_box')
li = sido.find_elements_by_tag_name('li')
li[5].click()
time.sleep(1)

gugun = driver.find_element_by_class_name('gugun_arae_box')
li = gugun.find_elements_by_tag_name('li')
li[-1].click()
time.sleep(1)

source = driver.page_source
bs = BeautifulSoup(source, 'lxml')

entire = bs.find('ul',class_='quickSearchResultBoxSidoGugun')

li_list = entire.find_all('li')
for li in li_list:
    print(li.find('p').text)

driver.close()