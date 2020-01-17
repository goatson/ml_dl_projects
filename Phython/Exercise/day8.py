
import cx_Oracle as oci   #conda install cx_oracle
import pandas as pd       #conda install pandas  <= 설치되어 있음
  

conn=oci.connect("admin/1234@192.168.99.100:32764/xe", encoding="utf-8")
cursor=conn.cursor() #커서 생성

# 가져오기 SELECT : SELECT * FROM 테이블명
# 수정하기 UPDATE : UPDATE 테이블명 SET 컬럼명=변경값 WHERE 조건
# 추가하기 INSERT : INSERT INTO 테이블명 VALUES(추가할값들...)
# 삭제하기 DELETE : DELETE FROM 테이블명 WHERE 조건
# ROLLBACK
# commit


# 1:추가, 2:삭제, 3:수정, 4:목록 5:검색, 0:종료
while True:
    menu = int(input("1:추가, 2:삭제, 3:수정, 4:목록, 5:검색, 0:종료 ??  "))
    if menu == 0:
        break
    elif menu == 1:
        #입력할 항목을 입력받으세요.
        str1 = input("추가할 항목을 입력?") #1,a,b,1000,100,AAA
        arr = str1.split(",")
        sql = "INSERT INTO ITEM VALUES(:1,:2,:3,:4,:5,:6,SYSDATE)"
        cursor.execute(sql, arr)  #[]리스트 형태
        conn.commit() #적용 완료

    elif menu == 2:
        #삭제 구현
        str1 = int(input("삭제할 물품번호 입력? "))  #1
        sql = "DELETE FROM ITEM WHERE ITM_NO=:no"
        cursor.execute(sql,no=str1)
        conn.commit() #적용 완료
        
    elif menu == 3:
        # 변경할 글번호,
        # 변경할 내용들(이름, 내용, 가격, 재고수량, 분류)
        no = input("수정할 글 번호 입력")
        str1 = input("수정할 항목 입력")
        arr1 = str1.split(",")
        arr1.append(no)
        sql = "UPDATE ITEM SET ITM_NAME=:1, ITM_CONTENT=:2, ITM_PRICE=:3, ITM_QTY=:4, ITM_CATE=:5 WHERE ITM_NO=:no"
        cursor.execute(sql,arr1)
        conn.commit() #적용 완료
        
    elif menu == 4:
        df = pd.read_sql('SELECT * FROM ITEM ORDER BY ITM_NO ASC', con=conn)
        print(df)
        
    
        #목록 => Dataframe형태로
    elif menu == 5:
        while True :
            info = int(input("1:물품명, 2:물품 내용, 3:물품 가격. 4:물품 양, 5:물품 카테고리"))
            if info == 1 :
                str1 = input("검색할 물품명 입력")
                sql1 = f"SELECT * FROM ITEM WHERE ITM_NAME=\'{str1}\'"
                df1 = pd.read_sql(sql1, con=conn)
                print(df1)
               
            elif info == 2 :
                str2 = input("검색할 물품내용 입력")
                sql2 = f"SELECT * FROM ITEM WHERE ITM_CONTENT=\'{str2}\'"
                df2 = pd.read_sql(sql2, con=conn)
                print(df2)
            elif info == 3 :    
                str3 = input("검색할 가격 입력")
                sql3 = f"SELECT * FROM ITEM WHERE ITM_PRICE=\'{str3}\'"
                df3 = pd.read_sql(sql3, con=conn)
                print(df3)
            elif info == 4 :    
                str4 = input("검색할 양 입력")
                sql4 = f"SELECT * FROM ITEM WHERE ITM_QTY=\'{str4}\'"
                df4 = pd.read_sql(sql4, con=conn)
                print(df4)
            elif info == 5 :    
                str5 = input("검색할 카테고리 입력")
                sql5 = f"SELECT * FROM ITEM WHERE ITM_CATE=\'{str5}\'"
                df5 = pd.read_sql(sql5, con=conn)
                print(df5)        
        #sql = "SELECT * FROM ITEM WHERE ITM_NAME LIKE '% || :keyword ||"
        #가능하다면 검색 구현
                

"""
sql = "SELECT * FROM ITEM" #ITEM 테이블에서 모든 데이터 가져오는 SQL
cursor.execute(sql)
data = cursor.fetchall()
print( type(data) )
print( data )
print()

# 아이디/암호@서버주소:포트번호/SID
conn = oci.connect('admin/1234@192.168.99.100:32764/xe',encoding="utf-8")
df = pd.read_sql('SELECT * FROM ITEM', con=conn)
print(df)
print()

a=[]
for i in data :
    a.append( list(i) )
print(a)
"""
