from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver.exe')
driver.get('https://ko.wikipedia.org/wiki/%EC%9C%84%ED%82%A4%EB%B0%B1%EA%B3%BC')
google = driver.find_element_by_xpath('//*[@id="searchInput"]')
google.send_keys('구글')
google.send_keys(Keys.ENTER)
print(driver.find_element_by_xpath('//*[@id="bodyContent"]').text)