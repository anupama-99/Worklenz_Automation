# 1)Open web Browser
# 2)Open URL to sign up page
# 3)Enter Full name
# 4)Enter Email
# 5)Enter Password
# 5) CLick on Sign up
# 6) Capture title of the setup account page (actual title)
# 7) Verify title of the Page
# 8) Close browser

           ####         not correct code         ######

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://uat.app.worklenz.com/auth/signup")
time.sleep(5)
driver.maximize_window() # maximize the browser window

Fullname = "W.A.D. Anupama Udeshani"
Email = "anu0709udeshani@gmail.com"
Password ="#18Apc.3619#"

def sign_up():
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

def sign_up_verify():
    act_title = driver.title
    exp_title = "Worklenz | Setup your account"
    if act_title==exp_title:
        print("sign up is success")
    else:
        print("sign up is failed")

def organization():
    org = driver.find_element(By.ID,"FJGRL")
    org.send_keys("setitorg")
    driver.find_element(By.CLASS_NAME,"ng-star-inserted").click()
    print(org)
    print(driver.title)

def project():
    goback_button = driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-account-setup/div[1]/div/div/div[2]/nz-space/div/nz-skeleton/form/div/button[1]/span")
    goback_button.click()     # go to enter organization page
    driver.find_element(By.CLASS_NAME, "ng-star-inserted").click()   # go to enter project page
    project = driver.find_element(By.ID,"BNWGQG").send_keys("myweather")
    driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-account-setup/div[1]/div/div/div[2]/nz-space/div/nz-skeleton/form/div/button[2]/span").click()
    print(project)
    print(driver.title)

def task():
    task = driver.find_element(By.ID,"task-name-input-0")
    task.send_keys("checkweather")
    driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-account-setup/div[1]/div/div/div[2]/nz-space/div/nz-skeleton/form/div[2]/button[2]/span").click()
    print(task)
    print(driver.title)

def teammembers():
    team = driver.find_element(By.ID,"FQV")
    team.send_keys("anubwabt414@gmail.com")
    driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-account-setup/div[1]/div/div/div[2]/nz-space/div/nz-skeleton/form/div/button[3]/span").click()
    print(team)
    print(driver.title)

time.sleep(3)

sign_up()
sign_up_verify()
organization()
project()
task()
teammembers()

driver.close()