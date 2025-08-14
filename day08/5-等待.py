import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

service = Service("driver/chromedriver.exe")
drver = webdriver.Chrome(service=service)

drver.get('https://passport.bilibili.com/login')
time.sleep(2)

sms_btn = WebDriverWait(drver,30,0.5).until(lambda dv:dv.find_element(
    By.XPATH,
    '//*[@id="app-main"]/div/div[2]/div[3]/div[1]/div[3]'
))

sms_btn.click()
time.sleep(2)
drver.close()