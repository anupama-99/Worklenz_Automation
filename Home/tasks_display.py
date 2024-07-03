import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import Login_function  # Import the login function

driver = webdriver.Chrome()
driver.get("https://uat.app.worklenz.com/auth/login")
wait = WebDriverWait(driver, 10)
driver.maximize_window()

# Call the login function from imported module
Login_function.login(driver, wait)

def test_see_list_tasks():
    list_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[normalize-space()='List']")))
    list_button.click()

def test_see_calander_tasks():
    calander_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[normalize-space()='Calendar']")))
    calander_button.click()