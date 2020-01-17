import time
import requests
from bs4 import BeautifulSoup

def time_function(f):
    '''함수 사용 시간을 측정하기 위한 데코레이터
    Args
        f (function) : 함수
    Return
        function : 함수 포인터 
    '''
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        end_time = time.time() - start_time
        print("{} {} time: {}".format(f.__name__, args[1], end_time))
        return result
    return wrapper
    #시간 재는 함수

# 접속 URL (네이버)
url = "https://www.naver.com"


@time_function
def r_selector(url, parser):
    r = requests.get(url)
    bs = BeautifulSoup(r.text, parser)
    # 뷰티풀숩의 select 함수 사용
    # li 태그의 클래스명이 ah_item 인 요소 하위의 span 태그이며 클래스명이 ah_k 인 요소 선택
    lists = bs.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li")
    for li in lists :
        print(li.text)



r_selector("http://www.naver.com", "html5lib")
r_selector("http://www.naver.com", "html.parser")
r_selector(url, "lxml")



