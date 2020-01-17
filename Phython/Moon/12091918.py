from bs4 import BeautifulSoup

html = """<html> <head><title>Super Son</title></head>
<body> <p><a>test1</a><b>test2</b><c>test3</c></p> </body></html>""" 
#<c>도 태그로 되어있기 때문에 lxml은 인식 가능하지만 html5lip은 불가능(브라우저 인식 안되기 때문)
soup = BeautifulSoup(html, 'lxml')

tag_a = soup.a
tag_b = soup.b
tag_c = soup.c

print('tags')
print(tag_a)
print(tag_b)
print(tag_c)

tag_a_nexts = tag_a.next_siblings
tag_a_prevs = tag_c.previous_siblings

print(tag_a_nexts)
print(tag_a_prevs)

print('next sibilings')
for sibling in tag_a_nexts:
    print(sibling)

print('previous sibilings')
for sibling in tag_a_prevs:
    print(sibling)