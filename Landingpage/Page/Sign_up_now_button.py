                            ######       Done          #######
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)

driver.get("https://uat.worklenz.com/")
driver.maximize_window()

def sign_up():
    sign_up_button = wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@class='rounded-full text-center transition focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-blue-500 focus-visible:outline-none focus-visible:shadow-outline-blue px-7 py-2.5 bg-white text-blue-800 border-2 border-transparent']")))
    sign_up_button.click()

def verify_sign_up_now_button():
    act_title = driver.title
    exp_title = "Worklenz | Signup"
    if act_title == exp_title:
        print("successfully work signupnow button")
    else:
        print("unsuccessfull")


sign_up()
verify_sign_up_now_button()

driver.quit()

