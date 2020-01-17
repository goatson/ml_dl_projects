from bs4 import BeautifulSoup

html = """<html> <head><title>Super Son</title></head>
<body> <p id="i" class="a">test1</p>
<p class="d">test2</p><p class="d">test3</p>
<a>a tag</a> <b>b tag</b></body></html>""" 
#<c>도 태그로 되어있기 때문에 lxml은 인식 가능하지만 html5lip은 불가능(브라우저 인식 안되기 때문)
soup = BeautifulSoup(html, 'lxml')

print(soup.select('p'))   # 태그  #css와 똑같은 표기법으로 가능
print(soup.select('.d'))   # 클래스
print(soup.select('p.d'))   #  #은 아이디
print(soup.select('#i'))
print(soup.select('p#i'))

