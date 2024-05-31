import time
                            #       not mouse hover work         ###
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.worklenz.com/")
driver.implicitly_wait(10)
time.sleep(5)
driver.maximize_window()

# to administrator
# first way
driver.find_element(By.XPATH,"//span[normalize-space()='Capabilities']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Team Members']").click()
time.sleep(10)

# #second way
# capabilities = driver.find_element(By.XPATH,"//span[normalize-space()='Capabilities']")
# team_members = driver.find_element(By.XPATH,"//a[normalize-space()='Team Members']")
# #mouse hover
# act = ActionChains(driver)
# act.move_to_element(capabilities).move_to_element(team_members).click().perform()
# time.sleep(5)

def verify():
    act_title = driver.title
    exep_title = "Analytics | Worklenz"
    if act_title == exep_title:
        print("In Team member page")
    else:
        print("Not in Team member page")

verify()

driver.quit()