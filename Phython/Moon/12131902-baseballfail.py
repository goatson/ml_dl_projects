from selenium import webdriver
import requests, time
from bs4 import BeautifulSoup
import json


driver = webdriver.Chrome('./chromedriver.exe')
kbo = driver.get("https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx")
time.sleep(1)

team = driver.find_element_by_id('cphContents_cphContents_cphContents_ddlTeam_ddlTeam')
team.click()
time.sleep(1)

teamlist =['OB','LT','SS','WO','HH','HT','KT','LG','NC','SK']  

list_record = []
record = {}
for team_i in teamlist:

    ### 1번째 페이지 ###
    team_1 = driver.find_element_by_xpath(f"//option[@value='{team_i}']")
    team_1.click()
    time.sleep(1)

    source_1 = driver.page_source
    bs_1 = BeautifulSoup(source_1,'lxml')
    # print(bs)

    entire_1 = bs_1.find(class_="record_result")  
    # print(entire)

    for i, r in enumerate(entire_1.find_all('tr')):
        for j, c in enumerate(r.find_all('td')):
            # print(j, c)
            if j == 0:
                record.update({'순위':int(c.text)})
            elif j ==1:
                record.update({'선수명':str(c.text)})
            elif j ==2:
                record.update({'팀명':str(c.text)})         
            elif j ==3:
                record.update({'AVG':str(c.text)}) 
            elif j ==4:
                record.update({'G':str(c.text)})
            elif j ==5:
                record.update({'PA':str(c.text)})
            elif j ==6:
                record.update({'AB':str(c.text)})
            elif j ==7:
                record.update({'R':str(c.text)})
            elif j ==8:
                record.update({'H':str(c.text)})
            elif j ==9:
                record.update({'2B':str(c.text)})
            elif j ==10:
                record.update({'3B':str(c.text)})
            elif j ==11:
                record.update({'HR':str(c.text)})
            elif j ==12:
                record.update({'TB':str(c.text)})
            elif j ==13:
                record.update({'RBI':str(c.text)})
            elif j ==14:
                record.update({'SAC':str(c.text)})
            elif j ==15:
                record.update({'SF':str(c.text)})
    
# print(record)


### 2번째 페이지 ### 있으면   ###없으면 스킵
    # try:
    #     team_2 = driver.find_element_by_id("cphContents_cphContents_cphContents_ucPager_btnNo2")
    #     team_2.click()
    #     time.sleep(1)    
    #     source_2 = driver.page_source
    #     bs_2 = BeautifulSoup(source_2,'lxml')

    #     entire_2 = bs_2.find(class_="record_result")  #tData01 tt
    #     # print(entire)
    #     for i, r in enumerate(entire_1.find_all('tr')):
    #         for j, c in enumerate(r.find_all('td')):
    #             # print(j, c)
    #             if j == 0:
    #                 record = ({'순위':int(c.text)})
    #             elif j ==1:
    #                 record.update({'선수명':str(c.text)})
    #             elif j ==2:
    #                 record.update({'팀명':str(c.text)})         
    #             elif j ==3:
    #                 record.update({'AVG':str(c.text)}) 
    #             elif j ==4:
    #                 record.update({'G':str(c.text)})
    #             elif j ==5:
    #                 record.update({'PA':str(c.text)})
    #             elif j ==6:
    #                 record.update({'AB':str(c.text)})
    #             elif j ==7:
    #                 record.update({'R':str(c.text)})
    #             elif j ==8:
    #                 record.update({'H':str(c.text)})
    #             elif j ==9:
    #                 record.update({'2B':str(c.text)})
    #             elif j ==10:
    #                 record.update({'3B':str(c.text)})
    #             elif j ==11:
    #                 record.update({'HR':str(c.text)})
    #             elif j ==12:
    #                 record.update({'TB':str(c.text)})
    #             elif j ==13:
    #                 record.update({'RBI':str(c.text)})
    #             elif j ==14:
    #                 record.update({'SAC':str(c.text)})
    #             elif j ==15:
    #                 record.update({'SF':str(c.text)})

    #     team_3 = driver.find_element_by_id("cphContents_cphContents_cphContents_ucPager_btnNo1")
    #     team_3.click()
    #     time.sleep(1)

    # except:
    #     team_3 = driver.find_element_by_id("cphContents_cphContents_cphContents_ucPager_btnNo1")
    #     team_3.click()
    #     time.sleep(1)
        

        
    


        # try:
        #     list_record.append(record)
       

# with open('./hitter.json','wt') as f:
#     json.dump(list_record,f)




### 2번째 페이지 ### 있으면   ###없으면 스킵
#     team_2 = driver.find_element_by_id("cphContents_cphContents_cphContents_ucPager_btnNo2")
#     team_2.click()
#     time.sleep(1)    
#     source_2 = driver.page_source
#     bs_2 = BeautifulSoup(source_2,'lxml')

#     entire_2 = bs_2.find(class_="record_result")  #tData01 tt
#     # print(entire)
#     for i, r in enumerate(entire_2.find_all('tr')):
#         # print(i, r)
#         player()
        


        
# #     ### 다시 1번째 페이지 ###

#     team_3 = driver.find_element_by_id("cphContents_cphContents_cphContents_ucPager_btnNo1")
#     team_3.click()
#     time.sleep(1)
        
    


  
#         team_3 = driver.find_element_by_id("cphContents_cphContents_cphContents_ucPager_btnNo1")
#         team_3.click()
#         time.sleep(1)
    
        


    

# print(list_record)
# with open('./hitter.json','wt') as f:
#     json.dump(list_record,f) 


    # for j in range(1, 10, 1):
    #     try:
    #         team_2 = driver.find_element_by_id("cphContents_cphContents_cphContents_ucPager_btnNo" + j)
    #         team_2.click()

    #         time.sleep(1)    
    #         source_2 = driver.page_source
    #         bs_2 = BeautifulSoup(source_2,'lxml')

    #         entire_2 = bs_2.find(class_="record_result")  #tData01 tt
    #         # print(entire)
    #         for i, r in enumerate(entire_2.find_all('tr')):
    #             # print(i, r)
    #             player()

    #     except:
    #         print("페이지없음")
        
        




