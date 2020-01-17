import urllib.request, time
from bs4 import BeautifulSoup


url = "https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx"
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response, 'lxml')

# results = soup.find('select', id= 'cphContents_cphContents_cphContents_ddlTeam_ddlTeam', class_='select02')

#i가 2부터 11

for i in range(2,12,1):
    results = soup.select('#cphContents_cphContents_cphContents_ddlTeam_ddlTeam > option:nth-child(i)')
    print(results)
# print(results[1:11])
# result = results[1:11]
# print(result)
# for i in range(2,12,1):
    # team = i.text
    # print(team)
    # url_team = "https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx"
    # response_team = urllib.request.urlopen(url_team)
    # soup_team = BeautifulSoup(response_team, 'lxml')
    # team = soup_team.select('#cphContents_cphContents_cphContents_ddlTeam_ddlTeam > option:nth-child(i)')
    # print(team)






players = soup.select('#cphContents_cphContents_cphContents_udpContent > div.record_result > table > tbody > tr')


for player in players : 
    hitters = player.text
    # print(hitters)



