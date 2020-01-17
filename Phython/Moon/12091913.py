from bs4 import BeautifulSoup

html = """<html> <head><title>Super Son</title></head> <body> <p>test</p> <p>test1</p> <p>ballon dor</p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')
tag_title = soup.title

data_text = tag_title.text    # data만 
data_string = tag_title.string  # element의 load 객체  상위/하위가 살아있다.  meta정보가 많고 memory 잡아먹는다.


print('text : ', data_text, type(data_text))
print('string : ', data_string, type(data_string))