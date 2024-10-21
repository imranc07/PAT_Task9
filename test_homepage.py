"""
test_homepage.py - Python Selenium Scripts to test the Swag Labs url, title and save page contents (test cases)
"""

# Import the SwagLabsAutomation class from the 'homepage' module
from homepage import SwagLabsAutomation

# Import the pytest framework to write and execute test cases
import pytest  

# Initialize the base URL for Swag Labs
url = "https://www.saucedemo.com/"

# Create an instance of SwagLabsAutomation, initializing it with the Swag Labs URL for automated testing
automation = SwagLabsAutomation(url)


# Test case for verifying the title of the webpage
def test_title():

    # Expected title of the Swag Labs homepage
    expected_title = "Swag Labs"

    # Assertion to verify if the fetched title matches the expected title
    assert automation.fetch_title() == expected_title

    # Prints a success message indicating the webpage title was verified correctly
    print("SUCCESS: SWAG LAB TITLE VERIFIED")


# Test case for verifying the URL of the webpage
def test_url():

    # Expected URL of the Swag Labs homepage
    expected_url = "https://www.saucedemo.com/"

    # Assertion to check if the fetched URL matches the expected URL
    assert automation.fetch_url() == expected_url

    # Prints a success message indicating the webpage URL was verified correctly
    print("SUCCESS: SWAG LAB URL VERIFIED")


# Test case for saving the webpage content to a file
def test_save_page_content():

    # Save the webpage content using the automation function
    file_path = automation.save_webpage_content()
    
    # Assert that the file path is not None, indicating that the content was saved
    assert file_path is not None

    # Prints a success message indicating the webpage contents saved to text file    
    print("SUCCESS: WEBPAGE CONTENTS SAVED TO TEXT FILE 'Webpage_task_11.txt'")