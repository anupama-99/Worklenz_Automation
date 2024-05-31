import time         ####    not working    ####

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://uat.app.worklenz.com/terms-of-use")

driver.find_element(By.XPATH,"/html/body/footer/div/div[1]/div[2]/ul/li[1]/a").click()
print(driver.title)

