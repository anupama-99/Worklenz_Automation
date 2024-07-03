# tasks due statushttps://uat.app.worklenz.com/auth/login
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import Login_function  # Import the login function

driver = webdriver.Chrome()
driver.get("")
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10)
driver.maximize_window()

# Call the login function from imported module
Login_function.login(driver, wait)

def test_see_all_asks():
    all_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//body/worklenz-root/worklenz-layout[@class='ng-star-inserted']/nz-spin[@class='ant-spin-nested-loading']/div[@class='ant-spin-container ng-star-inserted']/nz-layout[@class='ant-layout layout']/nz-layout[@class='ant-layout']/nz-content[@class='ant-layout-content']/div[@class='inner-content']/worklenz-dashboard[@class='ng-star-inserted']/div[@class='container-fluid']/div[@class='my-dashboard mx-auto']/div[@class='dahsboard-content']/div[@class='ant-row']/div[@class='gutter-row ant-col ant-col-16']/div[@class='dashboard-main-card tasks-card']/worklenz-my-tasks/div[@class='card-data mb-3']/nz-skeleton[@class='ant-skeleton ant-skeleton-active ng-star-inserted']/nz-tabset[@class='ant-tabs mob-overflow ant-tabs-card ant-tabs-top ant-tabs-default ng-star-inserted']/nz-tabs-nav[@role='tablist']/div[@class='ant-tabs-nav-wrap']/div[@class='ant-tabs-nav-list']/div[1]")))
    all_button.click()
    time.sleep(3)

def test_see_today_tasks():
    today_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//nz-tabs-nav[@role='tablist']//div[2]")))
    today_button.click()
    time.sleep(3)

def test_see_upcoming_tasks():
    upcoming_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//nz-tabs-nav[@role='tablist']//div[3]")))
    upcoming_button.click()
    time.sleep(3)

def test_see_overdue_tasks():
    overdue_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//nz-tabs-nav[@role='tablist']//div[4]")))
    overdue_button.click()
    time.sleep(3)


def test_see_noduedate_tasks():
    noduedate_button =wait.until(EC.element_to_be_clickable((By.XPATH,"//nz-tabs-nav[@role='tablist']//div[5]")))
    noduedate_button.click()
    time.sleep(3)



