# 1)Open web Browser
# 2)Open URL to sign up page
# 3)Enter Full name
# 4)Enter Email
# 5)Enter Password
# 5) CLick on Sign up
# 6) Capture title of the setup account page (actual title)
# 7) Verify title of the Page
# 8) Close browser

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("https://app.worklenz.com/auth/signup")
time.sleep(5)
driver.maximize_window()

Fullname = "Anupama udeshani"
Email = "anupamaudeshani1999@gmail.com"
Password ="#18ApC.3619#"

Name_element = driver.find_element(By.ID,"full-name")
Email_element = driver.find_element(By.ID,"email")
Password_element = driver.find_element(By.ID,"password")
Name_element.send_keys(Fullname)
time.sleep(2)
Email_element.send_keys(Email)
time.sleep(2)
Password_element.send_keys(Password)
time.sleep(2)

Button = driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-layout/div[1]/div[1]/div/div/div/div/div/worklenz-signup/nz-spin/div/form/button[1]")
Button.click()
time.sleep(5)

act_title = driver.title
exp_title = "Worklenz | Setup your account"
if act_title==exp_title:
    print("sign up is success")
else:
    print("sign up is failed")

time.sleep(5)

driver.close()