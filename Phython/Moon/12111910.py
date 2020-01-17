import urllib,csv, json
from bs4 import BeautifulSoup

params = urllib.parse.urlencode({'page':1})  #page 1 함수로 호출하게
url = 'http://movie.naver.com/movie/point/af/list.nhn?&%s' %params
#print(url)

response = urllib.request.urlopen(url)
navigator = BeautifulSoup(response,'html.parser')
table = navigator.find('table', class_='list_netizen')
# print(table)

list_records=[]

# with open('navermovie.csv', 'w', newline="", encoding='UTF-8') as csvfile:
#     fieldnames = ['번호', '평점', '영화', '140자평', '글쓴이', '날짜']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='|')
#     writer.writeheader()


for i,r in enumerate(table.find_all('tr')):
    # print(i, r)
    for j,c in enumerate(r.find_all('td')):
        print(j, ':::', c)
        if j==0:
            record={'번호':int(c.text.strip())}
            print(record)
        elif j==1:
            record.update( { '평점':str(c.find('em').text) } )
            # print(record)
            record.update( { '영화': str(c.find('a').text) } )
            print(record)
            # record.update( { '140자평': })

#             elif j==3:
#                 record.update({'영화':str()})
    try:
        list_records.append(record)
    except:
        pass
# print(list_records)

with open('C:/Users/admin/Documents/Phython/Crawling/movie.json','wt') as f:
    json.dump(list_records,f)
    