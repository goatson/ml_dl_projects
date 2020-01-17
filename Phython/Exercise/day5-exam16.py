import requests
import json

url="http://ihongss.com/json/exam16.json"  #서버주소
str1 = requests.get(url).text  # 문자열
dic1 = json.loads(str1)  #type변경

# print(type(dic1))
# print(dic1) # boxOfficeResult
# print()

# print(boxOfficeResult)
# for i in dic1 :
    #print(i)


print()    
a = dic1['boxOfficeResult']
print(a)
print()

for i in dic1 :
    print(a['boxofficeType'])
print()

for i in dic1 :
    print(a["dailyBoxOfficeList"])
print()

for i in dic1 :
    print(a["dailyBoxOfficeList"][0])
print()    

for i in dic1 :
    print(a["dailyBoxOfficeList"][1])
print()

for i in dic1 :
    print(a["dailyBoxOfficeList"][9])
print()   

for i in dic1 :
    print(a["dailyBoxOfficeList"][9]['movieNm'])
print()   