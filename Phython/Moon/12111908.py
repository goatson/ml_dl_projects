import urllib,csv
from bs4 import BeautifulSoup
import sqlite3

def moviesearch():
    params = urllib.parse.urlencode({'page':1})  #page 1 함수로 호출하게
    url = 'http://movie.naver.com/movie/point/af/list.nhn?&%s' %params
    #print(url)

    response = urllib.request.urlopen(url)
    navigator = BeautifulSoup(response,'html.parser')
    table = navigator.find('table', class_='list_netizen')
    # print(table)

    list_records=[]
    for i,r in enumerate(table.find_all('tr')):
        # print(i, r)
        for j,c in enumerate(r.find_all('td')):
            print(j, ':::', c)
            if j==0:
                record={c.text.strip()}
                
            elif j==1:
                record1 = str(c.find('em').text.strip())
                # print(record)
                record2 = str(c.find('a', class_='movie').text.strip())
                record3 = str(c.text).split('<br>')[0].split('\n')
        try:
            record_t=tuple([record, record1, record2, record3])#, record4, record5])
            list_records.append(record_t)
        except:
            pass
                
conn = sqlite3.connect('./example.db')            
with conn:
    c=conn.cursor()
    #있으면 만들지말고 없으면 만들어라   #column이름과 타입 함께 지정
    sql='CREATE TABLE if not exists movie (no integer, grade integer, title text, content text, writer text, date text)'
    c.execute(sql)
    conn.commit()
    sql='INSERT INTO movie VALUES (?, ?, ?, ? ?, ?)'
    c.executemany(sql, list_records)
    conn.commit()
    sql='select * from movie'
    c.excute(sql)
    rows=c.fetchall()
    
    for row in rows:
        print(row)