import time         ####NOT COMPLETE , HAVE ERRROR  ####

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.app.worklenz.com/auth/signup")
time.sleep(5)
driver.maximize_window()

show_password = driver.find_element(By.XPATH,"//*[name()='path' and contains(@d,'M942.2 486')]")

def notselected():
    print("show password display: ", show_password.is_displayed())
    print("show password: ", show_password.is_selected())
    time.sleep(2)

def selected():
    show_password.click()
    print("show password:",show_password.is_selected())
    time.sleep(3)

notselected()
selected()

driver.quit()
