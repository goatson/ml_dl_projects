# py=모듈과 폴더=패키지(같은놈끼리 묶어라)
from sklearn.externals import joblib
import json, re
import os
import sys
import urllib.request
import db

#1. python 3.3 이하 버전과 하위 호환을 위해서 사용
#2. 패키지 자체를 지칭할 때 사용
#없으면 패키지 자체를 못땡긴다
# run 시키면 항상 실행

# <5단계 개발자가 던져줘야>

# 0. 경로 -> 상수값 -> 환경변수 혹은 DB에서 획득
MODEL_LABEL = './ml/clf_labels.label'
MODEL_PATH = './ml/clf_model_202001161419.model'

if __name__ != '__main__':
    # 1. 모델 로드(1회만) -> 요청이 많아지면 컨트롤이 가능한지 체크  - 변수처리
    clf = joblib.load( MODEL_PATH )
    # 2. 레이블 로드  - 변수처리
    with open(MODEL_LABEL, 'r') as f:
        clf_label = json.load(f)

# 3. 예측 함수 (in:텍스트, out:예측결과)  - 함수처리
def detect_lang( text ):
    # text -> 빈도계산 -> 알고리즘에 예측요청(데이터 주입) -> 그 결과를 리턴
    text = text.lower()           # 1. 소문자 처리
    p = re.compile('[^a-z]')      # 2. 알파벳 소문자만 제외 a-z를 배제 , 한칸 더 남는다.
    text = p.sub( '', text)       # 3. 소문자만 남는다.
    counts = [ 0 for n in range(26) ] # 알파벳별 카운트를 담을 공간(리스트)
    limit_a = ord('a') # 매번 반복해서 작업하니까 그냥 최초 한번 변수로 받아서 사용
    for word in text:
        counts[ord(word)-limit_a] += 1 # 문자 1개당 카운트 추가
    # 빈도수는 값이 너무 퍼져 있어서 0-1 사이로 정규화를 하겠다. => 학습효과가 뛰어나니까    
    total_count = sum(counts)
    freq = list(map( lambda x:x/total_count , counts))  # 정규화
    
    # B. 알고리즘에 예측요청(데이터 주입) ------------------------------------------
    predict = clf.predict( [freq] )  # 입력 형태를 개발했던 형태와 동일하게 차원을 맞춘다. # 2차리스트여야 하니까 정적구성!
    na_code = predict[0]             # 'en' or 'fr' ...
    na_str = clf_label[ na_code ]   # '영어', '프랑스어', ...
    
    # C. 결과를 리턴 -------------------------------------------------------------
    return na_code, na_str    
    #pass

# 개인별로 신청한 키
CLIENT_ID = 'SkSQh3KCVw5NR7_F9Emw'
SECRET_KEY = '3UVO2Hhw8c'
PAPAGO_URL = "https://openapi.naver.com/v1/papago/n2mt"   # 주소 / 변하지 않으니 대문자
'''
POST 방식
curl "https://openapi.naver.com/v1/papago/n2mt" \
-H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" \
-H "X-Naver-Client-Id: SkSQh3KCVw5NR7_F9Emw" \
-H "X-Naver-Client-Secret: 3UVO2Hhw8c" \
-d "source=ko&target=en&text=만나서 반갑습니다." -v
'''
# -H : header
# -d : parameter
# target : 번역결과값

# 4. 번역 함수 (현 : 파파고연동, 향후 : RNN 구현) - 함수처리
def transfer_lang(text, na_input_code='en', na_output_code='ko'):
    print('파파고와 연동한 번역 처리 시작')

    encText = urllib.parse.quote(text)          # 한글의 URL 인코딩 처리 => %2D.... 변환처리
    data = "source={}&target={}&text={}".format(na_input_code, na_output_code, encText)      # 파라미터 구성
    print(data)
    request = urllib.request.Request(PAPAGO_URL)            # 요청객체 생성
    request.add_header("X-Naver-Client-Id",CLIENT_ID)       # 헤더 설정
    request.add_header("X-Naver-Client-Secret",SECRET_KEY)  # 헤더 설정
    # javascript의 $.post와 같다.
    response = urllib.request.urlopen(request, data=data.encode("utf-8")) # 요청
    rescode = response.getcode() # 응답코드 획득
    if(rescode==200): # 응답 성공
        return json.load( response )        
    else:
        return {}   # 딕셔너리 리턴


                                    

# 미드웨어 서버다.
# 이 코드는 개발 시 테스트했던 코드이다.
# 의도될때만 작동해야한다.
if __name__ =='__main__':
    # print('테스트')
    test_str = 'Bong Joon-ho (Korean: 봉준호, Korean pronunciation: [poːŋ tɕuːnho → poːŋdʑunɦo]; born September 14, 1969) is a South Korean film director and screenwriter. He garnered international acclaim for his second feature film Memories of Murder (2003), before achieving commercial success with his subsequent films The Host (2006) and Snowpiercer (2013), both of which are among the highest-grossing films of all time in South Korea.[1]'
    transfer_lang(test_str)

    