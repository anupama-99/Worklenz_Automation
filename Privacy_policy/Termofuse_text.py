import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.app.worklenz.com/privacy-policy")
driver.implicitly_wait(10)

def termText():
    textLink = driver.find_element(By.XPATH,"//*[@id='worklenz_privacy']/div/div[1]/p[3]/a")
    textLink.click()
    print(driver.title)


def verify():
    exp_title = driver.title
    act_title = "Worklenz | Terms of Use"
    if exp_title == act_title:
        print("success")
    else:
        print("not success")

termText()
verify()
