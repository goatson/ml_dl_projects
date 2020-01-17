import requests
from bs4 import BeautifulSoup

# 야구 선수기록 URL
url = "https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx"

# url 접속 후 서버의 응답을 r 변수에 저장
r = requests.get(url)

# 뷰티풀숩 객체 생성 기본 html.parser 파서 사용
bs = BeautifulSoup(r.text, "html.parser")

# find_all 함수로 li 태그에 class 영어 ah_item인 요소를 lists 변수에 저장
lists = bs.find_all("tbody")

# print(lists)




# lists 요소만큼 반복
for li in lists:
    # lists의 요소인 li(tr) 요소 하위에 td 태그인 요소의 text값을 player에 저장
    player = li.find_all
    print(player)
    
