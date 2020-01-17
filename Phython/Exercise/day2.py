"""
a=1
b=2
c=3
d = [1,2,3,4,5,6,7,8]
#    0 1 2 3 4 5 6 7
#   -8-7-6-5-4-3-2-1

print( type(d) )
print( d )
print( d[2] )  #인덱스가 0부터 시작함.
print( d[0:4] ) #0부터 4까지
print( d[:-4])  #처음부터 -4

for i in d:  #for i in range(1,10,1):
    print(i, end=" ")

d = int(input("숫자입력"))
"""
"""
for i in range(1,d+1,1) :
    if i%3 == 0 :
        print(i)
""""""
for i in d :
    if i%3==0:
        print(i, end="")        
        """


# next(rdr, None) 첫번째 라인을 skip
#print( type(rdr))
"""
for i in rdr:
    i[2]
    print(i[0])

for i in range(1,11,1)    :
    if a%3==0:
        c=c+1

print(c)     
"""

"""
c=0
d=0
c_name = [] #빈 리스트 생성
d_name = [] #빈 리스트 생성

for i in rdr:
    if i[2] == "male":
        c=c+1
        c_name.append(i[0])
    elif i[2] == "female":
        d=d+1
        d_name.append(i[0])

print("{}:{}".format(c,d))
print(c_name)
print(d_name)
"""
"""
d=["1","2","3","4.0","5"]
s=0
for i in d:
    s=s+float(i)
print(s)
print(s//len(d))
"""

#리스트 값 합 구하기

import csv
f = open('c:/data/exam1.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
next(rdr, None) #첫번째 라인을 skip
"""
s=0
for i in rdr :
    s = s + str((count(i[2]))
    for i in rdr :
        s = s + float(i[3])
        for i in rdr :
            s = s + float(i[4])
            for i in rdr :
                s = s + float(i[5])

print(s) #time의 합 출력
"""
"""
s=0
c=0
for i in rdr:
    c=c+1
    s = s + float(i[3]) + float(i[4]) + float(i[5])

print(s) #합
print(s/c) #평균
"""
"""
for i in range(1,3,1):  #1부터 2까지 1씩 증가
    print(i)
    for j in range(1,4,1): #1부터 3까지 1씩 증가
        print("{} - {}".format(i,j))
"""
"""
1 *
2 **
3 ***
""""""
for i in range(1,4,1) :
    for j in range(1, i+1, 1) :
        print("*",end="")
    print(end="\n")    

 *****
 ****
 ***
 **
 *
 """
"""
for i in range(5,0,-1) : #5부터 1까지 1씩 감소
    for j in range(1,i+1,1) : # 1부터 5까지 1씩 증가
        print("*", end="")  
    print(end="\n")

for i in range(1,6,-1) :
    for j in range(1,6-i,1) :
        print("*", end="")
    print(end="\n")
     """ 
 
"""
for i in range(1,6,1) :
    for j in range(1,i*2,1) :
        print("*", end="")
    for k in range(3,i-2,1) :
        print("*", end="")
    
    
    print(end="\n")
"""

"""
1 *
2 ***
3 *****    
1 ***
2*
***
"""
"""
for i in range(1,4,1) : # 1 2 3
    for j in range(1,2*i,1) : # 1 123 12345
        print("*",end="")
    print()

for i in range(1, 3, 1) : # 1 2
    for j in range(1, 6-2*i, 1) : #123 1
        print("*", end="")
    print()
"""

a = 156,780 #원 => 50000:3 10000:0 ...
b = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
"""
+
*
// 나머지
/ 나누기
%
"""
"""
for i in b :
    n = a // i  #156780/50000 = 3
    a = a - (n*i)  #6780
    print("{} - {}".format(i, n))
    """
"""
a = [3, 5, 289, 2, 34, 134]
max = a[0]
min = a[0]

for i in a:
    if max < i :
        max = i
    
    if min > i :
        min = i

print("최대값은={}".format(max))
print("최대값은={}".format(min))
"""


"""
#합계/평균
s=0
a=0

for i in rdr :
    a=a+1
    s=s+float(i[3])
print(s)    #합
print(s/a)  #평균
"""

#나이의 최대 최소 합계 평균
import csv
f = open('c:/data/exam1.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
next(rdr, None) #첫번째 라인을 skip

#최대/최소

max = 0
min = 999
for i in rdr :
    print(i[3])
    
    if max < int(i[3]):
        max = int(i[3])


    if min > int(i[3]) :
        min = int(i[3])

print("최대값은={}".format(max)) 
print("최소값은={}".format(min))

