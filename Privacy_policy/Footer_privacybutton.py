import time
                       ###      not working proplerly      ###
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.app.worklenz.com/privacy-policy")
driver.implicitly_wait(10)

def footerprivacy():
    button = driver.find_element(By.XPATH,"/html/body/footer/div/div[1]/div[2]/ul/li[1]/a")
    button.click()
    print(driver.title)

footerprivacy()