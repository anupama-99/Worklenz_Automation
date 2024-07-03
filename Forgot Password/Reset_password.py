import time

from selenium import webdriver                                      ###### NOT COMPLETE ###
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.app.worklenz.com/auth/login")
time.sleep(5)
driver.maximize_window()

time.sleep(2)

email="wanigasooriyaanupama99@gmail.com"
Password = "Auw06*NO"

def forgot_password():
    forgot_password = driver.find_element(By.CLASS_NAME,"login-form-forgot")
    forgot_password.click()

    print(driver.title)

def reset():
    Email = driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-reset-password/div/div/div/div/div/div/div/div[2]/div[2]/form/nz-form-item/nz-form-control/div/div/nz-input-group/input")
    Email.send_keys("wanigasooriyaanupama99@gmail.com")

    Reset_button = driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-reset-password/div/div/div/div/div/div/div/div[2]/div[2]/form/button[1]")
    Reset_button.click()

time.sleep(3)
print(driver.title)
def confirm_process():
    Confirm_msg = driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-reset-password/div/div/div/div/div/div/div/nz-result/div[2]")
    print(Confirm_msg.text)

def enter_email():
    driver.get("https://mail.google.com")
    email_input = driver.find_element(By.NAME,"identifier")
    email_input.send_keys(email)
    time.sleep(2)

forgot_password()
reset()
confirm_process()
enter_email()