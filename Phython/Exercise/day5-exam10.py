import requests
import json

url="http://ihongss.com/json/exam10.json"  #서버주소
str1 = requests.get(url).text  # 문자열
dic1 = json.loads(str1)  #type변경

print(dic1)  #딕셔너리 
print()

print(dic1["ret"])    
print()

print(dic1['data'])  #리스트 [{},{},{},{},{}]
print()

a = dic1['data']
for i in a :
    print(i)   #딕셔너리
print()      

for i in a :
    print("{},{},{}".format(i['id'],i['name'],i['age']))
print()

for i in a :
    print(i["score"])
print()    



for i in a :
    print("{}-{}-{}".format(i["score"]['math'],i["score"]['eng'],i["score"]['kor']))
print() 

for i in a :
    print(i["score"]["math"])
print()  


s = 0
c = 0

for i in a :
    c = c + 1
    s = s + i["score"]["math"]

print(s) #합계
print(s/c) #평균
print()

s = 0
c = 0
a = dic1['data']
b = a[0]["score"]["math"]  #숫자라서 for문 불가 / index 1개 뿐이라서 불가
for i in b :
    c = c + 1
    s = s + i

print(s) #합계
print(s/c) #평균

