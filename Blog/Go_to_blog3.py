# Mastering Horizon Europe Projects with Open-Source Tools

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()
    driver.get("https://uat.worklenz.com/")
    driver.maximize_window()
    yield driver # Yield the WebDriver to the test functions
    driver.quit()

def test_go_to_blogs(driver):
    wait = WebDriverWait(driver, 10)
    blog_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@class='flex lg:px-3 py-2 text-sm text-gray-600 hover:text-blue-600 focus-visible:ring-2 focus-visible:ring-offset-2 transition focus-visible:ring-blue-500 focus-visible:outline-none focus-visible:shadow-outline-blue rounded-full'][normalize-space()='Blog']")))
    blog_button.click()

# 05 Best Open-Source Case Management Software for Your Law Firm
def test_blog3(driver):
    wait = WebDriverWait(driver,10)
    blog = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/main/ul/li[3]/a")))
    blog.click()

def test_picture_display(driver):
    wait = WebDriverWait(driver, 10)

    image = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/picture/img")))

    # Check if the image is displayed
    if image.is_displayed():
        print("Image is displayed on the page.")

        # Check if the image source is not empty
        src = image.get_attribute("src")
        if src:
            print("Image source is valid:", src)
        else:
            print("Image source is empty.")
    else:
        print("Image is not displayed on the page.")

def test_go_back_to_blogs(driver):
    wait = WebDriverWait(driver,10)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    back_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@class='bg-gray-100 px-5 py-3 rounded-md hover:bg-gray-200 transition']")))
    back_button.click()