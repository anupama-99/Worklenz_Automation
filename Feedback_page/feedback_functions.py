
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
    driver.get("https://worklenz.canny.io/")
    driver.maximize_window()
    yield driver # Yield the WebDriver to the test functions
    driver.quit()

def test_feedfack_button(driver):
    wait = WebDriverWait(driver, 10)
    feedback_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='content']/div/div/div[1]/div/div/div[1]/div/div/div/div[2]/a[2]")))

    # # Get the color of the button text before clicking
    # color_before_click = feedback_button.value_of_css_property('color')
    # print(f'Color before click: {color_before_click}')

    feedback_button.click()

    # # Get the color of the button text after clicking
    # color_after_click = feedback_button.value_of_css_property('color')
    # print(f'Color after click: {color_after_click}')

    # # Assert that the color has changed
    # assert color_before_click != color_after_click, "Button text color did not change after click"

    # Wait for the "Feedback" section to be visible
    feedback_section = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='content']/div/div/div[1]/div/div/div[2]/div/div/div/div[2]")))

    # Assert that the "Feedback" section is displayed
    assert feedback_section.is_displayed(), "Feedback section is not displayed after clicking public button"

def test_createpost_addtitle(driver):
    wait = WebDriverWait(driver,10)
    title = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='Short, descriptive title']")))

    # Check the placeholder attribute
    title_placeholder = title.get_attribute('placeholder')

    # Replace 'Expected Placeholder Text' with the expected placeholder text
    assert title_placeholder == 'Short, descriptive title', f"Expected 'Short, descriptive title' but got '{title_placeholder}'"

    title.send_keys("dark mood")

def test_createpost_description(driver):
    wait = WebDriverWait(driver, 10)
    description = wait.until(EC.visibility_of_element_located((By.ID,"details")))

    # Check the placeholder attribute
    description_placeholder = description.get_attribute('placeholder')

    # Replace 'Expected Placeholder Text' with the expected placeholder text
    assert description_placeholder == 'Any additional details…', f"Expected 'Any additional details…' but got '{description_placeholder}'"

    description.send_keys("it is better if get dark mood of the Worklenz")

def test_canceledpost(driver):
    wait = WebDriverWait(driver, 10)
    cancle_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='right']//button[@type='button']")))
    cancle_button.click()


def test_gotocreatepost(driver):
    wait = WebDriverWait(driver, 10)
    post = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@aria-label='Create post']")))
    post.click()

    form = wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='content']/div/div/div[1]/div/div/div[2]/div/div/div/div[2]/div[1]/form")))

    # Check form is displayed after enter posy button
    assert form.is_displayed(),"form need to crete post not displayed"

# def test_createpost_button(driver):
#     wait = WebDriverWait(driver, 10)
#     createpost_button = wait.until(EC.element_to_be_clickable(By.XPATH,"//button[@type='submit']"))
#     createpost_button.click()





