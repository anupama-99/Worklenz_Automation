                   ###     Done       ###
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

wait = WebDriverWait(driver,10)

driver.get("https://uat.worklenz.com/")
driver.maximize_window()

def blog():
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/footer")))
    contact_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@class='py-2 text-sm text-slate-600 hover:text-blue-600'][normalize-space()='Blog']")))
    contact_text.click()
    wait.until(EC.title_is("Blog | Worklenz"))

def verify():
    act_title =driver.title
    exp_title = "Blog | Worklenz"
    if act_title == exp_title:
        print("In blog page")
    else:
        print("Not in blog page")

blog()
verify()

driver.quit()