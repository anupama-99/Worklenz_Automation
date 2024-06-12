                               ###     Done       ###
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

wait = WebDriverWait(driver,10)

driver.get("https://uat.worklenz.com/")
driver.maximize_window()

def template():
    features = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Features']")))
    Template = driver.find_element(By.XPATH,"//a[normalize-space()='Templates']")
    features.click()
    Template.click()

    wait.until(EC.title_is("Templates | Worklenz"))

def verify():
    act_title = driver.title
    exep_title = "Templates | Worklenz"
    if act_title == exep_title:
        print("In template page")
    else:
        print("Not in templates page")

template()
verify()

driver.quit()
