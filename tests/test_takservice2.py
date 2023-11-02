import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def browser():
    # Initialize the browser (e.g., Chrome)
    driver = webdriver.Chrome()
    yield driver  # Provide the driver object to the test
    driver.quit()  # Quit the browser after the test

def test_contact_form(browser):
    # Open Google
    browser.get("https://testtak.gedex.ca/")
    # Find the search input element and type a query
    search_box = browser.find_element(By.CSS_SELECTOR, "#main-section > div > div > div.grid-bonus__content > a")
    search_box.click()
    name_field = browser.find_element(By.CSS_SELECTOR, "#wpcf7-f179-o1 > form > label:nth-child(2) > span > input")
    name_field.send_keys("Test Name")
    phone_field = browser.find_element(By.CSS_SELECTOR, "#wpcf7-f179-o1 > form > label:nth-child(3) > span > input")
    phone_field.send_keys("123456")
    msg = browser.find_element(By.NAME, "your-message")
    msg.send_keys("Test message")
    btn = browser.find_element(By.CSS_SELECTOR, "#wpcf7-f179-o1 > form > input")
    btn.click()
    time.sleep(5)

    # Submit the search form
    #search_box.send_keys(Keys.RETURN)

    # Verify the search results page
    #assert "Selenium automation with Python" in browser.title

def test_example_page(browser):
    # Open an example web page
    browser.get("https://example.com")

    # Perform some interactions and assertions
    # For example, checking the page title
    assert "Example Domain" in browser.title

if __name__ == "__main__":
    pytest.main(["-v", "test_example.py"])