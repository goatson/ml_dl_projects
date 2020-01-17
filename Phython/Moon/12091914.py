from bs4 import BeautifulSoup

html = """<html> <head><title>Super Son</title></head>
<body> <p><span>test1</span><span>test2</span></p> <p>ballon dor</p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')

tag_p_chidren = soup.p.contents

print(tag_p_chidren)