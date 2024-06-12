                            ###      Done          ###
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

wait = WebDriverWait(driver,10)

driver.get("https://uat.worklenz.com/")
driver.maximize_window()

def project_overview():
    try_now_button = wait.until(EC.visibility_of_element_located((By.XPATH,"//body/div[@class='max-w-screen-xl mx-auto px-5']/div[4]/div[2]/div[1]/div[1]/a[1]//*[name()='svg']")))
    try_now_button.click()

    print(driver.title)

def verify_project_overview_try_now():
    act_title = driver.title
    exp_title = "Worklenz | Signup"
    if act_title == exp_title:
        print("successfully")
    else:
        print("unsuccessfull")

project_overview()
verify_project_overview_try_now()

driver.quit()