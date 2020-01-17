import requests as rq
import re
import controler as con
import model as md

custlist=[]
page=-1
while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''').upper()
    if choice == "I":
        con.insert()

    elif choice == "C":
        con.customer()

    elif choice == "P":
        con.pre()

    elif choice == "N":
        con.nxt()

    elif choice == "U":
        con.update()

    elif choice == "D":
        con.delete()
        
    elif choice == "Q":
        break
    
    