                                   ###     Done      ###
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

wait = WebDriverWait(driver,10)

driver.get("https://uat.worklenz.com/")
driver.maximize_window()

def timetraking():
    features = wait.until(EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='Features']")))
    timetracking = driver.find_element(By.XPATH,"//a[normalize-space()='Time Tracking']")
    features.click()
    timetracking.click()

    wait.until(EC.title_is("Time Tracking | Worklenz"))


def verify():
    act_title = driver.title
    exep_title = "Time Tracking | Worklenz"
    if act_title == exep_title:
        print("In time tracking page")
    else:
        print("Not in time tracking page")

timetraking()
verify()

driver.quit()
