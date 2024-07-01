
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

def test_roadmap_button(driver):
    wait= WebDriverWait(driver,10)
    roadmap_button =wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@class='link roadmap activeLink']")))
    roadmap_button.click()

def test_after_public_button_click(driver):
    wait = WebDriverWait(driver, 10)
    public_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='boardGridItem']")))
    public_button.click()

    # Wait for the "Feedback" section to be visible
    feedback_section = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='content']/div/div/div[1]/div/div/div[2]/div/div/div/div[2]")))

    # Assert that the "Feedback" section is displayed
    assert feedback_section.is_displayed(),"Feedback section is not displayed after clicking public button"

    #wait for "feedback" button selected
    feedback_button = wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='content']/div/div/div[1]/div/div/div[1]/div/div/div/div[2]/a[2]")))

    #assert that feedback button is selected
    assert feedback_button.is_selected(), "foodback button is not selected"

def test_search(driver):
    wait = WebDriverWait(driver,10)
    search = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='content']/div/div/div[1]/div/div/div[1]/div/div/div/div[2]/div[2]/div")))

    # Click the search box to expand it
    search.click()

    # Enter a value into the search box
    search_value = "test value"
    search.send_keys(search_value)

    # Optionally, submit the search and verify the results
    search.submit()










