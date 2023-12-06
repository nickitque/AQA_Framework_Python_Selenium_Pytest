import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """Fixture for choosing language.Work with terminal for choosing language.."""
    parser.addoption("--language", action="store", default="ru",
                     help="Choose language: ru or en ")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    """Work with language in headers."""
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
