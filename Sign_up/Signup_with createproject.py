
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

Fullname = "udeshani anupama"
Email = "udeshanianupama@gmail.com"
Password ="#18Apc.3619#"

# Initialize the WebDriver (assuming you have the chromedriver in your PATH)
@pytest.fixture(scope="module")
def driver():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()
    driver.get("https://uat.app.worklenz.com/auth/signup")
    driver.maximize_window()
    yield driver # Yield the WebDriver to the test functions
    driver.quit()


def test_sign_up(driver):
    wait = WebDriverWait(driver, 10)
    Name_element = wait.until(EC.visibility_of_element_located((By.ID,"full-name")))
    Email_element = driver.find_element(By.ID,"email")
    Password_element = driver.find_element(By.ID,"password")
    sigh_up_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='ant-btn mt-1 ant-btn-primary ant-btn-lg ant-btn-block']")))

    Name_element.send_keys(Fullname)
    Email_element.send_keys(Email)
    Password_element.send_keys(Password)
    sigh_up_button.click()

def test_enter_organization(driver):
    wait = WebDriverWait(driver, 10)
    org = driver.find_element(By.XPATH,"//input[@id='BFAOZT']")
    org.send_keys("Deepsea.org")
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"ng-star-inserted"))).click()
    print(org)

def test_gobackbutton_enter_project(driver):
    wait = WebDriverWait(driver, 10)
    goback_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Go back']")))
    goback_button.click()  # go to enter organization page
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ng-star-inserted"))).click()  # go to enter project page

def test_enter_project(driver):
    wait = WebDriverWait(driver, 10)
    project = wait.until(EC.visibility_of_element_located((By.ID,"BNWGQG")))
    project.send_keys("myweather")
    continue_button = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/worklenz-root/worklenz-account-setup/div[1]/div/div/div[2]/nz-space/div/nz-skeleton/form/div/button[2]/span")))
    continue_button.click()
    print(project)


def test_enter_task(driver):
    wait = WebDriverWait(driver, 10)
    task = wait.until(EC.visibility_of_element_located((By.ID,"task-name-input-0")))
    task.send_keys("checkweather")
    continue_button = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/worklenz-root/worklenz-account-setup/div[1]/div/div/div[2]/nz-space/div/nz-skeleton/form/div[2]/button[2]/span")))
    continue_button.click()
    print(task)


def test_enter_teammembers(driver):
    wait = WebDriverWait(driver, 10)
    team = driver.find_element(By.ID,"FQV")
    team.send_keys("anubwabt414@gmail.com")
    button = wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/worklenz-root/worklenz-account-setup/div[1]/div/div/div[2]/nz-space/div/nz-skeleton/form/div/button[3]/span")))
    button.click()
    print(team)




