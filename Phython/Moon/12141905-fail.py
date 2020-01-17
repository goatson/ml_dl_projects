from bs4 import BeautifulSoup
import urllib.request, time




url = "https://www.youtube.com/results?search_query=KBO+%EB%A0%88%EC%A0%84%EB%93%9C"
# url = "https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y"
print(url)
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response, 'lxml')
print(response)



print(soup.find_all('p'))
print(soup.find_all('ytd-page-manager'))

# kbolink = driver.find_element_by_link_text('watch')
# print(kbolink)




        




