                              ####     Done      #####
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

wait = WebDriverWait(driver,10)

driver.get("https://uat.worklenz.com/")
driver.maximize_window()

def analysis():
    features = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Features']")))
    analytics = driver.find_element(By.XPATH,"//a[normalize-space()='Analytics_page']")
    features.click()
    analytics.click()

    wait.until(EC.title_is("Analytics_page | Worklenz"))

def verify():
    act_title = driver.title
    exep_title = "Analytics_page | Worklenz"
    if act_title == exep_title:
        print("In analytics page")
    else:
        print("Not in analytics page")

analysis()
verify()

driver.quit()
