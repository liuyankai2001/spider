import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("driver/chromedriver.exe")
drver = webdriver.Chrome(service=service)

drver.get('https://passport.bilibili.com/login')
time.sleep(3)
sms_btn = drver.find_element(
    By.XPATH,
    '//*[@id="app-main"]/div/div[2]/div[3]/div[1]/div[3]'
)
sms_btn.click()

phone_txt = drver.find_element(
    By.XPATH,
    '//*[@id="app-main"]/div/div[2]/div[3]/div[2]/div[1]/div[1]/input'
)
phone_txt.send_keys('18303733675')

val_btn = drver.find_element(
    By.XPATH,
    '//*[@id="app-main"]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div[3]'
)
val_btn.click()

time.sleep(10)
drver.close()