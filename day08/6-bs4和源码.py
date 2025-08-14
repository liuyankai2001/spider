import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

service = Service("driver/chromedriver.exe")
drver = webdriver.Chrome(service=service)

drver.get('https://passport.bilibili.com/login')

html_string = drver.page_source
print(html_string)