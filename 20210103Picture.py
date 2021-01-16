#Chrome 켠 후, 이미지 가져옴
 
from selenium import webdriver
 
path = "C:/chromedriver/chromedriver.exe"    #웹드라이버가 있는 경로
 
driver = webdriver.Chrome(path)        #웹드라이버가 있는 경로에서 Chrome을 가져와 실행-> driver변수
 
driver.get('https://www.hiphoper.com/clothing/list?_ct=tshirts')     #driver변수를 이용해 원하는 url 접속
 
imgs = driver.find_elements_by_css_selector('img.pos_center')       #css selector를 이용해서 'tag이름.class명'의 순으로 인자를 전달
result = []     #웹 태그에서 attribute 중 src만 담을 리스트
 
for img in imgs:                                #모든 이미지들을 탐색
    #print(img.get_attribute('src'))         #이미지 주소를 print
    result.append(img.get_attribute('src'))     #이미지 src만 모아서 리스트에 저장
 
 
#폴더생성
import os
 
img_folder_path = 'C:/Users/ASUS S510UN/Desktop/Projects/bottom-up/imgs'    #이미지 저장 폴더
 
if not os.path.isdir(img_folder_path):      #없으면 새로 생성
    os.mkdir(img_folder_path)
 
 
 
#이미지 다운로드
from urllib.request import urlretrieve
 
for index, link in enumerate(result):           #리스트에 있는 원소만큼 반복, 인덱스는 index에, 원소들은 link를 통해 접근 가능
    start = link.rfind('.')         #.을 시작으로
    end = link.rfind('?')           #?를 끝으로
    filetype = link[start:end]      #확장자명을 잘라서 filetype변수에 저장 (ex -> .jpg)
    urlretrieve(link, './imgs/{}{}'.format(index, filetype))        #link에서 이미지 다운로드, './imgs/'에 파일명은 index와 확장자명으로
