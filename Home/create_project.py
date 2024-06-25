import select
import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import Login_function  # Import the login function from login_module.py

driver = webdriver.Chrome()
driver.get("https://uat.app.worklenz.com/auth/login")
wait = WebDriverWait(driver, 10)

driver.maximize_window()

# Call the login function from the imported module
Login_function.login(driver, wait)


def create_project():
    # Wait for and click the 'Create Project' button
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Create Project']")))
    button.click()

    # Wait for the 'Create Project' slider to appear
    slider = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='ant-drawer ant-drawer-right ng-star-inserted ant-drawer-open']//div[@class='ant-drawer-body']")))


def enter_name():
    # Enter new project name
    name_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Name']")))
    name_input.send_keys("OMI Game")

def enter_color():
    # Generate the list of XPaths dynamically
    colors_to_select = [f"//li[{i}]//nz-tag[1]" for i in range(1, 25)]

    for color_xpath in colors_to_select:
        # Open color picker
        color_picker = wait.until(EC.element_to_be_clickable((By.XPATH,"//nz-tag[@class='ant-tag ant-dropdown-trigger ms-2 rounded-circle cursor-pointer ant-tag-has-color']")))
        color_picker.click()

        # Select color
        color_option = wait.until(EC.element_to_be_clickable((By.XPATH, color_xpath)))
        color_option.click()
        time.sleep(1)

def status():
    status_type = driver.find_element(By.XPATH,"//nz-select-item[@title='Proposed']")
    status_type.click()

    options = driver.find_elements(By.CLASS_NAME, "cdk-virtual-scroll-content-wrapper")
    time.sleep(5)

    for types in options:
        if types.text == "Cancelled":
            types.click()
            time.sleep(5)
            break


    #//nz-option-item[@title='Cancelled']
    #//nz-option-item[@title='Blocked']
    #//nz-option-item[@title='On Hold']
    #//nz-select-item[@title='Proposed']
    #//nz-select-item[@title='In Planning']
    #//nz-option-item[@title='In Progress']
    #//nz-option-item[@title='Completed']


# Execute the function
create_project()
enter_name()
enter_color()
status()

# Close the browser
driver.close()
