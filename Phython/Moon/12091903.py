import bs4

html = """<p>test</p>"""

soup = bs4.BeautifulSoup(html, 'lxml')  # lxml : 태그형태로 정리하는 방법 -> 없는 부분 알아서 넣어준다. (body 등 넣어준다.)
print(soup)