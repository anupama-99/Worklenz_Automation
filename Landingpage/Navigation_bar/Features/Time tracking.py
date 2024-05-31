import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.worklenz.com/")
driver.implicitly_wait(10)
driver.maximize_window()

# To time tracking
features = driver.find_element(By.XPATH,"//span[normalize-space()='Features']")
timetracking = driver.find_element(By.XPATH,"//a[normalize-space()='Time Tracking']")

features.click()
timetracking.click()
time.sleep(5)

def verify():
    act_title = driver.title
    exep_title = "Time Tracking | Worklenz"
    if act_title == exep_title:
        print("In time tracking page")
    else:
        print("Not in time tracking page")

verify()

driver.quit()
