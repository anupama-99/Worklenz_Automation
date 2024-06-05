                                  ###    Done     ###
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)

driver.get("https://uat.worklenz.com/")
driver.maximize_window()

def login():
    loginbutton = driver.find_element(By.XPATH,"//a[@class='text-sm px-2 py-1 transition focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-blue-500 focus-visible:outline-none focus-visible:shadow-outline-blue rounded-full']")
    loginbutton.click()
    wait.until(EC.title_is("Worklenz | Login"))

def verify():
    act_title = driver.title
    exep_title = "Worklenz | Login"
    if act_title == exep_title:
        print("successful")
    else:
        print("Not successful")


login()
verify()

driver.quit()