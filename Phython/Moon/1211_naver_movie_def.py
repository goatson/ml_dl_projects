import urllib, csv
from bs4 import BeautifulSoup

def getNavermovie():
    params = urllib.parse.urlencode({'page':1})

    url = f"https://movie.naver.com/movie/point/af/list.nhn?&={params}" #%params

    response = urllib.request.urlopen(url)
    navigator = BeautifulSoup(response, 'html.parser')
    table = navigator.find('table',class_='list_netizen')
    #print(table)

    list_records =[]
    with open('./navermovie_1.csv','w',newline='',encoding='UTF-8') as csvfile:
        fieldnames = ['번호','평점','영화','140자평','글쓴이','날짜']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='|')
        writer.writeheader()
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
        writer.writerows(list_records) 
if __name__ =="__main__":
    getNavermovie