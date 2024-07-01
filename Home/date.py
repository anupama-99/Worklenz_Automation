import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import Login_function  # Import the login function

driver = webdriver.Chrome()
driver.get("https://uat.app.worklenz.com/auth/login")
wait = WebDriverWait(driver,10)
driver.maximize_window()
# Call the login function from the imported module
Login_function.login(driver,wait)

def confirm_date():
    date = driver.find_element(By.XPATH,"//h4[@class='mb-0 ant-typography']")
    print(date.text)


confirm_date()

driver.quit()