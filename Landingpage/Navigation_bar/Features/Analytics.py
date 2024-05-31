import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.worklenz.com/")
driver.implicitly_wait(10)
driver.maximize_window()

# To time tracking
features = driver.find_element(By.XPATH,"//span[normalize-space()='Features']")
analytics = driver.find_element(By.XPATH,"//a[normalize-space()='Analytics']")

features.click()
analytics.click()
time.sleep(5)

def verify():
    act_title = driver.title
    exep_title = "Analytics | Worklenz"
    if act_title == exep_title:
        print("In analytics page")
    else:
        print("Not in analytics page")

verify()

driver.quit()
