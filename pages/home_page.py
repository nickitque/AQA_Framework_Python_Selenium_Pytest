from base_page import BasePage
from locators import HomePageLocators
import time


class HomePage(BasePage):
    def click_sign_up_button(self):
        self.browser.find_element(*HomePageLocators.SIGN_UP_BTN).click()
        time.sleep(10)

    def fill_contact_form_homepage(self):
        self.browser.find_element(*HomePageLocators.CF_NAME_FIELD).send_keys("Nikita_test")
        self.browser.find_element(*HomePageLocators.CF_PHONE_FIELD).send_keys("+48 111 111 111")
        self.browser.find_element(*HomePageLocators.CF_MESSAGE_FIELD).send_keys("Test with using Python and selenium.")
        self.browser.find_element(*HomePageLocators.CF_SEND_BTN).click()
