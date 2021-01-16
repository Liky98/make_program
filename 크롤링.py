from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

base = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plus = input('검색 : ')
url = base + quote_plus(plus)

driver = webdriver.Chrome() # 크롬사용
driver.get(url)

html= driver.page_source #페이지 소스가져옴
soup = BeautifulSoup(html, 'html.parser')#페이지 분석

r= soup.select('.thumb')
print(r[0])