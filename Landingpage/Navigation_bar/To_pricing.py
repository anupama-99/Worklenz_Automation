import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.worklenz.com/")
driver.implicitly_wait(10)
time.sleep(5)
driver.maximize_window()

def pricing():
    pricing_button = driver.find_element(By.XPATH,"//a[normalize-space()='Pricing']")
    pricing_button.click()
    time.sleep(20)
    print(driver.title)

def verify():
    act_title = driver.title
    exep_title = "Pricing | Worklenz"
    if act_title == exep_title:
        print("successful")
    else:
        print("not successful")


pricing()
verify()

driver.quit()