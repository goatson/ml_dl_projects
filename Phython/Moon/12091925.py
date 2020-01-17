from bs4 import BeautifulSoup

html = """<html> <head><title>Super Son</title></head>
<body> <p>test1</p><p class="d">test2</p><p class="c">test3</p> </body></html>""" 
#<c>도 태그로 되어있기 때문에 lxml은 인식 가능하지만 html5lip은 불가능(브라우저 인식 안되기 때문)
soup = BeautifulSoup(html, 'lxml')

print(soup.find_all('p', limit=1))   # css 셀렉터 이용 / 3가지 있음
print(soup.find_all('p', limit=2)) 
print(soup.find_all('p', limit=3))
print(soup.find_all('p', limit=4))
