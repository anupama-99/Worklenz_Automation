
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

email = "anupamabb4@gmail.com"
password = "#18Apc.3619#"

def login(driver, wait):
    emailbox = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/worklenz-root/worklenz-layout/div[1]/div[1]/div/div/div/div/div/worklenz-login/form/nz-form-item[1]/nz-form-control/div/div/nz-input-group/input")))
    emailbox.send_keys(email)

    passwordbox = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/worklenz-root/worklenz-layout/div[1]/div[1]/div/div/div/div/div/worklenz-login/form/nz-form-item[2]/nz-form-control/div/div/nz-input-group/input")))
    passwordbox.send_keys(password)

    loginbutton = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/worklenz-root/worklenz-layout/div[1]/div[1]/div/div/div/div/div/worklenz-login/form/button[1]")))
    loginbutton.click()
    time.sleep(5)
