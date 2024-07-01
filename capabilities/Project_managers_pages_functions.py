
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

videos = [
    "video-0",
    "video-1",
    "video-2",
    "video-3",
    "video-4",
    "video-5"
]

@pytest.fixture(scope="module")
def driver():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()
    driver.get("https://uat.worklenz.com/for-project-managers/")
    driver.maximize_window()
    yield driver  # Yield the WebDriver to the test functions
    driver.quit()


def test_project_managers(driver):
    wait = WebDriverWait(driver, 10)
    print(driver.title)
    # get start button
    button = driver.find_element(By.XPATH,"//a[@class='rounded-full text-center transition focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-blue-500 focus-visible:outline-none focus-visible:shadow-outline-blue px-7 py-2.5 bg-blue-600 text-white hover:bg-blue-800 flex gap-1 items-center justify-center w-40 mx-auto mt-8']")
    button.click()

    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(5)  # Adjust if necessary
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    else:
        time.sleep(5)  # Adjust if necessary
        driver.back()

    #.......... play videos in the page
    for video in videos:
        # Wait for the video element to be present
        video = wait.until(EC.presence_of_element_located((By.ID, video)))

        # Scroll to the element
        driver.execute_script("arguments[0].scrollIntoView();", video)

        if video:

            # Play the video using JavaScript
            driver.execute_script("arguments[0].play();", video)

            # Wait for a few seconds to let the video play
            time.sleep(20)

            # Check current playback time
            current_time = driver.execute_script("return arguments[0].currentTime;", video)
            print(f"Current playback time: {current_time} seconds")

            # Optionally, you can check if the video has played for at least a certain duration
            if current_time > 0:
                print(f"video is successfully playing.")

            else:
                print("Video failed to play.")

        else:
            print("Video element not found.")



from Footer_linkes import test_footer_links,test_footer_accounts

def test_footer(driver):
    test_footer_links(driver)
    test_footer_accounts(driver)

#####################footer test twice ######################

