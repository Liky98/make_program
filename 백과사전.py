import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import os

baseURL = 'https://dict.naver.com/search.nhn?dicQuery='


while True :
    inputURL = input('검색할 단어 : ')
    if inputURL == '그만' : break
    mixURL = baseURL + urllib.parse.quote_plus(inputURL) #한글로쓴거 아스키코드로 자동 변환

    html = urllib.request.urlopen(mixURL).read()#url링크 가져와서 읽음
    soup = BeautifulSoup(html, 'html.parser') #크롤링하려면 이거해줘야함

 
    bsSoup = soup.find("dd")
    print(bsSoup.text)

os.system('pause')