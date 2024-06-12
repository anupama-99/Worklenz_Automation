
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)

# Open the web page with the video
driver.get("https://uat.worklenz.com/time-tracking/")

driver.maximize_window()

# Wait for the video element to be present
video = wait.until(EC.presence_of_element_located((By.ID, "video-2")))

# scroll to video element
driver.execute_script("window.scrollBy(0,1500)","")

# Check if the video element is present
if video:
    print("Video element found.")

    # Play the video using JavaScript
    driver.execute_script("arguments[0].play();", video)

    # Wait for a few seconds to let the video play
    time.sleep(20)

    # Check current playback time
    current_time = driver.execute_script("return arguments[0].currentTime;", video)
    print(f"Current playback time: {current_time} seconds")

    # Optionally, you can check if the video has played for at least a certain duration
    if current_time > 0:
        print("Video is successfully playing.")

    else:
        print("Video failed to play.")

else:
    print("Video element not found.")



driver.quit()
