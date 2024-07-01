
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)
driver.get("https://uat.app.worklenz.com/auth/signup")
driver.maximize_window() # maximize the browser window

Fullname = "Anupama Udeshani"
Email = "anupamabb4@gmail.com"
Password ="#18Apc.3619#"

def test_sign_up():
    Name_element = wait.until(EC.visibility_of_element_located((By.ID,"full-name")))
    Email_element = driver.find_element(By.ID,"email")
    Password_element = driver.find_element(By.ID,"password")
    sigh_up_button = wait.until(EC.element_to_be_clickable(By.XPATH,"//button[@class='ant-btn mt-1 ant-btn-primary ant-btn-lg ant-btn-block']"))

    Name_element.send_keys(Fullname)
    Email_element.send_keys(Email)
    Password_element.send_keys(Password)
    sigh_up_button.click()

def test_organization_enter():
    org = driver.find_element(By.XPATH,"/html/body/worklenz-root/worklenz-account-setup/div[1]/div/div/div[2]/nz-space/div/nz-skeleton/form/nz-form-item/nz-form-control/div/div")
    org.send_keys("My world")
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"ng-star-inserted"))).click()
    print(org)

def test_gobackbutton_projectenter():
    goback_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Go back']")))
    goback_button.click()  # go to enter organization page
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ng-star-inserted"))).click()  # go to enter project page

def test_quit_from_select_templete():
    import_templete_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='ant-btn ms-auto me-auto ant-btn-primary']")))
    import_templete_button.click()

    close_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Cancel']")))
    close_button.click()
def test_importtemplate_projectenter():
    # Click the import button
    import_templete_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='ant-btn ms-auto me-auto ant-btn-primary']")))
    import_templete_button.click()

    # Wait for the 'select template' slider to appear
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='cdk-overlay-0']/div/div[2]")))

    # List of templates to be selected
    templates = [
        "Bug Tracking",
        "Construction",
        "Design & Creative",
        "Education",
        "Finance",
        "HR & Recruiting",
        "Information Technology",
        "Legal",
        "Manufacturing",
        "Marketing",
        "Nonprofit",
        "Personal use",
        "Sales & CRM",
        "Services & Consulting",
        "Software Development"
    ]

    # Select each template
    for template in templates:
        template_element = wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[normalize-space()='{template}']")))
        template_element.click()

    # Select templete and import
    templete = wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='cdk-overlay-0']/div/div[2]/div/div/div[2]/nz-tabset/div/div/div/worklenz-template-list/div/div[1]/nz-skeleton/ul/li[1]")))
    create_button = wait.until(EC.element_to_be_clickable(By.XPATH,"//span[normalize-space()='Create']"))
    

