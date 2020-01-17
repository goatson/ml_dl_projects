from bs4 import BeautifulSoup

html = """<html id ="g"> <head id="g"><title>Super Son</title></head>
<body id="f"> <p>test1</p><p id="d">test2</p><p>test3</p> </body></html>""" 
#<c>도 태그로 되어있기 때문에 lxml은 인식 가능하지만 html5lip은 불가능(브라우저 인식 안되기 때문)
soup = BeautifulSoup(html, 'lxml')

# print(soup.find_all(id = True))
# print(soup.body.find_all(id = False))   #왜 id 있어도 들고옴?
print(soup.body("p", id = False))