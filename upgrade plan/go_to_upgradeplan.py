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

def test_enter_upgradeplan():
    upgrade_plan = wait.until(EC.presence_of_element_located((By.XPATH,"//a[@class='ng-star-inserted']")))
    upgrade_plan.click()
    time.sleep(5)

    # check title is correct
    act_title = driver.title
    exep_title = "Worklenz"
    print(driver.title)
    assert act_title == exep_title ,"Not enter to the upgrade plan"

    # #check billing button is selected
    # billing_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//li[@class='rounded-4 ant-menu-submenu ant-menu-submenu-vertical ant-menu-item-selected ant-menu-submenu-active ant-menu-submenu-open']//div[@class='ant-menu-submenu-title']")))
    # assert billing_button.is_selected(), "not in billing section"


