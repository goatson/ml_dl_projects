# 접속 함수
import pymysql
def insert_trans_log(oCode, tCode, oStr, tStr):
    # 차후 db쪽 연결은 pooling이나 ORM 방식을 이용하여 최대 동접에 대한 안정적인 처리를 구현한다.
    # 현재는 그냥 요청하면 접속, 쿼리, 접속해제순으로 처리
    # 해당 접속법은 임시적이다.
    connection = pymysql.connect(host='localhost',  # = 127.0.0.1
                             user='root',
                             password='12341234',
                             db='py_db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
                            # DictCursor 안쓰면 리스트/튜플 -> db 테이블 순서 바뀌면 코드 다 수정해야한다.
    
        
    try:
        # 쿼리
        with connection.cursor() as cursor:
            # 쿼리문
            sql = '''
            INSERT INTO `py_db`.`tbl_trans_lang_log`
             (`oCode`, `tCode`, `oStr`, `tStr`)
            VALUES
             (%s, %s, %s, %s);
            '''
            # 쿼리 수행
            cursor.execute(sql,  (oCode, tCode, oStr, tStr) )  # 튜플로 들어간다!

        # 커밋 수행(디비에 실제 반영)
        connection.commit()

    except Exception as e:    #Exception : 예외의 super클래스
        print(e)
    finally:
        if connection :
            connection.close()
            