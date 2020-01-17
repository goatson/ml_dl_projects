
import requests
import json
import csv

url="http://ihongss.com/json/exam7.json"  #서버주소
str1 = requests.get(url).text  # 문자열
dic1 = json.loads(str1)  #type변경

a = dic1['data']
b = []


for i in a :
    b.append(   [ i['id'], i['name'], i['age'], i['height'], i['weight'] ]  )
print(b)   
print()


for i in b :
    print(i)
print()




while True :
    menu = int(input("숫자를 입력하세요(1:추가, 2:수정, 3:삭제, 4:목록, 5:저장, 6:읽기, 0:종료)"))
    if menu == 0 :  #종료
        break
    elif menu == 1 :  #추가 5개 항목을 입력받아서 추가하기
        # str, str, int, float, float
        a1,a2,a3,a4,a5 = map(str,input("아이디, 이름, 나이, 키, 몸무게 입력?").split(","))
        b.append(  [a1,a2,a3,a4,a5]  )   # [   [],[],[],[],[]   ]

    elif menu == 2 : #수정
        
    
        d = int(input("수정할 정보의 위치?"))
        e = int(input("몇번째의 값를 수정하시겠습니까?"))
        f = str(input("어떤값으로 수정하시겠습니까?"))

        b[d][e] = f
        
        
        a1 = float(input("수정 할 몸무게 입력?"))
        a2 = float(input("몸무게?"))
        # a3 = input("이름?")
        # a4 = int(input("나이?"))
        # a5 = float(input("키?"))
        # a6 = float(input("몸무게?"))

        for i, t in enumerate(b) :  #[  [],[],[],[],[]  ]
            if t[4] == a1 :
                b[i][4] = a2


    elif menu == 3 : #삭제
        #n = int(input("삭제할 위치 입력?"))
        #del b[n]   #[  [], [], [], [], []  ]

        s = input("삭제할 아이디 입력?")
        for i, t in enumerate(b): #[  [],[],[],[],[]  ]
            if t[0] == s :
                del b[i]
                break
        
    elif menu == 4 : #목록
        print(b)

    elif menu == 5 : #저장
        # 엑셀에서 한글을 보기 위해 엔코딩을 cp949로 설정
        f = open('c:/data/20191115.csv', 'w', encoding='cp949', newline='')       
        
        wr = csv.writer(f)
        # wr = csv.DictWriter(f, fieldnames=['id','name','age','height','weight'])
        # wr.writeheader()

        for tmp in b :
            wr.writerow(tmp) #wr.writerow(  ['a','가나다',34,165.7,56,6]  )
        f.close()

    elif menu == 6:  #읽기
        b.clear() #리스트 다 지우기
        f = open('c:/data/20191115.csv', 'r', encoding='cp949')
        rdr = csv.reader(f)
        #next(rdr, None) #첫번째 라인을 skip


        # for idx, tmp in enumerate(rdr):  # index,  값
        #     b.append( [ tmp[0], tmp[1], int(tmp[2]), float(tmp[3]), float(tmp[4]) ]  )
        #     print(idx+1, tmp)

        print(type(rdr))
        for line in rdr:
            print(line)
            b.append(line)
        print(b)
        f.close()
        


        # 문자열로 읽음
        # 문자열을 리스트로 변환(타입도 str, str, int, float, float)
        # b배열에 넣어줌

"""
import csv
f = open('c:/Users/ihong/Documents/data/exam1.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
next(rdr,None)  #첫번째 라인을 skip
#numlines = len(f.readlines())
"""

"""
1. 서버에서 exam7.json 데이터 받기
2. 2차원 리스트로 만들기
3. 무한반복 구현 while문
4. 숫자를 1개 받음 그 숫자가 0이면 break
5. 메뉴 구성(1번 추가, 2번 수정, 3번 삭제, 4번 목록, 0번 종료)
"""



"""
print(dic1)  # {}
print(type(dic1))
print()

print(dic1["ret"])
print()

print(dic1["data"])  #[]
print()

for i in (dic1["data"]) :
    print(i)
print()

for key in (dic1["data"][0]) :
    print(key)
print()

for k,v in (dic1["data"][0].items()) :
    print(k,v)
print()

a = dic1["data"]  #[{},{},{},{},{}]
print(a)
print(type(a))

for i in a :
    print("{},{},{},{},{}".format(i["id"], i["name"], i["age"], i["height"], i["weight"]))
print()

for i in (dic1["data"]) :
    print(i)
print()    

#그냥 돌리면 key만 나오고 key값 넣어야 value가 나온다.
"""