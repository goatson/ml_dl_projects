import requests
import json

url="http://ihongss.com/json/exam2.json"  #서버주소
str1 = requests.get(url).text  # 문자열
dic1 = json.loads(str1)  #type변경

#id불러오기

print(dic1["ret1"]["id"])

id=[]
name=[]
for key in dic1 :
    print(dic1[key]["id"])
    name.append(dic1[key]["id"])
print(name)    


