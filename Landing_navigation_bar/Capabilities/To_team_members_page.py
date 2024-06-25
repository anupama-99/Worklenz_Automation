                             ###     Done     ###
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

wait = WebDriverWait(driver,10)

driver.get("https://uat.worklenz.com/")
driver.maximize_window()

def team_memb():
    capabilities = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Capabilities']")))
    team = driver.find_element(By.XPATH,"//a[normalize-space()='Team Members']")
    capabilities.click()
    team.click()

    wait.until(EC.title_is("Analytics_page | Worklenz"))

def verify():
    act_title = driver.title
    exep_title = "Analytics_page | Worklenz"
    if act_title == exep_title:
        print("In Team member page")
    else:
        print("Not in Team member page")

team_memb()
verify()

driver.quit()