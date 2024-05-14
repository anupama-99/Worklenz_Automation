import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://app.worklenz.com/auth/reset-password")
time.sleep(5)
driver.maximize_window()

time.sleep(2)

email="wanigasooriyaanupama99@gmail.com"
Password = "Auw06*NO"

Email = driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-reset-password/div/div/div/div/div/div/div/div[2]/div[2]/form/nz-form-item/nz-form-control/div/div/nz-input-group/input")
Email.send_keys("wanigasooriyaanupama99@gmail.com")

Reset_button = driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-reset-password/div/div/div/div/div/div/div/div[2]/div[2]/form/button[1]")
Reset_button.click()

time.sleep(3)

print(driver.title)
Confirm_msg = driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-reset-password/div/div/div/div/div/div/div/nz-result/div[2]")
print(Confirm_msg.text)

driver.get("https://mail.google.com")

email_input = driver.find_element(By.NAME,"identifier")
email_input.send_keys(email)
time.sleep(2)

email_button =driver.find_element(By.CLASS_NAME,"VfPpkd-vQzf8d")
email_button.click()
time.sleep(2)

password_input = driver.find_element(By.NAME,"Passwd")
password_input.send_keys(Password)
time.sleep(2)

email_next_button =driver.find_element(By.CLASS_NAME,"VfPpkd-RLmnJb")
email_next_button.click()
time.sleep(2)

print(driver.title)
