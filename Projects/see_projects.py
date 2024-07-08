import time

import pytest
from selenium import webdriver
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

def test_enter_project():
    project_button = wait.until(EC.presence_of_element_located((By.XPATH,"//ul[@class='top-nav-ul-main ant-menu ant-menu-root ant-menu-light ant-menu-horizontal']//strong[@class='ng-star-inserted'][normalize-space()='Projects']")))
    project_button.click()
    time.sleep(5)

    # check title is correct
    act_title = driver.title
    exep_title = "Worklenz | Projects"
    print(driver.title)
    assert act_title == exep_title ,"not enter projects"

def test_see_all_projects():
    all_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[normalize-space()='All']")))
    print("All button is displayed: ", all_button.is_displayed())

    exp_button = "All"
    act_button = all_button.text
    if act_button == exp_button:
        print(f"text in button is correct.text is {act_button} ")
    else:
        print(f"text in button is wrong. text is {act_button}")

    all_button.click()

def test_favorite_projects():
    favorite_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[normalize-space()='Favorites']")))
    print("favorite button is displayed: ", favorite_button.is_displayed())

    exp_button = "Favorites"
    act_button = favorite_button.text
    if act_button == exp_button:
        print(f"text in button is correct.text is {act_button} ")
    else:
        print(f"text in button is wrong. text is {act_button}")

    favorite_button.click()

def test_archived():
    archived_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[normalize-space()='Archived']")))
    print(f"archived button is displayed: ", archived_button.is_displayed())

    exp_button = "Archived"
    act_button = archived_button.text
    if act_button == exp_button:
        print(f"text in button is correct.text is {act_button} ")
    else:
        print(f"text in button is wrong. text is {act_button}")

    archived_button.click()

