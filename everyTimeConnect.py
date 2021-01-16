from selenium import webdriver
from selenium.webdriver.common.keys import Keys

usr = "test"
pwd = "TT"

driver = webdriver.Chrome()
driver.get("https://everytime.kr/login")
#assert "EveryTime" in driver.title
elem = driver.find_element_by_name("userid")
elem.send_keys(usr)
elem = driver.find_element_by_name("password")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)