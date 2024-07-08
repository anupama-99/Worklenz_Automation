
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

videos = [
    "video-0",
    "video-1",
    "video-2",
    "video-3",
    "video-4"
]
@pytest.fixture(scope="module")
def driver():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()
    driver.get("https://uat.worklenz.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_enter_task_mng(driver):
    wait = WebDriverWait(driver, 10)
    features = wait.until(EC.visibility_of_element_located((By.XPATH,"//span[normalize-space()='Features']")))
    task_mng = driver.find_element(By.XPATH,"//a[normalize-space()='Task Management']")
    features.click()
    task_mng.click()

    wait.until(EC.title_is("Task Management | Worklenz"))

    act_title = driver.title
    exep_title = "Task Management | Worklenz"
    if act_title == exep_title:
        print("In task management page")
    else:
        print("Not in task management page")

def test_task_management(driver):
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

def test_footer_links(driver):
    wait = WebDriverWait(driver, 10)
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

    # Wait for a few seconds to observe the result
    time.sleep(5)

    print('Footer links successfully executed')

def test_footer_accounts(driver):
    wait = WebDriverWait(driver, 10)
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

    # Wait for a few seconds to observe the result
    time.sleep(5)

    print('successfully enter to accounts')

