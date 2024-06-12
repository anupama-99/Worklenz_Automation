                                   ###    Done    ###
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)

driver.get("https://uat.worklenz.com/")
driver.maximize_window()


# to capabilities
capability = (driver.find_element(By.XPATH,"//span[normalize-space()='Capabilities']"))
capability.click()

def verify():
    # wait 10 seconds before looking for element
    cap_item =wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/header/div/div/nav/ul/li[2]/menu/div/div")))
    print(cap_item.text)

verify()

driver.quit()

