import time

from selenium import webdriver

driver = webdriver.Chrome()


driver.get("https://app.worklenz.com/auth/login")
time.sleep(5)