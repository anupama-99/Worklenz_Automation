import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.app.worklenz.com/privacy-policy")
driver.implicitly_wait(10)

def tryforfree():
    try_button = driver.find_element(By.XPATH,"//*[@id='navbarSupportedContent']/div/a[2]/button")
    try_button.click()
    print(driver.title)

tryforfree()