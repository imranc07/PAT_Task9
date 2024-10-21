"""
Homepage.py - Python Selenium Script to verify and validate the Swag Lab url and title and save webpage contents
"""

# Import the WebDriver class from Selenium to control the browser
from selenium import webdriver

# Import the Service class for managing WebDriver services
from selenium.webdriver.common.service import Service

# Import ChromeDriverManager to automatically manage ChromeDriver installation
from webdriver_manager.chrome import ChromeDriverManager

# Import sleep function to pause the execution of the script for a specified time
from time import sleep

# Class for automting Swag Labs webpage
class SwagLabsAutomation:

    # Init Constructor, Passing url
    def __init__(self, url):

        # Assign the provided URL to variable 'url'
        self.url = url

        # Initialize a Chrome WebDriver to control the Chrome browser
        self.driver = webdriver.Chrome()


    # starting automation method
    def start_automation(self):

        # Maximize the browser window
        self.driver.maximize_window()

        # Navigate to the specified URL
        self.driver.get(self.url)

        # Indicate that the automation process started successfully
        return True
   
    # Shutdown method to close the browser
    def shutdown(self):

        # Quit the WebDriver and close all associated browser windows
        self.driver.quit()

    # Method to fetch the title of the webpage
    def fetch_title(self):

        # Check if the automation process started successfully
        if self.start_automation():
            
            # Return the title of the current webpage
            return self.driver.title
        
        else:

            # Return False if the automation process failed
            return False

       
    # Method to fetch the current URL of the webpage
    def fetch_url(self):

        # Check if the automation process started successfully
        if self.start_automation():
            
            # Return the current URL of the webpage
            return self.driver.current_url

        else:

            # Return False if the automation process failed
            return False

    # Method to to save the contents of the webpage    
    def save_webpage_content(self):

        # Check if the automation process started successfully
        if self.start_automation():

            # Fetch the entire content of the current webpage
            page_content = self.driver.page_source

            # Create and open a text file named 'Webpage_task_11.txt' in append mode
            file = open('Webpage_task_11.txt', 'a')

            # Write the content of the webpage into the text file
            file.write(page_content)

            # Close the text file
            file.close()

            # Return the current URL of the webpage after saving its content
            return self.driver.current_url

        else:

            # Return False if the automation process failed
            return False