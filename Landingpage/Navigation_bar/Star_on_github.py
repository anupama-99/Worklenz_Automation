                             ###      Done        ###
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

wait = WebDriverWait(driver,20)

driver.get("https://uat.worklenz.com/")
driver.maximize_window()

def Star_on_github():
    starongithub_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Star us on GitHub']")))
    starongithub_button.click()

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
    new_window_title = WebDriverWait(driver, 10).until(
        EC.title_is(driver.title)
    )
    print("Title of the new window: ", new_window_title)
    print(driver.title)

Star_on_github()

driver.quit()