                               ###     Done       ###
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

wait = WebDriverWait(driver,10)

driver.get("https://uat.worklenz.com/")
driver.maximize_window()

def task_mng():
    features = wait.until(EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='Features']")))
    task_mng = driver.find_element(By.XPATH,"//a[normalize-space()='Task Management']")
    features.click()
    task_mng.click()

    wait.until(EC.title_is("Task Management | Worklenz"))

def verify():
    act_title = driver.title
    exep_title = "Task Management | Worklenz"
    if act_title == exep_title:
        print("In task management page")
    else:
        print("Not in task management page")

task_mng()
verify()


driver.quit()
