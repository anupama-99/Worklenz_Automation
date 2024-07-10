
import time
import pytest
from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()
    driver.get("https://uat.worklenz.com/")
    driver.maximize_window()
    yield driver # Yield the WebDriver to the test functions
    driver.quit()

def test_go_to_blogs(driver):
    wait = WebDriverWait(driver, 10)
    blog_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@class='flex lg:px-3 py-2 text-sm text-gray-600 hover:text-blue-600 focus-visible:ring-2 focus-visible:ring-offset-2 transition focus-visible:ring-blue-500 focus-visible:outline-none focus-visible:shadow-outline-blue rounded-full'][normalize-space()='Blog']")))
    blog_button.click()
    time.sleep(5)

def test_footer_links(driver):
    wait = WebDriverWait(driver, 10)
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

def test_footer_accounts(driver):
    wait = WebDriverWait(driver, 10)
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
    click_element("/html/body/footer/div[1]/div/div[1]/div/a[4]")
    # to linkedIn
    click_element("//a[@href='https://lk.linkedin.com/showcase/worklenz/']//*[name()='svg']")
    # to twitter
    click_element("//a[@href='https://twitter.com/WorklenzHQ']//*[name()='svg']")

    # Wait for a few seconds to observe the result
    time.sleep(5)

    print('successfully enter to accounts')


