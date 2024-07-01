import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Login_function  # Import the login function

# Set up WebDriver and WebDriverWait
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Open the login page
driver.get("https://uat.app.worklenz.com/auth/login")
driver.maximize_window()

# Call the login function
Login_function.login(driver, wait)

def test_enter_project():
    project_button = wait.until(EC.presence_of_element_located((By.XPATH,"//ul[@class='top-nav-ul-main ant-menu ant-menu-root ant-menu-light ant-menu-horizontal']//strong[@class='ng-star-inserted'][normalize-space()='Projects']")))
    project_button.click()
    time.sleep(5)

    # check title is correct
    act_title = driver.title
    exep_title = "Worklenz | Projects"
    print(driver.title)
    assert act_title == exep_title ,"not enter projects"


