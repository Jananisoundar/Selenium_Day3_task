from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def fetch_webpage_content():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()

    try:
        # Open the website
        driver.get("https://www.saucedemo.com/")

        # Login using provided credentials
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(5)  # Let the page load

        # Fetch the current URL of the webpage
        current_url = driver.current_url
        print(f"Current URL: {current_url}")

        # Fetch the title of the webpage
        title = driver.title
        print(f"Title of the page: {title}")

        # Extract the entire content of the webpage
        page_content = driver.page_source

        # Save the content to a text file named "test.txt"
        with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
            file.write(page_content)

        print("Content saved to Webpage_task_11.txt")

    finally:
        # Close the browser session
        driver.quit()
#Calling the function
fetch_webpage_content()