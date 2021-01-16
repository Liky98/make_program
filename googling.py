from urllib.parse import quote_plus 
from bs4 import BeautifulSoup
from bs4.element import SoupStrainer
from selenium import webdriver

baseUrl = 'https://www.google.com/search?q='
inputUrl = input('입력하세요')
url = baseUrl + quote_plus(inputUrl) #quote_plus를 해줘야 웹이 인식하는 언어로 바꿔줌.

driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html)

a = soup.select('Uo8X3b')
print(soup.select_one('span'))