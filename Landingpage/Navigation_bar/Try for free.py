import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.worklenz.com/")
time.sleep(5)
driver.maximize_window()

def Tryforfree():
    tryforfree_button = driver.find_element(By.XPATH,"//span[normalize-space()='Try for Free']")
    tryforfree_button.click()
    print(driver.title)

def verify():
    act_title = driver.title
    exep_title = "Worklenz | Signup"
    if act_title == exep_title:
        print("successful")
    else:
        print("Not successful")


Tryforfree()
verify()

driver.quit()