                           ###       Done         ###
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

wait = WebDriverWait(driver,10)

driver.get("https://uat.worklenz.com/")
driver.maximize_window()

def get_start():
   get_start_button = wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@class='rounded-full text-center transition focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-blue-500 focus-visible:outline-none focus-visible:shadow-outline-blue px-7 py-2.5 bg-blue-600 text-white hover:bg-blue-800 flex gap-1 items-center justify-center']")))
   get_start_button.click()

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

   wait.until(EC.title_is(("Worklenz | Signup")))

def vefity_get_start():
    act_title = driver.title
    exp_title = "Worklenz | Signup"
    if act_title == exp_title:
        print("In sign up page")
    else:
        print("Not in sign up page")

get_start()
vefity_get_start()

driver.quit()
