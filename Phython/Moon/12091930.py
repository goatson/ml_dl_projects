from bs4 import BeautifulSoup

html = """<html> <head><title>Super Son</title></head>
<body> <p id="i" class="a">test1</p>
<p class="d">test2</p><p class="d">test3</p>
<a>a tag</a> <b>b tag</b></body></html>""" 
#<c>도 태그로 되어있기 때문에 lxml은 인식 가능하지만 html5lip은 불가능(브라우저 인식 안되기 때문)
soup = BeautifulSoup(html, 'lxml')

a = soup.body.extract()

print('제거 항목')
print(a)
print('제거 완료')
print(soup)
