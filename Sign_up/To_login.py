import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.app.worklenz.com/auth/signup")
time.sleep(5)
driver.maximize_window()

def log_in():
    login_button = driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-layout/div[1]/div[1]/div/div/div/div/div/worklenz-signup/nz-spin/div/form/nz-form-item[6]/nz-form-control/div/div/p/a")
    login_button.click()
    print(driver.title)

log_in()

time.sleep(5)