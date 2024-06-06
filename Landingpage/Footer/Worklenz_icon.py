                           ###       Done        ###
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

wait = WebDriverWait(driver,10)

driver.get("https://uat.worklenz.com/")
driver.maximize_window()
def gotofooter():
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/footer")))
    worklenz_icon =wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@class='text-lg flex items-center']//img[@alt='Logo']")))
    worklenz_icon.click()

gotofooter()

driver.quit()