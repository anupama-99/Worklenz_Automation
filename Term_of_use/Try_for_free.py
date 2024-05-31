import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://uat.app.worklenz.com/terms-of-use")

button = driver.find_element(By.XPATH,"//*[@id='navbarSupportedContent']/div/a[2]/button")
button.click()
print(driver.title)