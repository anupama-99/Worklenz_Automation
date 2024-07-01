
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver (assuming you have the chromedriver in your PATH)
@pytest.fixture(scope="module")
def driver():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()
    driver.get("https://uat.worklenz.com/contact/")
    driver.maximize_window()
    form_iframe = driver.find_element(By.ID,"hs-form-iframe-0")
    driver.switch_to.frame(form_iframe)
    yield driver # Yield the WebDriver to the test functions
    driver.quit()

def test_form_firstname(driver):
    wait = WebDriverWait(driver, 10)
    first_name = wait.until(EC.visibility_of_element_located((By.ID,"firstname-3cbc9ade-13ff-41a7-a76d-7fbd525ec079")))
    first_name.send_keys("anupama")

    # Check if the 'required' attribute is present
    is_required = first_name.get_attribute('required') is not None
    assert is_required, "First name field should be required"

def test_form_lastname(driver):
    wait = WebDriverWait(driver, 10)
    last_name = wait.until(EC.visibility_of_element_located((By.ID, "lastname-3cbc9ade-13ff-41a7-a76d-7fbd525ec079")))
    last_name.send_keys("wanigasooriya")

def test_form_companyname(driver):
    wait = WebDriverWait(driver, 10)
    company_name = wait.until(EC.visibility_of_element_located((By.ID,"company-3cbc9ade-13ff-41a7-a76d-7fbd525ec079")))
    company_name.send_keys("Ceydigital")

def test_form_email(driver):
    wait = WebDriverWait(driver, 10)
    email_address = wait.until(EC.visibility_of_element_located((By.ID,"email-3cbc9ade-13ff-41a7-a76d-7fbd525ec079")))
    email_address.send_keys("Udeshanianupama@gmail.com")

    # Check if the 'required' attribute is present
    is_required = email_address.get_attribute('required') is not None
    assert is_required, "Email field should be required"


def test_form_message(driver):
    wait = WebDriverWait(driver, 10)
    message = wait.until(EC.visibility_of_element_located((By.ID,"message-3cbc9ade-13ff-41a7-a76d-7fbd525ec079")))
    message.send_keys("contact for to say this is testing practice.")

    # Check if the 'required' attribute is present
    is_required = message.get_attribute('required') is not None
    assert is_required, "Message field should be required"

def test_form_send_msg_button(driver):
    wait = WebDriverWait(driver, 10)
    send_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='Send Message']")))
    send_button.click()
    time.sleep(10)

# def test_send_verify(driver):
#     wait = WebDriverWait(driver, 10)
#
#     # switching to the iframe
#     success_msg_iframe = driver.find_element(By.CLASS_NAME, "hs-form-iframe")
#     driver.switch_to.frame(success_msg_iframe)
#
#     # After switching to the iframe, locate the HTML document elements
#     html_doc = driver.find_element(By.XPATH,"/html")
#
#     # Wait for the success message to appear
#     success_message = wait.until(EC.visibility_of_element_located(
#         (By.XPATH, "//div[@class='submitted-message hs-main-font-element hs-form-3cbc9ade-13ff-41a7-a76d-7fbd525ec079 hs-form-3cbc9ade-13ff-41a7-a76d-7fbd525ec079_192c3155-1a5c-43fe-a4ee-12271112cf91']"))
#     )
#     assert success_message.text == "Your submission has been received. Thank you!", f"Unexpected message: {success_message.text}"





