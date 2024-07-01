
import time
from selenium import webdriver
from selenium.webdriver import Keys
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


def test_add_task_name():
    add_task = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@class='ant-input task-name-input-field task-input-default ng-valid ng-star-inserted ng-touched ng-dirty']")))

    # check placeholder is correct
    addtasks_placeholder = add_task.get_attribute('placeholder')
    # Replace 'Expected Placeholder Text' with the expected placeholder text
    assert addtasks_placeholder == '+ Add Task', f"Expected '+ Add Task' but got '{addtasks_placeholder}'"

    add_task.send_keys("check sea animals types")

    # verify next step is displayed
    enter_step = wait.until(EC.visibility_of_element_located((By.XPATH, "//small[@class='ng-star-inserted']")))
    assert enter_step.is_displayed(), "Not displayed next steps to add task"

    add_task.send_keys(Keys.TAB)

def test_add_task_duedate():
    due_date = wait.until(EC.visibility_of_element_located(By.XPATH,"//nz-select-item[@title='No Due Date']"))

    #check title is correct
    act_title = due_date.text
    exep_title = "No Due Date"
    assert act_title == exep_title ,"title is not correct"

    #select due date
    