
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture(scope="module")
def driver():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()
    driver.get("https://worklenz.canny.io/")
    driver.maximize_window()
    yield driver # Yield the WebDriver to the test functions
    driver.quit()

def test_login(driver):
    wait= WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='buttonV2 primary medium outlined']")))
    button.click()

    login_form = driver.find_element(By.CLASS_NAME,"loginForm")

    #login form is displayed for not
    assert login_form.is_displayed(),"login form is not displayed"




