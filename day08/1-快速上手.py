import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("driver/chromedriver.exe")
drver = webdriver.Chrome(service=service)

drver.get('https://passport.bilibili.com/login')
time.sleep(10)
drver.close()