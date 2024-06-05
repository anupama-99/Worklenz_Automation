                               ###     Done     ###
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

wait = WebDriverWait(driver,10)
driver.get("https://uat.worklenz.com/")
driver.maximize_window()

def resource_mng():
    features = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Features']")))
    res_mng = driver.find_element(By.XPATH,"//a[normalize-space()='Resource Management']")
    features.click()
    res_mng.click()

    wait.until(EC.title_is("Resource Management | Worklenz"))

def verify():
    act_title = driver.title
    exep_title = "Resource Management | Worklenz"
    if act_title == exep_title:
        print("In resource management page")
    else:
        print("Not in resource management page")

resource_mng()
verify()

driver.quit()
