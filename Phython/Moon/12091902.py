from urllib.request import urlopen, Request

url = "http://blog.naver.com/pjt3591oo"

req = Request(url)
page = urlopen(req)

print(page)             # 응답객체
print(page.code)        # 응답코드  
print(page.headers)     # 헤더확인
print(page.url)         # 요청 url 확인
print(page.info().get_content_charset()) # 인코딩 설정 확인
print(page.read())      # HTML 코드 가져오기

page.close