import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("driver/chromedriver.exe")
drver = webdriver.Chrome(service=service)

drver.get('https://www.5xclass.cn/')

# /html/body/div[1]/div[2]/div/div/div[2]/div[9]/a/dl/dd/div[1]/p[1]

# tag = drver.find_element(By.CLASS_NAME,'nav-menu')
tag_list = drver.find_elements(By.XPATH,'//div[@class="name"]/p[1]')
for tag in tag_list:
    print(tag.text)

# time.sleep(10)
drver.close()