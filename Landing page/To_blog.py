import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://worklenz.com/")
time.sleep(3)
driver.maximize_window()

def free():
    try_for_free_button = driver.find_element(By.XPATH,"/html/body/header/nav/div/div/div[2]/div[2]/a")
    try_for_free_button.click()

    time.sleep(3)

def verify():
    act_title = driver.title
    exp_title = "Worklenz | Signup"
    if act_title==exp_title:
        print("Enter signup page success")
    else:
        print("Enter signup page failed")

    time.sleep(3)

free()
verify()

driver.close()