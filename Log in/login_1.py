# 1)Open web Browser
# 2)Open URL to Login page
# 3)Enter Email
# 4)Enter Password
# 5) CLick on login
# 6) Capture title of the home page (actual title)
# 7) Verify title of the Page
# 8) Close browser

#correct password / correct username

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.app.worklenz.com/auth/login")
time.sleep(5)
driver.maximize_window()
driver.implicitly_wait(20)

email = "anupamaudeshani1999@gmail.com"
password = "#18Apc.3619#"

def login():
    emailbox = driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-layout/div[1]/div[1]/div/div/div/div/div/worklenz-login/form/nz-form-item[1]/nz-form-control/div/div/nz-input-group/input")
    emailbox.send_keys(email)
    time.sleep(5)
    passwordbox = driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-layout/div[1]/div[1]/div/div/div/div/div/worklenz-login/form/nz-form-item[2]/nz-form-control/div/div/nz-input-group/input")
    passwordbox.send_keys(password)
    time.sleep(5)
    loginbutton = driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-layout/div[1]/div[1]/div/div/div/div/div/worklenz-login/form/button[1]")
    loginbutton.click()
    time.sleep(10)

def check_page_load():
    print(driver.title)
    act_title = driver.title
    exp_title = "Worklenz | Home"
    if act_title == exp_title:
        print("login success")
    else:
        print("login fails")

def loginhome():
    Name = driver.find_element(By.XPATH,"//h3[@class='ant-typography ng-star-inserted']")
    text = Name.text
    print(text)

login()
check_page_load()
loginhome()
driver.close()
