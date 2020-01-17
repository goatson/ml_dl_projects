# 라이브러리 임포트
import requests
from bs4 import BeautifulSoup

# 네이버 메인 URL
url = "https://www.naver.com"

# url 접속 후 서버의 응답을 r 변수에 저장
r = requests.get(url)
bs = BeautifulSoup(r.text, 'html.parser')
#뷰티풀숩의 select 함수 사용
# li 태그의 클래스명이 ah_item 인 요소 하위의 span 태그이며 클래스명이 ah_k인 요소 선택
lists = bs.select("li.ah_item > span.ah_k")
for li in lists:
    print(li.text)


#

















# find_all 함수로 li 태그에 class 영어 ah_item 인 요소를 lists 변수에 저장
# for i in range(1,11,1):
# lists = bs.find_all("li", {"class":"ah_item"} )

print(lists)

# lists 요소만큼 반복
for li in lists:
    # lists의 요소인 li 요소 하위에 span 태그에 클래스명이 ah_k 인 요소의 text값을 title에 저장
    title = li.find("span", attrs={"class": "ah_k"}).text
    print(title)


