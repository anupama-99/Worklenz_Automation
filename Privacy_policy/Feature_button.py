import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://uat.app.worklenz.com/privacy-policy")

def feature():
    feature_button = driver.find_element(By.XPATH,"//*[@id='navbarSupportedContent']/ul/li[2]/a")
    feature_button.click()
    print(driver.title)

feature()