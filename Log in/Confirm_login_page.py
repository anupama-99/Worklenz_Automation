import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.app.worklenz.com/auth/login")
time.sleep(5)
driver.maximize_window()

def confirm_login():
    page = driver.find_element(By.CLASS_NAME,"text-muted").text
    text = "Log Into your account."
    if page == text:
        print("In login page")
    else:
        print("Not in login page")

confirm_login()

driver.quit()