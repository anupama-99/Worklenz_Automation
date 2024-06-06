import time  ###   not correct     ####
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

wait = WebDriverWait(driver,10)

driver.get("https://uat.worklenz.com/")
driver.maximize_window()

def product_hunt():
   product_hunt_button = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='overflow-x-clip']//a[1]")))
   product_hunt_button.click()

   # # Handle the new window  # Store the ID of the original window
   # original_window = driver.current_window_handle
   #
   # # Wait for the new window to appear
   # wait.until(EC.new_window_is_opened([original_window]))
   #
   # # Get all window handles
   # all_windows = driver.window_handles
   #
   # # Identify the new window and switch to it
   # for window in all_windows:
   #     if window != original_window:
   #         driver.switch_to.window(window)
   #         break

time.sleep(10)


product_hunt()

driver.quit()
