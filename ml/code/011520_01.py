import re
import os.path, glob

file_list = glob.glob('./data/train/*.txt')
# print(len(file_list))
# print(file_list)

# 1. 파일명 획득
fNames = file_list[:]
# print(fNames)  # 리스트

# 2. 파일명 획득
for fName in fNames :
    name = os.path.basename(fName)
    # print(name)
    # 3. 파일명에는 정답(레이블)이 들어있다. 이것을 추출
    # 확장성을 고려해 정규식으로 처리
    p = re.compile('^[a-z]{2}')  #^[] 시작
    if p.match(name) :
        lang = p.match(name).group()
    else : 
        print('일치하지 않음')
    # print(lang)
    # 4. 알파벳 빈도 계산
    # 4-1. 파일을 읽는다.
    f = open(fName, encoding='utf-8')
    txt = f.read()
    # print(txt, '@@@')

    # 4-2. 알파벳만 남긴다.(정규식으로 전처리)
    p = re.compile('[^a-zA-Z]*')  # 알파벳 배제     # * : 0부터 무한대
    txt = p.sub('', txt)
    # print(type(txt))
    # print(txt[-1])
    txt.lower()
    print(txt.lower())
    print(len(txt))