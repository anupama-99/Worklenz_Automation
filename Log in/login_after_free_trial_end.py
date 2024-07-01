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

def test_upgrade_plan_forfree():
    upgrade_plan = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Upgrade Plan')]")))
    upgrade_plan.click()

    free_plan_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[normalize-space()='Free']")))
    free_plan_button.click()
    time.sleep(5)

    try_it_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='ant-btn w-100 mt-3 mb-2 ant-btn-primary']")))
    try_it_button.click()

    # #Chech free plan activate is suceess
    # notification = driver.find_element(By.XPATH,"//*[@id='cdk-overlay-8']/nz-notification-container/div[2]/nz-notification")
    # assert notification.is_displayed()

##############################   error ###########################################
def test_upgrade_plan_for_monthly():
    upgradeplan = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Upgrade Plan')]")))
    upgradeplan.click()

    monthly_plan_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[normalize-space()='Monthly']")))
    monthly_plan_button.click()
    time.sleep(10)

    purchase_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='ant-btn w-100 mt-3 mb-2 ant-btn-primary']")))
    purchase_button.click()


def test_upgrade_plan_for_annual():
    upgrade_plan = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Upgrade Plan')]")))
    upgrade_plan.click()

    anuual_plan_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(text(),'Annually')]")))
    anuual_plan_button.click()
    time.sleep(5)

    purchase_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Purchase']")))
    purchase_button.click()

def test_leave_upgrade_plan_types():
    upgradeplan = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Upgrade Plan')]")))
    upgradeplan.click()

    leave_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='anticon ant-modal-close-icon anticon-close ng-star-inserted']//*[name()='svg']")))
    leave_button.click()







