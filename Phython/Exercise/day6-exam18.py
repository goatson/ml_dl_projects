import requests
import json
import re

url="http://ihongss.com/json/exam18.json"  #서버주소
str1 = requests.get(url).text  # 문자열
dic1 = json.loads(str1)  #type변경  #[{},{},{},{},{}]



[ "aaa", "bbb", "ccc" ]
[ ["aaa"], ["bbb"]]
[ ["1","aaa",32], ["2","bb",35] ]


# a = []
# for i,t in enumerate(dic1) :
#     a.append( [ t['id'],t['name'], t['email'], t['date'], t["time"], t["birth"] ] )
# print(a)
# print()

# for i,t in enumerate(a) :
#     #print(t[3])
#     #print()
#     b = re.match('[0-9]{4}-[0-9]{2}-[0-9]{2}$', t[3])
#     #print(b)
#     if( b == None) :
#         print("{} : {}".format(t[3], "날짜 형식 오류"))
#     else :
#         print("{} : {}".format(t[3], b.group()))

# print()




# a = []
# for i,t in enumerate(dic1) :
#     a.append(  t['email']   )  #[ "aaa", "bb"]   #[ ["fdf"],"[dfdfdf]"]
# print(a)    
# print()

# for i,t in enumerate(a) :
#     # print(t)
#     b = re.match('^[a-zA-Z0-9+-_.]+\@[a-z]+\.[a-z]+$', str(t))
#     # print(b)
#     if( b == None) :
#         print("{} : {}".format(t, "이메일 형식 오류"))
#     else :
#         print("{} : {}".format(t, b.group()))


a = []

for i,t in enumerate(dic1) : 
    a.append( [ t["id"],t["name"],t["email"],t["date"],t["time"],t['birth'] ] ) 
print(a)
print()


# for i,t in enumerate(a) :
#     print(t)
#     # print()
#     b = re.match(" ''str(^[a-z]$)'',  ''str(^[가-힣]+)',  ''str([a-zA-Z0-9+-_.]+\@[a-z]+\.[a-z]+$)'',  ''[0-9]{4}-[0-9]{2}-[0-9]{2}$'',  ''^[0-9]{2}:[0-5]{1}[0-9]{1}:[0-5]{1}[1-9]{1}'',  ''^[0-9]{2}/[0-9]{2}/[0-9]{4}'' ", t)
#     if( b == None) :
#         print("{} : {}".format(t, "아이디 형식 오류"))
#     else :
#         print("{} : {}".format(t, b.group()))    



    # for m,n in enumerate(t) :
    #     print(n)
    #     print()
    # b = re.match('^[a-z]$', t[0])
    # c = re.match('^[가-힣]+',t[1])
    # d = re.match('[a-zA-Z0-9+-_.]+\@[a-z]+\.[a-z]+$', t[2])
    # e = re.match('[0-9]{4}-[0-9]{2}-[0-9]{2}$',t[3])
    # f = re.match('^[0-9]{2}:[0-5]{1}[0-9]{1}:[0-5]{1}[1-9]{1}',t[4])
    # g = re.match('^[0-9]{2}/[0-9]{2}/[0-9]{4}',t[5])

    
    # if (b==None or c==None or d==None or e==None or f==None or g==None) :
    #     print("{} : {}".format(t[0],"오류"))
    # else :
    #     print("{} : {} {} {} {} {}".format(b.group(), c.group(), d.group(), e.group(), f.group(), g.group()))

import pandas as pd
df = pd.DataFrame(a, columns = ['id', 'name', 'email','date', "time", "birth"])
print(df)



"""
#id
# for i,t in enumerate(a) :
#     # print(t[3])
#     # print()
#     b = re.match('[a-z]$', t[0])
#     # print(b)
#     if( b == None) :
#         print("{} : {}".format(t[0], "아이디 형식 오류"))
#     else :
#         print("{} : {}".format(t[0], b.group()))

# print()
# print()
# #name
# for i,t in enumerate(a) :
#     # print(t[3])
#     # print()
#     c = re.match('[0-9]{4}-[0-9]{2}-[0-9]{2}$', t[1])
#     # print(b)
#     if( c == None) :
#         print("{} : {}".format(t[1], "이름 형식 오류"))
#     else :
#         print("{} : {}".format(t[1], c.group()))

# print()
# print()
# #email
# for i,t in enumerate(a) :
#     # print(t[3])
#     # print()
#     d = re.match('^[a-zA-Z0-9+-_.]+\@[a-z]+\.[a-z]+$', str(t[2])
#     # print(b)
#     if( d == None) :
#         print("{} : {}".format(t[2], "날짜 형식 오류"))
#     else :
#         print("{} : {}".format(t[2], d.group()))
# print()
# print()

# #date
# for i,t in enumerate(a) :
#     # print(t[3])
#     # print()
#     e = re.match('[0-9]{4}-[0-9]{2}-[0-9]{2}$', t[3])
#     # print(b)
#     if( e == None) :
#         print("{} : {}".format(t[3], "날짜 형식 오류"))
#     else :
#         print("{} : {}".format(t[3], e.group()))

# print()
# print()
# #time
# for i,t in enumerate(a) :
#     # print(t[4])
#     f = re.match('^[0-9]{2}:[0-9]{2}:[0-9]{2}',t[4] )
#     # print(b)
#     if( f == None) :
#         print("{} : {}".format(t[4],"시간 형식 오류"))
#     else :
#         print("{} : {}".format(t[4], f.group()))
"""