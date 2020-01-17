import sqlite3
import urllib, csv
from bs4 import BeautifulSoup


list_records =[]
while True:
    pages=1
    params = urllib.parse.urlencode({'page':pages})

    url = f"https://movie.naver.com/movie/point/af/list.nhn?&={params}" #%params
    pages +=1
    response = urllib.request.urlopen(url)
    navigator = BeautifulSoup(response, 'html.parser')
    table = navigator.find('table',class_='list_netizen')

    if pages ==3:
        break
    else:    
        for i,r in enumerate(table.find_all('tr')):  # 여러개의 tr을 가져오기
            #print(i, r)
            for j,c in enumerate(r.find_all('td')):  # tr 밑에 여러개의 td 가져오기
                print(j, ':::', c)
                if j == 0:
                    record = int(c.text.strip())
                elif j == 1:
                    record1 = str(c.find('em').text)
                    record2 = str(c.find('a',class_='movie color_b').text.strip())
                    record3 = str(c.text).split('<br>')[0].split('\n')[5]
                elif j == 2:
                    record4 = str(c.find('a',class_='author').text.strip())
                    record5 = str(c.text).split('****')[1]
            try:
                record_t = tuple([record,record1,record2,record3,record4,record5])
                list_records.append(record_t)
                #print(list_records)
            except:
                pass    
    
conn=sqlite3.connect('./example.db')
with conn:
    c=conn.cursor()

    sql='CREATE TABLE if not exists movie(no integer, grade integer, title text, content text, writer text, date text)'
    c.execute(sql)
    conn.commit()

    sql='INSERT INTO movie VALUES (?,?,?,?,?,?)'
    c.executemany(sql, list_records)
    conn.commit()

    sql='select * from movie'
    c.execute(sql)

    rows=c.fetchall()
    for row in rows:
        print(row)
