import time
                       ###       not mouse hover work         ###
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.worklenz.com/")
# driver.implicitly_wait(10)
time.sleep(5)
driver.maximize_window()

# to administrator
# 1 way
driver.find_element(By.XPATH,"//span[normalize-space()='Capabilities']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[normalize-space()='Administrators']").click()
time.sleep(5)

# # 2 way
# capabilities = driver.find_element(By.XPATH,"//span[normalize-space()='Capabilities']")
# admistrator = driver.find_element(By.XPATH,"//a[normalize-space()='Administrators']")
# act = ActionChains(driver)
# act.move_to_element(capabilities).move_to_element(admistrator).click().perform()

def verify():
    act_title = driver.title
    exep_title = "Admin | Worklenz"
    if act_title == exep_title:
        print("In admin page")
    else:
        print("Not in admin page")

verify()

driver.quit()
