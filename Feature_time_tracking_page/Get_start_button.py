
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

wait = WebDriverWait(driver,10)

driver.get("https://uat.worklenz.com/time-tracking/")
driver.maximize_window()

def Get_start():
    button = wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@class='rounded-full text-center transition focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-blue-500 focus-visible:outline-none focus-visible:shadow-outline-blue px-7 py-2.5 bg-blue-600 text-white hover:bg-blue-800 flex gap-1 items-center justify-center w-40 mx-auto mt-8']")))
    button.click()

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

    print(driver.title)


Get_start()

