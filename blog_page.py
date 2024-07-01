
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)
driver.get("https://uat.worklenz.com/blog/")
driver.maximize_window()

def test_blog_page_title():
        actual_title = driver.title
        exep_title = "Blog | Worklenz"

        if actual_title == exep_title:
                print(f"success: page titile is '{actual_title}' and matches the expected title.")
        else:
                print(f"fail: page title is '{actual_title}' and not expected title '{exep_title}'.")

def test_blog_page_post_links():
        # Wait until all blog posts are loaded
        WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[1]/main/ul/li/a"))
        )

        # Get all blog posts
        blog_posts = driver.find_elements(By.XPATH, "/html/body/div[1]/main/ul/li")

        for post in blog_posts:
                # Get all links within each blog post
                post_links = post.find_elements(By.TAG_NAME, "a")
                links = [link.get_attribute("href") for link in post_links]

                for link in links:
                        driver.get(link)
                        try:
                                # Wait until the article is loaded
                                WebDriverWait(driver, 10).until(
                                        EC.presence_of_element_located((By., "article"))
                                )
                                driver.back()
                                print(f"Success: The link {link} loaded correctly.")

                        except:
                                print(f"Failure: The link {link} did not load correctly.")

