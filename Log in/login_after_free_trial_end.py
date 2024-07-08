import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Set up WebDriver and WebDriverWait
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Open the login page
driver.get("https://uat.app.worklenz.com/auth/login")
driver.maximize_window()

email = "anupamaudeshani1999@gmail.com"
password = "#18Apc.3619#"

def test_login():
    emailbox = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/worklenz-root/worklenz-layout/div[1]/div[1]/div/div/div/div/div/worklenz-login/form/nz-form-item[1]/nz-form-control/div/div/nz-input-group/input")))
    emailbox.send_keys(email)

    passwordbox = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/worklenz-root/worklenz-layout/div[1]/div[1]/div/div/div/div/div/worklenz-login/form/nz-form-item[2]/nz-form-control/div/div/nz-input-group/input")))
    passwordbox.send_keys(password)

    loginbutton = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/worklenz-root/worklenz-layout/div[1]/div[1]/div/div/div/div/div/worklenz-login/form/button[1]")))
    loginbutton.click()
    time.sleep(5)

def test_upgrade_now_button():
    button = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/worklenz-root/worklenz-layout/nz-spin/div/nz-layout/nz-layout/nz-content/div/worklenz-license-expired/nz-result/div[4]/button/span")))
    button.click()

    upgrade_plan = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Upgrade Plan')]")))
    upgrade_plan.click()

def test_change_seats():
    seats_choose_button = wait.until(EC.presence_of_element_located((By.ID,"seats")))
    seats_choose_button.click()

    amount = wait.until(EC.element_to_be_clickable((By.XPATH,"//nz-option-item[@title='4']")))
    amount.click()

def test_upgrade_plan_forfree():

    free_plan_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='cdk-overlay-3']/nz-modal-container/div/div/div/div/div[2]/div[1]/nz-card")))
    free_plan_button.click()

    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    try_for_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='ant-btn mt-3 mb-2 ant-btn-primary ant-btn-lg ng-star-inserted']")))
    try_for_button.click()


##############################   error ###########################################
# def test_upgrade_plan_for_monthly():
#
#     monthly_plan_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='cdk-overlay-4']/nz-modal-container/div/div/div/div/div[2]/div[2]/nz-card")))
#     monthly_plan_button.click()
#
#     driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#
#     purchase_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Continue with Pro - Annual']")))
#     purchase_button.click()

# def test_upgrade_plan_for_annual():
#
#     anuual_plan_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='cdk-overlay-4']/nz-modal-container/div/div/div/div/div[2]/div[3]/nz-card")))
#     anuual_plan_button.click()
#     time.sleep(5)
#
#     purchase_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='ant-btn mt-3 mb-2 ant-btn-primary ant-btn-lg ng-star-inserted']")))
#     purchase_button.click()








