from selenium import webdriver
from selenium.webdriver.common.by import By
import time


url = "https://www.musinsa.com/app/"

browser = webdriver.Safari()
browser.get(url)
 
time.sleep(1)
login = browser.find_element(By.XPATH, '//*[@id="topCommonPc"]/header/div[3]/button')
login.click()

time.sleep(3)

_id = browser.find_element(By.XPATH, '/html/body/div[1]/section[1]/div[1]/form/div[1]/div[1]/div/input')
_id.send_keys('user_id')

_pw = browser.find_element(By.XPATH, '/html/body/div[1]/section[1]/div[1]/form/div[1]/div[2]/div/input')
_pw.send_keys('password')

time.sleep(1)
browser.find_element(By.XPATH, '/html/body/div[1]/section[1]/div[1]/form/div[2]/button').click()


time.sleep(5)
