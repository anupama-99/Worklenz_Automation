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

def createproject():
    button = driver.find_element(By.XPATH,"//span[normalize-space()='Create Project']")
    button.click()
    time.sleep(5)

def detail():
    detailsslide = driver.find_element(By.XPATH,"//div[@class='ant-drawer ant-drawer-right ng-star-inserted ant-drawer-open']//span[@class='anticon anticon-close ng-star-inserted']//*[name()='svg']")
    detailsslide.click()
    time.sleep(5)
login()
createproject()
detail()