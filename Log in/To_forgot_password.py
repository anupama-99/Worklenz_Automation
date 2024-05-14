import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.app.worklenz.com/auth/login")
time.sleep(5)
driver.maximize_window()

time.sleep(2)

def forgot_password():
    forgot_password = driver.find_element(By.CLASS_NAME,"login-form-forgot")
    forgot_password.click()

time.sleep(3)

forgot_password()
print(driver.title)
