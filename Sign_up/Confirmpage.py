import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.app.worklenz.com/auth/signup")
time.sleep(5)
driver.maximize_window()

def confirm():
    signup = driver.find_element(By.CLASS_NAME,"text-muted").text
    print(signup)
    text = "Create your account."
    if signup == text:
        print("successfully in page")
    else:
        print("unsuccessfull")

confirm()
driver.close()
