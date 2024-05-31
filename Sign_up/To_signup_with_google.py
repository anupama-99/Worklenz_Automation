import time

from selenium import webdriver                                           ### NEED TO LOOK AGAIN  ###
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.app.worklenz.com/auth/signup")
time.sleep(5)
driver.maximize_window()

def signup():
    signup_button = driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-layout/div[1]/div[1]/div/div/div/div/div/worklenz-signup/nz-spin/div/form/button[2]")
    signup_button.click()
    print(driver.title)
    time.sleep(3)

signup()