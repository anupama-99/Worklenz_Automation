import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://uat.app.worklenz.com/privacy-policy")

def pricing():
    pricing_button = driver.find_element(By.XPATH,"//*[@id='navbarSupportedContent']/ul/li[3]/a")
    pricing_button.click()
    time.sleep(10)
    print(driver.title)

pricing()












