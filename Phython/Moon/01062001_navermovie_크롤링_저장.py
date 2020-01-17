import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
    

with open('c:/python_workplace/Crawling/review.csv', 'w', newline='', encoding='utf-8') as f :
    writer = csv.writer(f)
    writer.writerow(["리뷰", "평점"]) 

    for i in range(1,100,1) :
        url = 'https://movie.naver.com/movie/point/af/list.nhn?&page=' + str(i)

        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'lxml')
        result = soup.find('tbody')
        # print(result)
        list = result.find_all('tr')
        # print(list)

        for li in list:
            # print(li)
            comment = li.find('a',{'class':'report'})
            try : 
                review = comment.attrs['href'].split(',')[2].replace("'","")
                # print(review)
            except :
                pass
            score = li.select('em')[0].text
            print("리뷰:{}, 평점:{}".format(review,score))
            writer.writerow([review, score])


			
