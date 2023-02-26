from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()
driver.get("https://claystage.com/one-piece-chapter-release-schedule-for-2023")
time.sleep(2)

weeksList = []
chapterList = []
dateList = []
for i in range(1,53):
    xPath = '//*[@id="post-3990"]/div/div[2]/figure/table/tbody/tr[' + str(i) + ']/td'
    weeksList.append(driver.find_element(By.XPATH,xPath).text)
    xPath = '//*[@id="post-3990"]/div/div[2]/figure/table/tbody/tr[' + str(i) + ']/td[2]'
    chapterList.append(driver.find_element(By.XPATH,xPath).text)
    xPath = '//*[@id="post-3990"]/div/div[2]/figure/table/tbody/tr[' + str(i) + ']/td[3]'
    dateList.append(driver.find_element(By.XPATH,xPath).text)

df = pd.DataFrame(zip(weeksList,chapterList,dateList),columns=['Weeks','Chapters',"Release Dates"])
print(df)

currentChapter = df._get_value(8,'Chapters')
print(currentChapter)



'''
XPATH HOLDER
//*[@id="post-3990"]/div/div[2]/figure/table/tbody/tr[2]/td[2]
//*[@id="post-3990"]/div/div[2]/figure/table/tbody/tr[2]/td[2]

weeks = driver.find_element(By.XPATH,'//*[@id="post-3990"]/div/div[2]/figure/table/tbody/tr')
'''