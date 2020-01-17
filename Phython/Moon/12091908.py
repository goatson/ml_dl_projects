from bs4 import BeautifulSoup

html = """<html> <head><title>Super Son</title></head> <body>
<p>test</p> <p>test1</p> <p>ballon dor</p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())