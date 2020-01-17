from bs4 import BeautifulSoup

html = """<html> <head><title>Super Son</title></head>
<body> <p><a>ttt<span>123</span><span>123</span></a><b>test2</b><c>test3</c></p> </body></html>""" 
#<c>도 태그로 되어있기 때문에 lxml은 인식 가능하지만 html5lip은 불가능(브라우저 인식 안되기 때문)
soup = BeautifulSoup(html, 'lxml')

tag_p_nexts = soup.p.next_elements   #child까지 다 인식

print(soup.prettify())
print('**elements**')

for i in tag_p_nexts:
    print(i)
    