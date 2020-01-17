import re
import pickle
"""
a = [1,2,3,4]
#a의 리스트를 파일로 저장 하기
f= open("c:/data/pickle.pkl", "wb")  # wb
pickle.dump(a, f)   # 객체로 저장 dump
f.close()

# 파일에서 list타입 읽기
f1 = open("c:/data/pickle.pkl", "rb")
b = pickle.load(f1)  #읽을 때 load
print(type(b))
print(b)
f1.close()
"""


# str = "1234abc"
# a = re.match('[0-9]*', str)  ###dump 시험문제  직렬어를 바탕으로 모델을 저장#
# print(a.span())
# print(a.group())
# print()

# str1 = "'010-0000-0000'"
# print(str1)
# b = re.match("'[0-9]{3}-[0-9]{4}-[0-9]{4}'", str1)
# #b = re.match(r'\d{3}-\d{4}-\d{4}$', str1)
# print(b)
# if( b == None) :
#     print("휴대폰 번호 형식 오류")
# else :
#     print(b.group())
# print() 


# 이메일 [a-z]+  => a~z까지 1자 이상
# abc12__@naver.com  \.
# ^[a~zA-Z0-9+-_.]+   @  [     ]  \. [    ]$          => [a~z A~Z 0~9 + - _ .]

str = ["010"]
print(str)
b = re.match("[0-9]{3}",str)
if(b == None) :
    print("오류")
else :
    print(b.group())    
