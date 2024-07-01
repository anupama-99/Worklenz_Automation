                          ###        Done         ###
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import Login_function  # Import the login function

# Set up WebDriver and WebDriverWait
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Open the login page
driver.get("https://uat.app.worklenz.com/auth/login")
driver.maximize_window()

# Call the login function
Login_function.login(driver, wait)

# Function to check if the page loaded correctly after login
def check_page_load():
    print(driver.title)
    act_title = driver.title
    exp_title = "Worklenz | Home"
    if act_title == exp_title:
        print("login success")
    else:
        print("login fails")

# Function to check the home page after login
def loginhome():
    Name = driver.find_element(By.XPATH, "//h3[@class='ant-typography ng-star-inserted']")
    text = Name.text
    print(text)

# Execute
check_page_load()
loginhome()

# Close the browser
driver.close()
