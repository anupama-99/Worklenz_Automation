                              ###    Done      ###
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

wait = WebDriverWait(driver,10)
driver.get("https://uat.worklenz.com/")
driver.maximize_window()

def admin():

    capabilities = wait.until(EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='Capabilities']")))
    admin = driver.find_element(By.XPATH,"//a[normalize-space()='Administrators']")
    capabilities.click()
    admin.click()

    wait.until(EC.title_is("Admin | Worklenz"))

def verify():
    act_title = driver.title
    exep_title = "Admin | Worklenz"
    if act_title == exep_title:
        print("In admin page")
    else:
        print("Not in admin page")

admin()
verify()

driver.quit()
