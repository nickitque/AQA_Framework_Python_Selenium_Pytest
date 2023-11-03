from .base_page import BasePage
from .locators import PromotionsPageLocators
import time


class PromotionsPage(BasePage):

    def click_back_to_homepage_button(self):
        self.browser.find_element(*PromotionsPageLocators.BACK_TO_HOMEPAGE_BTN).click()
        assert self.browser.current_url == "https://takservice.pl/ru/", "The url is not https://takservice.pl/ru/"