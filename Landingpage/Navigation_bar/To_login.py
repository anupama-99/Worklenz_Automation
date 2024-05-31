import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.worklenz.com/")
time.sleep(5)
driver.maximize_window()

def login():
    loginbutton = driver.find_element(By.XPATH,"//a[@class='text-sm px-2 py-1 transition focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-blue-500 focus-visible:outline-none focus-visible:shadow-outline-blue rounded-full']")
    loginbutton.click()
    print(driver.title)

def verify():
    act_title = driver.title
    exep_title = "Worklenz | Login"
    if act_title == exep_title:
        print("successful")
    else:
        print("Not successful")


login()
verify()

driver.quit()