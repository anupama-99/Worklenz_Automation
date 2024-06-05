                                       ###    Done      ###
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 20)

driver.get("https://uat.worklenz.com/")
driver.maximize_window()

def pricing():
    pricing_button = driver.find_element(By.XPATH,"//a[normalize-space()='Pricing']")
    pricing_button.click()
    wait.until(EC.title_is("Pricing | Worklenz"))

def verify():
    act_title = driver.title
    exep_title = "Pricing | Worklenz"
    if act_title == exep_title:
        print("successful")
    else:
        print("not successful")


pricing()
verify()

driver.quit()