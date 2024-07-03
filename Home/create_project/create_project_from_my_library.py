import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
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

def test_create_project_from_templete():
    dropdown_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='ant-btn ant-dropdown-trigger ant-btn-primary ant-btn-icon-only']")))
    dropdown_button.click()

    import_templete_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//li[@class='ant-dropdown-menu-item']")))
    import_templete_button.click()

    templete = wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='ant-drawer ant-drawer-right ng-star-inserted ant-drawer-open']//div[@class='ant-drawer-header ng-star-inserted']")))

def test_my_library():
    my_library_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//nz-tabset[@class='ant-tabs ant-tabs-card ant-tabs-top ant-tabs-default ng-star-inserted']//div[@class='ant-tabs-tab ng-star-inserted']")))
    my_library_button.click()
    time.sleep(5)

def test_search_for_library():
    search = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='Search by template name']")))
    search.send_keys("Education")
    search.send_keys(Keys.ENTER)
    time.sleep(10)

def test_create_project():
    creat_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@nztype='primary']")))
    creat_button.click()


