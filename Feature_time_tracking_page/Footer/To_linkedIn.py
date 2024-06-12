                   ###       Done        ###
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

wait = WebDriverWait(driver,10)

driver.get("https://uat.worklenz.com/time-tracking/")
driver.maximize_window()

def linkedin():
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/footer")))
    linkedin = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='https://lk.linkedin.com/showcase/worklenz/']//*[name()='svg']")))
    linkedin.click()

    # Handle the new window  # Store the ID of the original window
    original_window = driver.current_window_handle

    # Wait for the new window to appear
    wait.until(EC.new_window_is_opened([original_window]))

    # Get all window handles
    all_windows = driver.window_handles

    # Identify the new window and switch to it
    for window in all_windows:
        if window != original_window:
            driver.switch_to.window(window)
            break

    # Step 4: Get the title of the new window
    print(driver.title)

linkedin()

driver.quit()