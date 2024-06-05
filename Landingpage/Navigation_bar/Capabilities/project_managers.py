                           ####      Done      ####
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

wait = WebDriverWait(driver,10)

driver.get("https://uat.worklenz.com/")
driver.maximize_window()

def project_mng():
    capabilities = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Capabilities']")))
    project_mng = driver.find_element(By.XPATH,"//a[normalize-space()='Project Managers']")
    capabilities.click()
    project_mng.click()

    wait.until(EC.title_is("Managers | Worklenz"))

def verify():
    act_title = driver.title
    exep_title = "Managers | Worklenz"
    if act_title == exep_title:
        print("In project managers page")
    else:
        print("Not in project managers page")

project_mng()
verify()

driver.quit()