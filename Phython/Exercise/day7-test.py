a = 11
b = 5
d = int("1")  #숫자 1
e = "2"
c = a //b # /값 //는 몫  + - *

# d+e = "12"  # 문자로 되있는건 합친다

a = 13

if a >= 34 or a>=45:
    print("1")
elif a >= 20:
    print("2")    
else :
    print("3")    
print("4")    

for i in range(1,15,3):  #1 4 7 ...14
    print(i)
print()

a = [4,5,6,7,8,9]   #list
print(a[:3])   #4 5 6
print(a[1:3])  # 5 6
print()

b = {1,2,3,3,4}  #set
print(b)  #1,2,3,4,
c = {2,4,5}
print(b&c)  #b-c b|c  
print()

d = (1,2,3,5)  #tuple -> 수정 불가
print()

e = {"aaa":1, "bbb":2} #dictionary
e["aaa"] = 45  # => 덮어쓰기  "aaa" : 45
print()

f = open("파일위치", "a")  #교재 409p 파일 끝에 추가


def func(x=1, y=2, z=3, k=9):
    return x+y+z+k

func(x=10,y=20)  #42
func(5, z=20)  # x=5, z=20