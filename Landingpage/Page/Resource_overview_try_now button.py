                           ###      Done          ###
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

wait = WebDriverWait(driver,10)

driver.get("https://uat.worklenz.com/")
driver.maximize_window()

def resource_overview():
    try_now_button =wait.until(EC.visibility_of_element_located((By.XPATH,"//body/div[@class='max-w-screen-xl mx-auto px-5']/div[3]/div[2]/div[1]/div[1]/a[1]/span[1]")))
    try_now_button.click()

    print(driver.title)

def verify_try_now():
    act_title = driver.title
    exp_title = "Worklenz | Signup"
    if act_title == exp_title:
        print("successfully")
    else:
        print("unsuccessfull")

resource_overview()
verify_try_now()

driver.quit()