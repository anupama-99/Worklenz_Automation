import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.app.worklenz.com/auth/login")
time.sleep(5)
driver.maximize_window()

remember_me_button = driver.find_element(By.XPATH, "/html/body/worklenz-root/worklenz-layout/div[1]/div[1]/div/div/div/div/div/worklenz-login/form/div[1]/div[1]/label/span[1]/input")

def notselected():
    print("select status:", remember_me_button.is_selected())
    time.sleep(4)

def selected():   #after select
    remember_me_button.click()
    print("after select status:", remember_me_button.is_selected())
    time.sleep(2)

notselected()
selected()