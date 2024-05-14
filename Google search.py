# 1)Open web Browser
# 2)Open URL to google page
# 3)Enter name in search bar
# 4)click to search worklenz
# 5)Click on worklenz tab
# 6) Capture title of the home page (actual title)
# 7) Verify title of the Page
# 8) Close browser

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://google.com")
time.sleep(2)

def search():
    driver.find_element(By.ID,"APjFqb").send_keys("Worklenz")
    time.sleep(1)
    # print(driver.find_elements(By.PARTIAL_LINK_TEXT, "Worklenz"))
    driver.find_element(By.CLASS_NAME, "gNO89b").click()
    time.sleep(5)
    print("Search completed")
    driver.find_element(By.CLASS_NAME,"LC20lb").click()

def verify():
    act_title = driver.title
    exp_title = "Worklenz - From chaos to clarity, more securely"

    if act_title == exp_title:
        print("Log to worklenz landing page")
    else:
        print("Log in failed")

search()
verify()

driver.close()



