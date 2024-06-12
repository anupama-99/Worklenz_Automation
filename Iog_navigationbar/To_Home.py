import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://uat.app.worklenz.com/auth/login")
time.sleep(5)
driver.maximize_window()

email = "anupamaudeshani1999@gmail.com"
password = "#18Apc.3619#"

def login():
    emailbox = driver.find_element(By.XPATH,"//input[@placeholder='Email']")
    emailbox.send_keys(email)
    passwordbox = driver.find_element(By.XPATH,"//input[@placeholder='Password']")
    passwordbox.send_keys(password)
    loginbutton = driver.find_element(By.XPATH,"//button[@class='ant-btn mt-1 ant-btn-primary ant-btn-lg ant-btn-block']")
    loginbutton.click()
    time.sleep(5)

def home():
    homebutton = driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-layout/nz-spin/div/nz-layout/nz-header/worklenz-header/div[2]/ul/li[1]/strong")
    homebutton.click()
    time.sleep(5)
    print(driver.title)

def verify():
    act_title = driver.title
    exep_title = "Worklenz | Home"
    if act_title == exep_title:
        print("In home")
    else:
        print("error")

login()
home()
verify()

driver.quit()
