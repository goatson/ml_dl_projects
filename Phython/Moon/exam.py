import requests as rq

url = "http://blog.naver.com/pjt3591oo"

res = rq.get(url)  # 해당 url로 GET 요청
res = rq.post(url)  # 해당 url로 POST 요청

print(res)               # 응답 객체
print(res.status_code)   # 응답코드 확인
print(res.headers)       # 헤더 가져오기
print(res.cookies)       # 쿠키 가져오기
print(res.text)          # HTML 코드 가져오기
print(res.content)       # 바이너리 형태로 변환된 HTML 코드 가져오기
print(res.encoding)      # 페이지 인코딩 확인