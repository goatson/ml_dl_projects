import pandas as pd
import requests
import json

url="http://ihongss.com/json/exam17.json"  #서버주소
str1 = requests.get(url).text  # 문자열
dic1 = json.loads(str1)  #type변경  #[{},{},{},{},{}]

a = dic1
b = []

"""
print(a)
print()

for i in a :
    print(i)
print()

for i in a :
    b.append( [ i['no'], i['title'], i['content'], i['date'], i['hit'] ])
print(b)
"""
"""
a = []
for i, t in enumerate(dic1) :
    print(i, t)
    a.append( [ int(t['no']),t['title'],t['content'],t['date'],int(t['hit']) ] )
print(a)
print()
"""

# a1 = "aaa bbb ccc ddd"
# a2 = a1.split()  #문자열을 공백으로 나누고 리스트로 변환
# print(a2)
# print()

#내용부분에 aaa가 몇개인지 파악
"""
for i, t in enumerate(a) :
    # print(i,t[2])  # aaa bbb ccc ddd eee
    print(t[2].split())
    a2 = t[2].split()

    s = 0    
    for v in t[2].split() :  #['aaa','bbb','ccc','ddd','eee'] <= 5개
        if 'aaa' == v :
            s = s + 1
    print(s)        
print()
"""
"""
# hello 갯수 세기
cnt = 0
cnt1 = 0
aaa = 0
for i, t in enumerate(a):
    print(t[2])
    a2 = t[2].split()
     
    for i1 in a2:
        if i1.upper() == "HELLO" :
            cnt = cnt +1
        
        if i1.isdigit() == True: #숫자로 구성된 것이면 True
            cnt1 = cnt1 + 1

        
print(cnt)
print(cnt1)
print()
print()
"""
wc = dict()  #빈 딕셔너리 생성
words = ["aaa", "bbb", "ccc", "aaa"]
# 딕셔너리 get(key값, 없을경우 리턴할 값)
# for word in words :
#     wc[word] = wc.get(word,0) + 1  # 단어 카운트 증가


a = []

for i, t in enumerate(dic1) :
    a.append( t["content"]  )
print(a)   
print()    

for m,n in enumerate(a) :
    #print(n)
    print(n.split())
    
    a2 = n.split()
    for word in a2 :
        wc[word] = wc.get(word,0) +1

print(wc)




# for m,n in enumerate(a) :
#     a2 = n.split()
#     #print(a2) 
#     for v in a2 :
#         print(v)
#         print()    
#         wc[word] = wc.get(word,0) + 1  # 단어 카운트 증가
# print() 

# print(wc)


#  for m,n in enumerate(t["content"]) :
#         print(n)

# print(a[0]['content'])





"""
print()
a1 = "12a"
print(a1.isdigit())  #문자열 내용이 숫자로만 되어 있느냐?

a2 = "HeLlo"
print(a2.lower())  #a2 내용을 소문자로 변경
"""





"""
print((a)[0][2])
print()
print(dic1[0]["content"])
print()
"""