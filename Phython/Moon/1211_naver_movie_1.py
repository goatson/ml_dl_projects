import urllib, csv
from bs4 import BeautifulSoup
import json

params = urllib.parse.urlencode({'page':1})

url = "https://movie.naver.com/movie/point/af/list.nhn?&=%s" #%params

response = urllib.request.urlopen(url)
navigator = BeautifulSoup(response, 'html.parser')
table = navigator.find('table',class_='list_netizen')
#print(type(table))

list_records =[]

for i ,r in enumerate(table.find_all('tr')):  # 여러개의 tr을 가져오기
    print(i, r)
    for j,c in enumerate(r.find_all('td')):  # tr 밑에 여러개의 td 가져오기
        print(j, ':::', c)
        if j == 0:
            record = {'번호':int(c.text.strip())}
        elif j == 1:
            record.update({'평점':str(c.find('em').text)})
            record.update({'영화':str(c.find('a',class_='movie color_b').text.strip())})
            record.update({'140자평':str(c.text).split('<br>')[0].split('\n')[5]})
        elif j == 2:
            record.update({'글쓴이':str(c.find('a',class_='author').text.strip())})
            record.update({'날짜':str(c.text).split('****')[1]})   
    try:
        list_records.append(record)
        # writer.writerow(record)
    except:
        pass    
 
with open('./movie.json','wt') as f:
    json.dump(list_records,f)    
