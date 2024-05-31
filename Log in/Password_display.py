import time        ####  NOT COMPLETE , HAVE ERRROR  ####

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.app.worklenz.com/auth/login")
time.sleep(5)
driver.maximize_window()

show_password = driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-layout/div[1]/div[1]/div/div/div/div/div/worklenz-login/form/nz-form-item[2]/nz-form-control/div/div/nz-input-group/span[2]")

def notselected():
    print("show password display: ", show_password.is_displayed())
    print("show password: ", show_password.is_selected())
    time.sleep(2)
def selected():
    show_password.click()
    print("show password:",show_password.is_selected())
    time.sleep(3)

notselected()
selected()

driver.quit()