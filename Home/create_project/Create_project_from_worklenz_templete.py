
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

def create_project_from_templete():
    dropdown_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='ant-btn ant-dropdown-trigger ant-btn-primary ant-btn-icon-only']")))
    dropdown_button.click()

    import_templete_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//li[@class='ant-dropdown-menu-item']")))
    import_templete_button.click()

    templete = wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='ant-drawer ant-drawer-right ng-star-inserted ant-drawer-open']//div[@class='ant-drawer-header ng-star-inserted']")))

    # worklenz_library = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='cdk-overlay-22']/div/div[2]/div/div/div[2]/nz-tabset/nz-tabs-nav/div/div/div[1]/div")))
    # assert worklenz_library.is_selected(), "worklenz library button is not selected"


# See template one by one
def select_template(index):
    template = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@class='side-menu']//li[{index}]")))
    template.click()

    template_display = wait.until(EC.presence_of_element_located((By.XPATH, f"//*[@id='cdk-overlay-4']/div/div[2]/div/div/div[2]/nz-tabset/div/div/div[1]/worklenz-template-list/div/div[2]/nz-skeleton")))
    assert template_display.is_displayed(), "Template is not displayed"
    time.sleep(2)


# Main function to test creating a project from a template
def test_create_project_from_template():
    create_project_from_templete()

    # Iterate through templates (assume there are 5 templates)
    for i in range(1, 16):
        select_template(i)


#select a specific template
def test_select_specific_template():
    template = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@class='side-menu']//li[7]")))
    template.click()
    time.sleep(5)


def test_create_project():
    create_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@nztype='primary']")))
    create_button.click()
    time.sleep(5)

def test_project():
    project = driver.find_element(By.XPATH,"//ul[@class='top-nav-ul-main ant-menu ant-menu-root ant-menu-light ant-menu-horizontal']//strong[@class='ng-star-inserted'][normalize-space()='Projects']")
    project.click()
    time.sleep(10)






