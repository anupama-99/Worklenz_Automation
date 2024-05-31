import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.app.worklenz.com/auth/signup")
time.sleep(5)
driver.maximize_window()

def terms():
    termslink = driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-layout/div[1]/div[1]/div/div/div/div/div/worklenz-signup/nz-spin/div/form/nz-form-item[4]/nz-form-control/div/div/p/a[2]")
    termslink.click()
    print(driver.title)

def confireterm():
    act_title = "Worklenz | Terms of Use"
    exp_title = driver.title
    if act_title == exp_title:
        print("Successfully enter to terms page")
    else:
        print("unsccessful enter to terms page")

terms()
confireterm()

driver.quit()