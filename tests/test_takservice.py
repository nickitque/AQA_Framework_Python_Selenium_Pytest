import pytest
from selenium import webdriver
from page_objects import HomePage

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Optional: Add implicit wait
    driver.get("https://takservice.pl/")  # Open the website
    yield driver
    driver.quit()


def test_search_product(driver):
    home_page = HomePage(driver)
    product_name = "Laptop"
    home_page.search_for_product(product_name)

    # Add assertions here to verify the search results

def test_another_test_case(driver):
    # Implement another test case using page objects


def test_search_product(driver):
    home_page = HomePage(driver)
    product_name = "Laptop"
    home_page.search_for_product(product_name)

    # Add assertions here to verify the search results

def test_another_test_case(driver):
# Implement another test case using page objects
