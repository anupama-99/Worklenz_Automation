import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.app.worklenz.com/auth/login")
time.sleep(5)
driver.maximize_window()

def forgot_password():
    forgot_password = driver.find_element(By.CLASS_NAME,"login-form-forgot")
    forgot_password.click()

    print(driver.title)

def RTL():
    RTL_button = driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-reset-password/div/div/div/div/div/div/div/div[2]/div[2]/form/button[2]")
    RTL_button.click()
    time.sleep(3)

def Print():
    print(driver.title)

forgot_password()
RTL()
Print()

driver.quit()
