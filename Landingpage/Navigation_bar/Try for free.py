                                      ###     Done      ###
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

wait = WebDriverWait(driver,10)

driver.get("https://uat.worklenz.com/")
driver.maximize_window()

def Tryforfree():
    tryforfree_button = driver.find_element(By.XPATH,"//span[normalize-space()='Try for Free']")
    tryforfree_button.click()
    wait.until(EC.title_is("Worklenz | Signup"))

def verify():
    act_title = driver.title
    exep_title = "Worklenz | Signup"
    if act_title == exep_title:
        print("successful")
    else:
        print("Not successful")


Tryforfree()
verify()

driver.quit()