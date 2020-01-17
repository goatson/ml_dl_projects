
#파이썬 비트 확인

import csv
import cx_Oracle as oci
import platform

#아이디/암호@서버주소:포트번호/SID
conn = oci.connect('admin/1234@192.168.99.100:32764/xe',encoding="utf-8")

cursor = conn.cursor()  # cursor 객체 얻기
cursor.execute('SELECT * FROM score')
data =  cursor.fetchall()  #[(),(),()]


# ID 입력하면 JAVA 점수 출력

data =  cursor.fetchone() # fetchone => (  ),  fetchall => [()]
if not data :
    print ("없음")    
else :
    print( data )



# print(platform.architecture())


# a = [1,2,3,4,5] #값 변경 가능 => 리스트
# b = {1,2,3,3,4} #값 변경 불가 => 튜플
# c = (2,2,3,4,5) #값 변경 불가 => 셋
# d = {'aaa':1, 'bbb':2, 'ccc':3} #값 변경 가능 => 딕셔너리

# for i in a :  #리스트
#     print(i, end=" ")
# print()

# for i in b :  #셋
#     print(i, end=" ")
# print()

# for i in c :  #튜플
#     print(i, end=" ")
# print()    

# for i,j in d.items() :  #셋
#     print("{}:{}".format(i,j), end=" ")
# print()    

# e = [['id1','가나다1','010-0000-0000', 25],
#     ['id2','가나다2','010-0000-0000', 35],
#     ['id3','가나다3','010-0000-0000', 45]]

# for i in e :
#     print(i)

n = input("ID")
c = 0

for tmp in data:
    if tmp[0] == n:
        print(tmp[3])
        c = 1
        break

if c == 0 :
    print("없음")

# java 60점 일때 ID 출력

n = input("")
