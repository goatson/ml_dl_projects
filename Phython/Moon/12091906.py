import time
from bs4 import BeautifulSoup

html = """<html><head></head><p>test<p></html>"""

start_time = time.time()
BeautifulSoup(html, 'lxml')       # logic을 많이 알아야 사용가능 빠르지만 불편함
lxml_end_time = time.time() - start_time

start_time = time.time()
BeautifulSoup(html, 'html5lib')   # 브라우저 기반에서 사용가능  느리지만 편함
html5lib_end_time = time.time() - start_time

print('lxml 시간측정 : %f' %(lxml_end_time))
print('html5lib 시간측정 : %f' %(html5lib_end_time))
print(html5lib_end_time / lxml_end_time)


# 라이브러리로 html을 tag형태로 만들어주는 시간
# 어떤 파서 쓸지?  양쪽에서 다 되는지 - > 빠른 것 선택
