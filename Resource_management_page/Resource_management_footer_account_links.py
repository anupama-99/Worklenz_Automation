
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()


def footer():
    wait = WebDriverWait(driver, 10)
    driver.get("https://uat.worklenz.com/resource-management/")

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


# Run the footer function
footer()

# Wait for a few seconds to observe the result
time.sleep(5)

print('successfully enter to accounts')

# Close the browser
driver.quit()
