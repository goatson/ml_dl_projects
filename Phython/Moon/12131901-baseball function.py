def player(self,r):
    for j, c in enumerate(r.find_all('td')):
            # print(j, c)
        if j == 0:
            record = {'순위':int(c.text)}
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



# for team_i in teamlist:

#     team = driver.find_element_by_xpath(f"//option[@value='{team_i}']")
#     team.click()
#     time.sleep(1)

#     source = driver.page_source
#     bs = BeautifulSoup(source,'lxml')
#     # print(bs)

#     entire = bs.find(class_="record_result")  #tData01 tt
#     # print(entire)

#     for i, r in enumerate(entire.find_all('tr')):
#         # print(i, r)
#         for j, c in enumerate(r.find_all('td')):
#             # print(j, c)
#             if j == 0:
#                 record = {'순위':int(c.text)}
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

#     team = driver.find_element_by_id("cphContents_cphContents_cphContents_ucPager_btnNo2")
#     team.click()
#     time.sleep(1)    
#     entire = bs.find(class_="record_result")  #tData01 tt
#     # print(entire)

#     for i, r in enumerate(entire.find_all('tr')):
#         # print(i, r)
#         for j, c in enumerate(r.find_all('td')):
#             # print(j, c)
#             if j == 0:
#                 record = {'순위':int(c.text)}
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

#                 # print(record)

#     team = driver.find_element_by_id("cphContents_cphContents_cphContents_ucPager_btnNo1")
#     team.click()
#     time.sleep(1)    
#     entire = bs.find(class_="record_result")  #tData01 tt
#     # print(entire)

#     for i, r in enumerate(entire.find_all('tr')):
#         # print(i, r)
#         for j, c in enumerate(r.find_all('td')):
#             # print(j, c)
#             if j == 0:
#                 record = {'순위':int(c.text)}
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

#                 print(record)