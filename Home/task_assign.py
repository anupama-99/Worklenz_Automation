import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import Login_function  # Import the login function

driver = webdriver.Chrome()
driver.get("https://uat.app.worklenz.com/auth/login")
wait = WebDriverWait(driver,10)
driver.maximize_window()
# Call the login function from the imported module
Login_function.login(driver,wait)

def test_task_assign_to_me():
       assgin_tasks = wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/worklenz-root/worklenz-layout/nz-spin/div/nz-layout/nz-layout/nz-content/div/worklenz-dashboard/div/div/div[2]/div/div[1]/div/worklenz-my-tasks/div[1]/div/nz-space/div[2]/nz-select")))
       assgin_tasks.click()

       assign_to_me = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(text(),'assigned to me')]")))
       assign_to_me.click()
       time.sleep(5)

def test_task_assign_by_me():
       assgin_tasks = wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/worklenz-root/worklenz-layout/nz-spin/div/nz-layout/nz-layout/nz-content/div/worklenz-dashboard/div/div/div[2]/div/div[1]/div/worklenz-my-tasks/div[1]/div/nz-space/div[2]/nz-select")))
       assgin_tasks.click()


       assgin_by_me = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[normalize-space()='assigned by me']")))
       assgin_by_me.click()
       time.sleep(5)