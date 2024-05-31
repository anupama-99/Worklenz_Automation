import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.worklenz.com/")
driver.implicitly_wait(10)
time.sleep(5)
driver.maximize_window()

# to administrator
driver.find_element(By.XPATH,"//span[normalize-space()='Capabilities']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Project Managers']").click()
time.sleep(10)

def verify():
    act_title = driver.title
    exep_title = "Managers | Worklenz"
    if act_title == exep_title:
        print("In project managers page")
    else:
        print("Not in project managers page")

verify()

driver.quit()