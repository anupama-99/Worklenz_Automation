import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.worklenz.com/")
driver.implicitly_wait(10)
driver.maximize_window()

# To time tracking
features = driver.find_element(By.XPATH,"//span[normalize-space()='Features']")
task_mng = driver.find_element(By.XPATH,"//a[normalize-space()='Task Management']")

features.click()
task_mng.click()
time.sleep(5)

def verify():
    act_title = driver.title
    exep_title = "Task Management | Worklenz"
    if act_title == exep_title:
        print("In task management page")
    else:
        print("Not in task management page")

verify()

driver.quit()
