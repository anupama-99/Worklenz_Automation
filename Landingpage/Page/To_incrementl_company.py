
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')

# Initialize the driver with the configured options
driver = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(driver,10)

driver.get("https://uat.worklenz.com/")
driver.maximize_window()

def incrementl_company():
    company = driver.find_element(By.XPATH,"//a[@href='https://incrementl.com/']//picture//img[@alt='gui']")
    company.click()


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

    wait.until(EC.title_contains("Incrementl"))

    print(driver.title)


incrementl_company()