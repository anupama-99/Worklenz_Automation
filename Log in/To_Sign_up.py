import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.app.worklenz.com/auth/login")
time.sleep(5)
driver.maximize_window()

time.sleep(3)

def To_sign_up():
    To_sign_up = driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-layout/div[1]/div[1]/div/div/div/div/div/worklenz-login/form/nz-form-item[4]/nz-form-control/div/div/p/a")
    To_sign_up.click()

time.sleep(10)

To_sign_up()

print(driver.title)