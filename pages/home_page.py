from .base_page import BasePage
from .locators import HomePageLocators
import time


class HomePage(BasePage):
    def click_sign_up_button(self):
        self.browser.find_element(*HomePageLocators.SIGN_UP_BTN).click()
        time.sleep(10)
