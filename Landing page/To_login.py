import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://worklenz.com/")
time.sleep(5)
driver.maximize_window()

def login_button():
    login_button = driver.find_element(By.XPATH,"/html/body/header/nav/div/div/div[3]/div/div/div/div[1]/a")
    login_button.click()

    time.sleep(3)

def verify():
    act_title = driver.title
    exp_title = "Worklenz | Login"
    if act_title==exp_title:
        print("Enter login page success")
    else:
        print("Enter login page failed")

    time.sleep(3)

login_button()
verify()

driver.close()