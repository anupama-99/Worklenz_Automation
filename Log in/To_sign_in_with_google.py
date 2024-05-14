import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.app.worklenz.com/auth/login")
time.sleep(5)
driver.maximize_window()

time.sleep(2)

sign_in_google_button = driver.find_element(By.CLASS_NAME,"ng-star-inserted")
sign_in_google_button.click()

time.sleep(3)


print(driver.title)