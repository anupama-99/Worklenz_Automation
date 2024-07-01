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

def test_logout_from_alert_using_X_button():
    profile = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "/html/body/worklenz-root/worklenz-layout/nz-spin/div/nz-layout/nz-header/worklenz-header/div[2]/div[2]/div[2]/ul/li[5]")))
    profile.click()
    time.sleep(5)

    logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@class='pl-def pr-def ant-menu-item']")))
    logout_button.click()

    X_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='anticon ant-modal-close-icon anticon-close ng-star-inserted']//*[name()='svg']")))
    X_button.click()

def test_logout():
    profile = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "/html/body/worklenz-root/worklenz-layout/nz-spin/div/nz-layout/nz-header/worklenz-header/div[2]/div[2]/div[2]/ul/li[5]")))
    profile.click()
    time.sleep(5)

    logout_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//li[@class='pl-def pr-def ant-menu-item']")))
    logout_button.click()

    # alert = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='ant-modal-body ng-tns-c3428272058-134']")))
    # assert alert.is_displayed() , "logout alert is not displayed"


