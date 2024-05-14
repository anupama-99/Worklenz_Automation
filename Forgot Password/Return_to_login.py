import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://app.worklenz.com/auth/reset-password")
time.sleep(5)
driver.maximize_window()

time.sleep(2)

def RTL():
    RTL_button = driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-reset-password/div/div/div/div/div/div/div/div[2]/div[2]/form/button[2]")
    RTL_button.click()
    time.sleep(3)

def Print():
    print(driver.title)


RTL()
Print()
