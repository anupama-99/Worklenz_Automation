import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://app.worklenz.com/auth/login")
time.sleep(5)
driver.maximize_window()