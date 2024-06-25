from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()

def footer():
    wait = WebDriverWait(driver, 10)
    driver.get("https://uat.worklenz.com/analytics/")

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


# Run the item_filters function
footer()

# Wait for a few seconds to observe the result
time.sleep(5)

print('SUCCESSFULLY EXECUTED!')

# Close the browser
driver.quit()

