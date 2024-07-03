import time        ####  NOT COMPLETE , HAVE ERRROR  ####

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.app.worklenz.com/auth/login")
driver.implicitly_wait(10)
driver.maximize_window()


def show_password():
    email_box = driver.find_element(By.XPATH,"//input[@placeholder='Email']")
    email_box.send_keys("wanigasooriyaanupama99@gmail.com")

    password_box = driver.find_element(By.XPATH,"//input[@placeholder='Password']")
    password_box.send_keys("18Apc.3619#")

# not show password
    show_password = driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-layout/div[1]/div[1]/div/div/div/div/div/worklenz-login/form/nz-form-item[2]/nz-form-control/div/div/nz-input-group/span[2]")
    print("show password display: ", show_password.is_displayed())
    print("show password: ", show_password.is_selected())

# show password
    show_password.click()
    time.sleep(5)
    print("show password:",show_password.is_selected())


show_password()

driver.quit()