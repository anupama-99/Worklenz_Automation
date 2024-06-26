import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

# Fixture to set up WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # You can change this to your preferred WebDriver
    yield driver
    driver.quit()

# Test function for footer links
def test_footer_links(driver):
    wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed

    def click_element(xpath):
        for _ in range(9):  # Retry up to 9 times
            try:
                element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
                element.click()
                time.sleep(5)
                driver.back()
                break  # Exit the loop if successful
            except StaleElementReferenceException:
                pass  # Retry the loop if exception occurs

    # Click the buttons using the click_element function
    click_element("//a[@class='text-lg flex items-center']//img[@alt='Logo']")
    click_element("//a[normalize-space()='About']")
    click_element("//a[normalize-space()='Contact']")
    click_element("//a[normalize-space()='Roadmap']")
    click_element("//a[normalize-space()='Feedback']")
    click_element("//a[@class='py-2 text-sm text-slate-600 hover:text-blue-600'][normalize-space()='Blog']")
    click_element("//a[normalize-space()='Community']")
    click_element("//a[normalize-space()='Terms']")
    click_element("//a[normalize-space()='Privacy']")

    # Wait for a few seconds to observe the result
    time.sleep(5)

    print('Footer links successfully executed')

# Test function for footer accounts
def test_footer_accounts(driver):
    wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed

    def click_element(xpath):
        for _ in range(4):  # Retry up to 4 times
            try:
                element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
                element.click()
                time.sleep(5)

                # Switch to the new tab if it opens
                if len(driver.window_handles) > 1:
                    driver.switch_to.window(driver.window_handles[1])
                    time.sleep(5)  # Adjust if necessary
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                else:
                    time.sleep(5)  # Adjust if necessary
                    driver.back()
                break  # Exit the loop if successful
            except StaleElementReferenceException:
                pass  # Retry the loop if exception occurs

    # Click the buttons using the click_element function
    # to facebook
    click_element("//a[@href='https://www.facebook.com/Worklenz/']")
    # to github
    click_element("//footer[@class='py-14 bg-slate-100 border-t border-slate-100 mt-10']//a[4]//*[name()='svg']")
    # to linkedIn
    click_element("//a[@href='https://lk.linkedin.com/showcase/worklenz/']//*[name()='svg']")
    # to twitter
    click_element("//a[@href='https://twitter.com/WorklenzHQ']//*[name()='svg']")

    # Wait for a few seconds to observe the result
    time.sleep(5)

    print('Successfully entered accounts')
