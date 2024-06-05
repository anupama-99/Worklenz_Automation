                                   ###     Done      #
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://uat.worklenz.com/")
driver.maximize_window()

wait = WebDriverWait(driver,10)

def blog():
    blog_button = driver.find_element(By.XPATH,"//a[@class='flex lg:px-3 py-2 text-sm text-gray-600 hover:text-blue-600 focus-visible:ring-2 focus-visible:ring-offset-2 transition focus-visible:ring-blue-500 focus-visible:outline-none focus-visible:shadow-outline-blue rounded-full'][normalize-space()='Blog']")
    blog_button.click()
    wait.until(EC.title_is("Blog | Worklenz"))

def verify():
    act_title = driver.title
    exep_title = "Blog | Worklenz"
    if act_title == exep_title:
        print("successful")
    else:
        print("not successful")


blog()
verify()

driver.quit()