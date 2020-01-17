import urllib.request
import os

#이미지의 주소
url='http://fla.kr/ueJV'

#실행하는 파일의 경로를 찾아서 같은 경로에 이미지 저장
dirname=os.path.dirname(__file__)
savename=dirname +'/test.jpg'

#파일을 열고.. 활용 할 수 있다.
mem = urllib.request.urlopen(url).read()

#위에서 불러온 파일을 저장함
print(savename)
with open(savename,mode='wb') as f:
    f.write(mem)
    print('저장되었습니다.')