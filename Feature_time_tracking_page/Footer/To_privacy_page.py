                                ###    Done      ###
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

wait = WebDriverWait(driver,10)

driver.get("https://uat.worklenz.com/time-tracking/")
driver.maximize_window()

def privacy():
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/footer")))
    privacy_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Privacy']")))
    privacy_text.click()
    wait.until(EC.title_is("Privacy Policy | Worklenz"))

def verify():
    act_title =driver.title
    exp_title = "Privacy Policy | Worklenz"
    if act_title == exp_title:
        print("In privacy page")
    else:
        print("Not in privacy page")

privacy()
verify()

driver.quit()