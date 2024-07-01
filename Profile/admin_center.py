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
    time.sleep(5)
def test_goto_admin_center():
    admin_center = wait.until(EC.element_to_be_clickable((By.XPATH,"//li[@class='ant-menu-item ng-star-inserted']")))
    admin_center.click()
    time.sleep(5)

def test_admincenter_overview():
    overview = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"ant-menu-submenu-title")))
    overview.click()

    #edit organization name
    edit_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='anticon anticon-edit ng-star-inserted']//*[name()='svg']")))
    edit_button.click()

    edit_box = wait.until(EC.element_to_be_clickable((By.XPATH,"//textarea[@class='ant-input ng-star-inserted']")))
    edit_box.clear()
    time.sleep(5)
    edit_box.send_keys("ocean_lanka")

    ################################## not finish ##########################################

