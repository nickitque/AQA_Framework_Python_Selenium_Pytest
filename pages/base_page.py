from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def should_be_address_text(self):
        assert self.is_element_present(*BasePageLocators.ADDRESS_TEXT_HEADER), "Login link is not presented"

    def should_be_address_icon(self):
        assert self.is_element_present(*BasePageLocators.ADDRESS_ICON_HEADER), "Login link is not presented"

    def check_address_text_header(self):
        address_text = self.browser.find_element(*BasePageLocators.ADDRESS_TEXT_HEADER)
        assert address_text.text == "ул. Składowa 33, Przezmierowo", "The address text is different"

    def should_be_phone_text(self):
        assert self.is_element_present(*BasePageLocators.PHONE_NUMBER_HEADER), "Login link is not presented"

    def should_be_phone_icon(self):
        assert self.is_element_present(*BasePageLocators.PHONE_NUMBER_ICON_HEADER), "Login link is not presented"

    def check_phone_text_header(self):
        phone_number_text = self.browser.find_element(*BasePageLocators.PHONE_NUMBER_HEADER)
        assert phone_number_text.text == "+48 66 40 40 599", "The phone number text is different"

    def check_whatsapp_link_header(self):
        whatsapp_text = self.browser.find_element(*BasePageLocators.WHATSAPP_HEADER)
        assert (whatsapp_text.get_attribute('href')) == "https://api.whatsapp.com/send?phone=48664040599", \
            "The whatsapp link is different"

    def check_messenger_link_header(self):
        messenger_text = self.browser.find_element(*BasePageLocators.MESSENGER_HEADER)
        assert (messenger_text.get_attribute('href')) == "https://m.me/takservicepoznan", \
            "The messenger link is different"

    def check_message_in_cart(self):
        empty_cart_message = (self.browser.find_element(*BasePageLocators.CART_MESSAGE_EMPTY)).text
        assert "Your basket is empty" in empty_cart_message

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False
