
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

def test_searchbox(driver):
    wait = WebDriverWait(driver,10)
    searchbox = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"searchBar")))

    # Check the placeholder attribute
    search = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='Search…']")))
    search_placeholder = search.get_attribute('placeholder')

    # Replace 'Expected Placeholder Text' with the expected placeholder text
    assert search_placeholder == 'Search…', f"Expected 'Search…' but got '{search_placeholder}'"

    # Get the initial width of the search box
    initial_width = searchbox.size['width']

    searchbox.click()

    # Verify that the search box has expanded
    expanded_width = searchbox.size['width']
    assert expanded_width > initial_width, "Search box did not expand after click"

    search.send_keys("Ability to tag all members of project")
    time.sleep(5)

    # Verify posts apper in the search results
    search_results = driver.find_elements(By.XPATH,"//span[normalize-space()='Ability to tag all members of project']")
    assert len(search_results) > 0 ,"post not fund in search results"

    quit_searchbox = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='content']/div/div/div[1]/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]")))
    quit_searchbox.click()
    time.sleep(5)









