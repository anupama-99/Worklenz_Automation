import time
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import Login_function

driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)

# Open the login page
driver.get("https://uat.app.worklenz.com/auth/login")
driver.maximize_window()

## call Login function
Login_function.login(driver,wait)

def test_goto_profile():
    profile = wait.until(EC.element_to_be_clickable((
        By.XPATH,"/html/body/worklenz-root/worklenz-layout/nz-spin/div/nz-layout/nz-header/worklenz-header/div[2]/div[2]/div[2]/ul/li[5]")))
    profile.click()


def test_goto_settings():
    settings = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/worklenz-root/worklenz-layout/nz-spin/div/nz-layout/nz-header/worklenz-header/div[2]/div[2]/div[2]/ul/div/div[3]/ul/li[2]")))
    settings.click()