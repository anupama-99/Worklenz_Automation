                                    ###     Done      ###
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)

driver.get("https://uat.worklenz.com/")
driver.maximize_window()

# To feature
features = driver.find_element(By.XPATH,"//span[normalize-space()='Features']")
features.click()

def verify():
    # wait 10 seconds before looking for element
    features = wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/header/div/div/nav/ul/li[1]/menu/div/div/div")))
    print(features.text)

verify()

driver.quit()