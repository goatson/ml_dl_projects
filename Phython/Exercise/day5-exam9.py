import requests
import json

url="http://ihongss.com/json/exam9.json"  #서버주소
str1 = requests.get(url).text  # 문자열
dic1 = json.loads(str1)  #type변경

print(dic1) #{"ret":"y", "data""[{},{},{},{},{}]"}
print()

print(dic1["ret"])
print()

a = dic1["data"] #[{},{},{},{},{}]

for i in a :
    print("{},{},{}".format(i['id'], i['name'], i['age']))
print()    


