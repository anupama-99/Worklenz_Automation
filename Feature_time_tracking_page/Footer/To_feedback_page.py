                      ###       Done        ###
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

wait = WebDriverWait(driver,10)

driver.get("https://uat.worklenz.com/time-tracking/")
driver.maximize_window()

def feedback():
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/footer")))
    feedback_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Feedback']")))
    feedback_text.click()
    wait.until(EC.title_is("Public | worklenz"))

def verify():
    act_title =driver.title
    exp_title = "Public | worklenz"
    if act_title == exp_title:
        print("In feedback page")
    else:
        print("Not in feedback page")

feedback()
verify()

driver.quit()