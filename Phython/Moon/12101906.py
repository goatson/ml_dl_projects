from selenium import webdriver                      # logic 상에서 자동화
from selenium.webdriver.common.keys import Keys

usr = "아이디"
pwd = "패스워드"

path = "./chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get("http://www.facebook.org")
assert "Facebook" in driver.title
# elem = driver.find_element_by_id("email")  #로그인 할 때 아이디
# elem.send_keys(usr) 
# elem = driver.find_element_by_id("pass")
# elem.send_keys(pwd)
# elem.send_keys(Keys.RETURN)  # submit과 같은 효과

# pip install selenium