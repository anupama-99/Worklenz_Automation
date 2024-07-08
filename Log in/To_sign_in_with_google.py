import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.app.worklenz.com/auth/login")
time.sleep(5)
driver.maximize_window()

time.sleep(2)

def sign_in_google():
    sign_in_google_button = driver.find_element(By.XPATH,"//span[normalize-space()='Sign in with Google']")
    sign_in_google_button.click()
    time.sleep(5)

# def confirm():
#     act_title = "Sign in - Google Accounts"
#     expe_title = driver.title
#
#     if act_title == expe_title:
#         print("Successfull")
#     else:
#         print("unsuccessful")



sign_in_google()



driver.quit()