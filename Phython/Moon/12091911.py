from bs4 import BeautifulSoup

html = """<html> <head><title class="t" id="ti"> Super Son</title></head> <body> <p>test</p> <p>test1</p> <p>ballon dor</p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')
tag_title = soup.title

print(tag_title.attrs)
print(tag_title['class'])
print(tag_title['id'])
