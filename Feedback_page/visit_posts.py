
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

def test_visit_posts(driver):
    wait = WebDriverWait(driver, 10)
    posts = driver.find_element(By.XPATH,"//*[@id='content']/div/div/div[1]/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div[1]/a")
    posts.click()

##################### can't visit posts   ###################