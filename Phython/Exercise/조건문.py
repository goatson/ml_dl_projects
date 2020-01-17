
#문제 국어 영어 수학 점수를 입력받아서 평균이
# 90이상이면 A
# 80이상이면 B
# 70이상이면 C
# 나머지는 D

"""
a,b,c = map(int, input("숫자를 3개 입력하세요.").split(","))  # 45,67,89
AVG = ((a + b + c) / 3)

if AVG >= 90 :
    print("A")
elif AVG >= 80 :
    print("B")    
elif AVG>= 70 :
    print("C")    
else :
    print("D")   
"""

"""
a = int(input("숫자를 입력하세요"))
if a%5 == 0 :  # == 같냐?  != 다르냐
    print("5의 배수입니다.")
else:
    print("5의 배수가 아닙니다.")    
"""

"""
x = int(input("숫자를 입력하세요."))
if 11 <= x <= 20 :
    print("11~20")
elif 21 <= x <= 30 :
    print("21~30")
else :    
    print("아무것도 해당하지 않음")



age = int(input("나이"))
a = int(9000)  # 잔액

if 7<= age <=12 :
    print(a-650)
if 13<= age <=18 :
    print(a-1050)
if age > 19 :
    print(a-1250)
    

print(balance)

#반복문
for i in range(0, 10, 2) : #range(0, 10, 1) 시작숫자, 조건(9까지), 증가값
    print("hello world"+str(i))

for i in range(10, 0, -2) : #
    print(i)    

# 문제 숫자 2개를 입력받아서 그 사이의 숫자를 출력하시오.
# ex) 1 5 => 1 2 3 4 5
# ex) 5 1 => 1 2 3 4 5


for i in range(100) :
    print('hello world')

for i in range(100) :
    print('hello, world!', i)
    """
"""
for i in range(5, 12) : #5부터 11까지 반복
    print('hello world', i)
"""

#문제 숫자 2개를 입력받아서 그 사이의 숫자를 출력하시오.
# ex) 1 5 => 1 2 3 4 5
# ex) 5 1 => 5 4 3 2 1
"""
a=1
b=5

if a < b :
    for i in range(a, b+1, 1) :
        print(i, end=" ")
else :
    for i in range(b, a+1, 1):
        print(i, end=" ")
    """
"""
a=3
b=4
print("{0}+{1}={2}").format(a,b,(a+b))  #3+4=7



i = int(input("구구단"))2
for v in range(1, 10, 1) :
    print("{0} * {1} = {2}".format(i, v, (i*v)))

a = int(input("구구단"))
for b in range(1, 10, 1):
    print("{0} * {1} = {2}".format(a, b, (a*b)))    
    """
"""
count = int(input('반복할 횟수를 입력하세요')) 
for i in range(count) :
    print('hello world', i)
    """

    #문제 숫자 1개를 입력받아서 3의 배수 5의 배수 3,5배수를 출력하시오


"""
i = int(input("3의 배수와 5의 배수 찾기"))
for i in range(1, i+1) :
    
    if i % 3 == 0 and i % 5 == 0 :
        print("35")
    elif i % 3 == 0 :
        print("3")
    elif i % 5 == 0 :
        print("5")
    else :
        print("X")
"""
#강사님
"""
a = int(input("숫자입력? "))  #16

for i in range(1, a+1, 1) :
    if i%3==0 and i%5==0:
        print("{}-{}".format(i, "35"))
    elif i%3 == 0 :
        print("{}-{}".format(i, "3"))
    elif i%5 == 0 :
        print("{}-{}".format(i,"3"))
    else :
        print("{}-{}".format(i,"X"))
"""
"""
a = int(input("숫자입력? "))
for i in range(1, a+1, 1) :
    print(i)
    """

#1부터 10까지 짝수 갯수 구하기
"""
a=0
for i in range(1, 11, 1) :
    if i%2 == 0 :
        a=a+1
print(a)
"""
#숫자 1개를 입력 받아서 끝자리가 3과 7인 숫자의 개수를 구하시오.
"""a = int(input("숫자입력 "))
b = 0

for i in range(1, a+1, 1) :
    if i%10 == 3 or i%10 == 7 :
        b=b+1

print("개수는{}".format(b))
"""


#숫자 1개를 입력 받아서 끝자리가 3과 7인 숫자의 개수를 구하시오.

a=int(input("숫자입력"))
b=0

for i in range(1, a+1, 1) :
    if i%10 == 3 or i%10 == 7 :
        b=b+1
print("개수는{}".format(b))
    

10으로 나누었을 때 3이나 7

a = int(input("숫자입력"))
b = 0
for i in range(1, a+1, 1) :
    if i%10 == 3 or i%10 == 7 :
        b=b+1
print("개수는{}".format(b))        