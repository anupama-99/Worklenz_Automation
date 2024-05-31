import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.app.worklenz.com/privacy-policy")
driver.implicitly_wait(10)


def login():
    login_button = driver.find_element(By.XPATH,"//*[@id='navbarSupportedContent']/div/a[1]/button")
    login_button.click()
    print(driver.title)

login()



