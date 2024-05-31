import time

from selenium import webdriver                              ### GO TO PAGE. BUT PRINT UNSCESSFULL ###
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.app.worklenz.com/auth/signup")
time.sleep(5)
driver.maximize_window()

def privacy():
    privacylink = driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-layout/div[1]/div[1]/div/div/div/div/div/worklenz-signup/nz-spin/div/form/nz-form-item[4]/nz-form-control/div/div/p/a[1]")
    privacylink.click()
    time.sleep(10)
    print(driver.title)


privacy()
time.sleep(10)
