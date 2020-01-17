# /  나눈값
# // 나눈 정수만
# % 나머지


# a = int(input("국어점수"))
# # b = int(input("영어점수"))
# # c = int(input("수학점수"))


# # 5의 배수 인지 아닌지 확인


# if a%5 == 0 :
#     print("5의배수")
# else :
#     print("x")    

# x = int(input("숫자입력"))

# if 11 <= x <= 20:
#     print("11~20")
# elif 21 <= x <= 30:
#     print("21~30")     

# a,b,c = map(int, input("숫자를 3개 입력하세요"). split(","))


# print(a,b,c)
# print()

#숫자 1개를 입력받아서 3의 배수 5의 배수 3, 5배수를 출력하시오
#16을 입력했을 경우
#ex) 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ... 
#    X X 3 X 5 3 X X 3  5  X  3  X  X 35 X ...

for i in range(1, 16) :
    print(i, end=" ")
    if i%3 and i%5== 0 :
        print(35)

    elif i%3 == 0 :
        print(3)
    
    elif i%5 == 0 :
        print(5)
