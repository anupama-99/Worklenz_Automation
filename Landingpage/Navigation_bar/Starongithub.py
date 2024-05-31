
import time

from selenium import webdriver
from selenium.common import ElementNotVisibleException, NoSuchElementException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

wait = WebDriverWait(driver,10)

driver.get("https://uat.worklenz.com/")

time.sleep(5)
driver.maximize_window()

def Starongithub():
    starongithub_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Star us on GitHub']")))

    starongithub_button = driver.find_element(By.XPATH,"//span[normalize-space()='Star us on GitHub']")
    starongithub_button.click()
    time.sleep(20)

Starongithub()
print("in github")

driver.quit()