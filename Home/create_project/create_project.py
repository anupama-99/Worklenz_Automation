import select
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import Login_function  # Import the login function

driver = webdriver.Chrome()
driver.get("https://uat.app.worklenz.com/auth/login")
wait = WebDriverWait(driver, 10)

driver.maximize_window()

# Call the login function
Login_function.login(driver, wait)


def test_create_project():
    # Wait for and click the 'Create Project' button
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Create Project']")))
    button.click()

    # Wait for the 'Create Project' slider to appear
    slider = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='ant-drawer ant-drawer-right ng-star-inserted ant-drawer-open']//div[@class='ant-drawer-body']")))


def test_enter_name():
    # Enter new project name
    name_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Name']")))
    name_input.send_keys("OMI Game")

def test_enter_color():
    colors_to_select = driver.find_element(By.XPATH,"//nz-tag[@class='ant-tag ant-dropdown-trigger ms-2 rounded-circle cursor-pointer ant-tag-has-color']")
    colors_to_select.click()

    selected_color = wait.until(EC.element_to_be_clickable((By.XPATH,"//li[5]//nz-tag[1]")))
    selected_color.click()

# def enter_color():
#     # Generate the list of XPaths dynamically
#     colors_to_select = [f"//li[{i}]//nz-tag[1]" for i in range(1, 25)]
#
#     for color_xpath in colors_to_select:
#         # Open color picker
#         color_picker = wait.until(EC.element_to_be_clickable((By.XPATH,"//nz-tag[@class='ant-tag ant-dropdown-trigger ms-2 rounded-circle cursor-pointer ant-tag-has-color']")))
#         color_picker.click()
#
#         # Select color
#         color_option = wait.until(EC.element_to_be_clickable((By.XPATH, color_xpath)))
#         color_option.click()
#         time.sleep(1)


def test_status():
    status_type = driver.find_element(By.XPATH,"//nz-select-item[@title='Proposed']")
    status_type.click()

    selected_status = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(text(),'In Progress')]")))
    selected_status.click()

    # options = driver.find_elements(By.CLASS_NAME, "cdk-virtual-scroll-content-wrapper")
    # time.sleep(5)
    #
    # for types in options:
    #     if types.text == "Cancelled":
    #         types.click()
    #         time.sleep(5)
    #         break

def test_health():
    health_types = driver.find_element(By.XPATH,"//*[@id='cdk-overlay-2']/div/div[2]/div/div/div[2]/nz-spin/div/form/nz-form-item[4]/nz-form-control/div/div/nz-select/nz-select-top-control/nz-select-item")
    health_types.click()

    selected_health = wait.until(EC.element_to_be_clickable((By.XPATH,"//nz-option-item[@title='Needs Attention']//div[@class='ant-select-item-option-content']")))
    selected_health.click()

# def category():
#     categories = wait.until(EC.element_to_be_clickable((By.XPATH,"//nz-select-top-control[@class='ant-select-selector ng-tns-c146563758-207']")))
#     categories.click()

def test_note():
    note_box = wait.until(EC.presence_of_element_located((By.XPATH,"//textarea[@placeholder='Notes']")))
    note_box.send_keys("mobile game developement project manage ")

def test_client():
    client = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='Select client']")))
    client.send_keys("Ceydigital")

def test_create():
    create_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='ant-btn ant-btn-primary ant-btn-block ng-star-inserted']")))
    create_button.click()




# Close the browser
driver.close()
