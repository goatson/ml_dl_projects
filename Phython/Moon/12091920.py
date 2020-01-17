from bs4 import BeautifulSoup

html = """<html> <head><title>Super Son</title></head>
<body> <p><a>ttt<span>123</span><span>123</span></a><b>test2</b><c>test3</c></p> </body></html>""" 
#<c>도 태그로 되어있기 때문에 lxml은 인식 가능하지만 html5lip은 불가능(브라우저 인식 안되기 때문)
soup = BeautifulSoup(html, 'lxml')

print(soup.find_all('title'))  #find, find_all : html5에서 가장 많이 쓴다. 
print(soup.find_all('p'))

