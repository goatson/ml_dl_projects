# 라이브러리 임포트
import requests
from bs4 import BeautifulSoup

# 네이버 메인 URL
url = "https://www.naver.com"

# url 접속 후 서버의 응답을 r 변수에 저장
r = requests.get(url)

# 뷰티풀숩 객체 생성 기본 html.parser 파서 사용
bs = BeautifulSoup(r.text, "html.parser")



# 1. copy selector 붙여 넣기 후 li 태그 추가
lists = bs.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li')
# print(lists)

# 2. 반복문 돌리기
for li in lists :
    title = li.find("span", attrs={"class": "ah_k"}).text
    print(title)


















# find_all 함수로 li 태그에 class 영어 ah_item 인 요소를 lists 변수에 저장
# for i in range(1,11,1):
# lists = bs.find_all("li", {"class":"ah_item"} )

# print(lists)

# lists 요소만큼 반복
# for li in lists:
#     # lists의 요소인 li 요소 하위에 span 태그에 클래스명이 ah_k 인 요소의 text값을 title에 저장
#     title = li.find("span", attrs={"class": "ah_k"}).text
#     print(title)


