#conda install cx_oracle  -> 이렇게 생긴 모듈을 다운받는 것
#import cx_Oracle as oci
#import func

def sum(a,b) :
    return a+b


#a=sum(7,8)

def sub(a,b) :
    return a-b  

def mul(a=1, b=1) :
    return a*b

#a = fc.mul(b=56)

def tot(a):   #1부터 a까지 합을 구하시오.
    s=0
    for i in range(1, a+1, 1) : 
        s=s+i
    return tot

def avg(a):   #1부터 a까지 평균을 구하시오.
    sum = 0
    avg = 0
    for i in range(1, a+1) :
        sum = sum + i
        avg = sum/a
    print("1부터 a까지 평균은", avg, "입니다.")
    return avg  
    
if __name__ == "__main__" :   #여기서만 수행하고 싶을 때
    print("AAA")
    print("__name__")
