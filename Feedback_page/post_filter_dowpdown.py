
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

    feedback_button.click()

def test_filerwithselector(driver):
    wait = WebDriverWait(driver, 10)

    def click_selector_and_option(option_xpath):
        # Click the selector
        selector = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "selector")))
        selector.click()
        # Click the desired feedback option
        option = wait.until(EC.presence_of_element_located((By.XPATH, option_xpath)))
        option.click()
        time.sleep(5)

    # XPaths for the sort options
    trending_xpath = "//*[@id='content']/div/div/div[1]/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/div[2]"
    top_xpath = "//*[@id='content']/div/div/div[1]/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/div[3]"
    new_xpath = "//*[@id='content']/div/div/div[1]/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/div[4]"

    #XPaths for the filter option
    underview_xpath = "//*[@id='content']/div/div/div[1]/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[1]/div/div[1]/div[2]/div[3]/div[2]/div[2]"
    planned_xpath = "//*[@id='content']/div/div/div[1]/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[1]/div/div[1]/div[2]/div[3]/div[2]/div[3]"
    inprograss_xpath = "//*[@id='content']/div/div/div[1]/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[1]/div/div[1]/div[2]/div[3]/div[2]/div[4]"
    complete_xpath = "//*[@id='content']/div/div/div[1]/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[1]/div/div[1]/div[2]/div[3]/div[2]/div[5]"

    # Select trending feedbacks
    click_selector_and_option(trending_xpath)
    # Select top feedbacks
    click_selector_and_option(top_xpath)
    # Select new feedbacks
    click_selector_and_option(new_xpath)
    # Select under view feedbacks
    click_selector_and_option(underview_xpath)
    # Select planned feedbacks
    click_selector_and_option(planned_xpath)
    # Select in prograss feedbacks
    click_selector_and_option(inprograss_xpath)
    # Select in complete feedbacks
    click_selector_and_option(complete_xpath)