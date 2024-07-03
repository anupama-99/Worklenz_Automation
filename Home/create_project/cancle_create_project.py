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


def test_create_project_from_templete():
    dropdown_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='anticon anticon-down']//*[name()='svg']")))
    dropdown_button.click()

    import_templete_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//li[@class='ant-dropdown-menu-item']")))
    import_templete_button.click()

    templete = wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='ant-drawer ant-drawer-right ng-star-inserted ant-drawer-open']//div[@class='ant-drawer-header ng-star-inserted']")))


def test_cancle_project():
    cancle_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Cancel']")))
    cancle_button.click()

