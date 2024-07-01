
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

def test_goto_notification():
    notification_button = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/worklenz-root/worklenz-layout/nz-spin/div/nz-layout/nz-header/worklenz-header/div[2]/div[2]/div[2]/ul/li[3]")))
    notification_button.click()

def test_see_read_notifications():
    read_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[normalize-space()='Read']")))
    read_button.click()

def test_see_unread_notifications():
    unread_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[normalize-space()='Unread']")))
    unread_button.click()

def test_leave_notification():
    leave_button = wait.until(EC.element_to_be_clickable(( By.XPATH,"//div[@class='ant-drawer-content-wrapper notifications-drawer']//button[@aria-label='Close']")))
    leave_button.click()


