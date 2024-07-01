
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Login_function  # Import the login function

# Set up WebDriver and WebDriverWait
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Open the login page
driver.get("https://uat.app.worklenz.com/auth/login")
driver.maximize_window()

# Call the login function
Login_function.login(driver, wait)

def test_add_todo_tasks():
    addtasks = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='card-data']//input[@placeholder='+ Add Task']")))

    #check placeholder is correct
    addtasks_placeholder = addtasks.get_attribute('placeholder')
    # Replace 'Expected Placeholder Text' with the expected placeholder text
    assert addtasks_placeholder == '+ Add Task', f"Expected '+ Add Task' but got '{addtasks_placeholder}'"

    # add tasks
    addtasks.send_keys("get action sea animals health result")

    #verify next step is displayed
    enter_step = wait.until(EC.visibility_of_element_located((By.XPATH,"//b[normalize-space()='Enter']")))
    assert enter_step.is_displayed(),"Not displayed next steps to add task"

    addtasks.send_keys(Keys.ENTER)

def test_refresh_todo_tasks():
    refresh_button = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/worklenz-root/worklenz-layout/nz-spin/div/nz-layout/nz-layout/nz-content/div/worklenz-dashboard/div/div/div[2]/div/div[2]/div[1]/worklenz-personal-tasks/div[1]/div/div/button")))

    table = driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-layout/nz-spin/div/nz-layout/nz-layout/nz-content/div/worklenz-dashboard/div/div/div[2]/div/div[2]/div[1]/worklenz-personal-tasks/div[2]/nz-skeleton/nz-table/nz-spin/div/div/nz-table-inner-default/div/table")

    # Capture initial number of rows
    initial_row_count = len(table.find_elements(By.TAG_NAME,"tr"))

    refresh_button.click()


############    need to correct

# def test_verify_todo_task_add():

# def  test_todo_task_markasdone():
#     mark1 = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"analyst sea animals health")))
#     mark1.click()





