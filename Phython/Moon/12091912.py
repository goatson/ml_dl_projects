from bs4 import BeautifulSoup

html = """<html> <head><title class="t" id="ti"> Super Son</title></head> <body> <p>test</p> <p>test1</p> <p>ballon dor</p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')
tag_title = soup.title

print(tag_title.attrs)
print(tag_title.get('class'))
print(tag_title.get('id'))
print(tag_title.get('class1'))
print(tag_title.get('class1', 'default_value'))   # error 안나게 하려면 get방식   /  error 나게 하려면  딕셔너리 직접 접근

