from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

baseURL = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query='
inputURL = input('어떤 것을 다운로드 할까요? : ')

mixURL = baseURL + quote_plus(inputURL) #한글로쓴거 아스키코드로 자동 변환
html = urlopen(mixURL).read()#url링크 가져와서 읽음
soup = BeautifulSoup(html, 'html.parser') #웹페이지분석
bsSoup = soup.find_all(class_ = 'photo')
print(bsSoup)

# n = 1
# for i in bsSoup:
#     with urlopen() as uo:
#         with open(inputURL + str(n) + '.jpg', 'wb') as op:
#             image = uo.read()
#             op.write(image)
#     n +=1     

# print('다운로드 완료')
