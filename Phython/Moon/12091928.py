from bs4 import BeautifulSoup

html = """<html> <head><title>Super Son</title></head>
<body> <p>test1</p><p class="d">test2</p><p class="c">test3</p>
<a>a tag</a> <b>b tag</b></body></html>""" 
#<c>도 태그로 되어있기 때문에 lxml은 인식 가능하지만 html5lip은 불가능(브라우저 인식 안되기 때문)
soup = BeautifulSoup(html, 'lxml')

print(soup.find('p'))    #처음 하나만 가지고 온다. 밑에보다 효율적
print(soup.find_all('p', limit=1)[0])
print(soup.find_all('p', limit=3)[2])
# print(soup.find_all('p', limit=1)[1])  #왜 오류?
