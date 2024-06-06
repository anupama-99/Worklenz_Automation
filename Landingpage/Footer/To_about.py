                                ###       Done        ###
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

wait = WebDriverWait(driver,10)

driver.get("https://uat.worklenz.com/")
driver.maximize_window()

def about():
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/footer")))
    about_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='About']")))
    about_text.click()
    wait.until(EC.title_is("About | Worklenz"))

def verify():
    act_title =driver.title
    exp_title = "About | Worklenz"
    if act_title == exp_title:
        print("In about page")
    else:
        print("Not in about page")

about()
verify()

driver.quit()