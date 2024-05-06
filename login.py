# 1)Open web Browser
# 2)Open URL to Login page
# 3)Enter Email
# 4)Enter Password
# 5) CLick on login
# 6) Capture title of the home page (actual title)
# 7) Verify title of the Page
# 8) Close browser


import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://app.worklenz.com/auth/login")
time.sleep(5)
driver.maximize_window()

email = "wanigasooriyaanupama99@gmail.com"
password = "#18Apc.3619#"

driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-layout/div[1]/div[1]/div/div/div/div/div/worklenz-login/form/nz-form-item[1]/nz-form-control/div/div/nz-input-group/input").send_keys(email)
driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-layout/div[1]/div[1]/div/div/div/div/div/worklenz-login/form/nz-form-item[2]/nz-form-control/div/div/nz-input-group/input").send_keys(password)
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-layout/div[1]/div[1]/div/div/div/div/div/worklenz-login/form/button[1]").click()
time.sleep(5)


act_title = driver.title
exp_title = "Worklenz | Home"
if act_title==exp_title:
    print("login is success")
else:
    print("login is failed")

Name = driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-layout/nz-spin/div/nz-layout/nz-layout/nz-content/div/worklenz-dashboard/div/div/div[1]/div[1]/nz-space/div/h3")
text = Name.text
print(text)

time.sleep(5)

driver.close()




