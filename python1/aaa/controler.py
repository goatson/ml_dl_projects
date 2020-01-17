import requests as rq
import re
custlist=[]
page=-1

def insert():
    customer={'name':'','sex':'',"email":'',"birthyear":''}
    customer['name']=input("이름을 입력하세요 : ")
    while True:
            customer['sex']=input("성별(M/m 또는 F/f)을 입력하세요 : ")
            customer['sex']=customer['sex'].upper()
            if customer['sex'] in ('M','F'):
                break
    while True: # 중복되지 않게 입력

        regex = re.compile('^[a-z][a-z0-9]{4,10}@[a-zA-Z]{2,6}[.][a-zA-Z]{2,3}$')
        while True:
            customer['email']=input("이메일 : ") 
            golbang = regex.search(customer['email'])
            if golbang:
                break
            else:
                print('"@"을 포함한 메일적어줘')
        check=0
        for i in custlist:
            if i['email']==customer['email']:
                check=1
        
        if check==0:
            break
        print('중복')
    while True:
        customer['birthyear']=input("생일언제야 : ")
        
        if len(customer['birthyear']) == 4 and customer['birthyear'].isdigit():
            break
    print(customer)
    custlist.append(customer)
    print(custlist)
    # page += 1
    page=len(custlist)-1
    print(page)

def customer():
    if page >= 0:
        print("현재 페이지는 {}쪽 입니다".format(page + 1))
        print(custlist[page])
    else:
        print("입력된 정보가 없습니다.")

def pre():
    if page <= 0:
        print('첫 번 째 페이지이므로 이전 페이지 이동이 불가합니다')
        print(page)
    else:
        page -= 1
        print("현재 페이지는 {}쪽 입니다".format(page + 1))
        print(custlist[page])

def nxt():
    if page >= len(custlist)-1:
        print('마지막 페이지이므로 다음 페이지 이동이 불가합니다')
        print(page)
    else:
        page += 1
        print("현재 페이지는 {}쪽 입니다".format(page + 1))
        print(custlist[page])

def update():
    while True:
        choice1=input('수정하시려는 고객 정보의 이메일을 입력하세요 : ') 
        idx=-1
        for i in range(0,len(custlist)):
            if custlist[i]['email'] == choice1:
                idx=i
                break
        if idx==-1:
            print('등록되지 않은 이메일입니다.')       
            break
                    
        choice2=input('''
        다음 중 수정하실 정보를 골라주세요 
                name, sex, birthyear
        (수정할 정보가 없으면 'exit' 입력)
        ''')
        if choice2 in ('name','sex','birthyear'):
            custlist[idx][choice2]=input('수정할 {}을 입력하세요 :'.format(choice2))
            break
        elif choice2 =='exit':
            break
        else:
            print('존재하지 않는 정보입니다.')
            break
            
def delete():
    choice1 = input('삭제하려는 고객 정보의 이메일을 입력하세요.')
    delok = 0
    for i in range(0,len(custlist)):
        if custlist[i]['email'] == choice1:
            print('{} 고객님의 정보가 삭제되었습니다.'.format(custlist[i]['name']))
            del custlist[i]
            print(custlist)
            delok = 1
            break
    if delok == 0:
            print('등록되지 않은 이메일입니다.')
            print(custlist)

# def logic():
#     if choice == 'Y' : 
#         res = rq.get(url)
#         # break
#     elif choice == 'N' :
#         print("프로그램 종료")
#         # break
#     else :
#         print("다시 입력해주세요")
#         # continue
#     url = ()"http://blog.naver.com/pjt3591oo"
#     res = rq.get(url)   # 해당 url로 GET 요청
#     res = rq.post(url)  # 해당 url로 POST 요청
#     print(res)