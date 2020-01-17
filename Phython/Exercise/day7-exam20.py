import requests
import json
import pandas as pd
from pandasql import sqldf  #conda install pandasql
pysqldf = lambda q : sqldf(q,globals())
from matplotlib import pyplot as plt

url="http://ihongss.com/json/exam20.json"  #서버주소
str1 = requests.get(url).text  # 문자열
dic = json.loads(str1)  #type변경  #[{},{},{},{},{}]


# {"code":,"name","cost"}
b = []
for i,t in enumerate(dic):
    a1 = t["cost"].split(",")  #"10000,200,3000" => ["10000","200","3000"]

    for i1, t1 in enumerate(a1):  #["10000","200","3000"] => [10000,200,3000]
        a1[i1] = int(t1)

    a1.insert(0, t["code"])
    a1.insert(1, t["name"])
    b.append(a1)  #[[14개][][][][][][][][][][]]
# print(b)


tot = [0,0,0,0,0,0,0,0,0,0,0,0]
for i,t in enumerate(b):
    # print(t[0])  #code
    # print(t[1])  #name
    # [1,2,3,4,5]
    # [6,7,8,9,10]
    # [7,9,11,13,15]
    # print(t)

    for j in range(2,14,1):
        # print(t[j])
        tot[j-2] = tot[j-2] + t[j]  # 1월부터 12월까지 출력
print(tot)       
"""
aa = list(range(1,13,1))  #[1,2,3,4,5,6,7,8,9,10,11,12]        
plt.plot(aa,tot)
plt.show()
""" 
##최대값 구하기
max = tot[0]
maxi = 0

for i3,t1 in enumerate(tot) :
    if max < t1 :
        max = t1
        maxi = i3
# print(max, maxi+1)        
print()



# ##최대값 구하기
# a = [3,56,7,89,23]
# max = a[0]
# maxi = 0
# for i,t in enumerate(a) :
#     if max < t :
#         max = t
#         maxi = i
# print(max, maxi)
# ###########


##순위구하기 (1~3위)

bbb=[1,1,1,1,1,1,1,1,1,1,1,1]
for i in range(0, 12, 1) :          # 0                   1               2             3            4 
    for j in range(0, 12, 1) :      #01234567891011 01234567891011 01234567891011 01234567891011
        print(tot[i])
        print()
        # print(tot[j])
        if tot[i] < tot[j] :
            bbb[i] = bbb[i]+1
print()
print(bbb)            



# # data에 2차 리스트가 있음
# df = pd.DataFrame(b, columns = ['code','name','a01', 'a02', 'a03', 'a04', 'a05', 'a06', 'a07', 'a08', 'a09', 'a10', 'a11', 'a12'])
# print(df[ ['code','name'] ])
# print()
# print(pysqldf("SELECT code, name, a01 FROM df WHERE a12 >= 10000"))

# # print(df.shape)
# # print(df['1'].describe())
# print()



# # a = "11000, 10000, 120000, 3000"
# # b = a.split(",") # ["111000", "1000", "120000"]

# # for i,t in enumerate(b):  #리스트의 문자값 숫자로 변경
# #     b[i] = int(t)
# # print(b)


# a=[]
# for i,t in enumerate(dic1):
#     # print(t)
#     a.append([ t['code'],t['name'],t['cost'] ])
# # print(a)
# print()


# # b = t['01'],t['02'],t['03'],t['04'],t['05'],t['06'],t['07'],t['08'],t['09'],t['10'],t['11'],t['12']


# for m,n in enumerate(a) :
#     # print(a[m][2])
#     # print()
#     l = a[m][2].split(",")
#     # print(l)
#     # print()

#     for x,y in enumerate(l) :
#         l[x] = int(y)
#     print(l)




    