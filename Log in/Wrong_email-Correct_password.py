#wrong username / correct password

import time                      ###   not correct code   ###

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.app.worklenz.com/auth/login")
time.sleep(5)
driver.maximize_window()
driver.implicitly_wait(20)

email = "anupamaudeshani9@gmail.com"
password = "#18Apc.3619#"

def login():
    emailbox = driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-layout/div[1]/div[1]/div/div/div/div/div/worklenz-login/form/nz-form-item[1]/nz-form-control/div/div/nz-input-group/input")
    emailbox.send_keys(email)

    passwordbox = driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-layout/div[1]/div[1]/div/div/div/div/div/worklenz-login/form/nz-form-item[2]/nz-form-control/div/div/nz-input-group/input")
    passwordbox.send_keys(password)

    loginbutton = driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-layout/div[1]/div[1]/div/div/div/div/div/worklenz-login/form/button[1]")
    loginbutton.click()


def alertdisplay():
    alert = driver.find_element(By.XPATH,"//*[@id='cdk-overlay-0']/nz-notification-container/div[2]/nz-notification/div/div/div/div/div[2]")
    print(alert.is_displayed())
    print(alert.text)


login()
alertdisplay()
driver.close()