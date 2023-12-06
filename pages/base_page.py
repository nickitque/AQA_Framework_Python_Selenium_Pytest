from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from .locators import BasePageLocators
import time


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def should_be_address_text(self):
        assert self.is_element_present(*BasePageLocators.ADDRESS_TEXT_HEADER), "Address text is not presented"

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
        whatsapp_text = self.browser.find_element(*BasePageLocators.WHATSAPP_BTN_HEADER)
        assert (whatsapp_text.get_attribute('href')) == "https://api.whatsapp.com/send?phone=48664040599", \
            "The whatsapp link is different"

    def check_messenger_link_header(self):
        messenger_text = self.browser.find_element(*BasePageLocators.MESSENGER_BTN_HEADER)
        assert (messenger_text.get_attribute('href')) == "https://m.me/takservicepoznan", \
            "The messenger link is different"

    def click_logo_header(self):
        self.browser.find_element(*BasePageLocators.LOGO_HEADER).click()
        assert self.browser.current_url == "https://takservice.pl/ru/", "The url is not https://takservice.pl/ru/"

    def check_url_in_logo_header(self):
        logo_header = self.browser.find_element(*BasePageLocators.LOGO_HEADER)
        assert (logo_header.get_attribute('href')) == "https://takservice.pl/ru/", \
            "The logo link is not https://takservice.pl/ru/"

    def click_services_header(self):
        self.browser.find_element(*BasePageLocators.SERVICES_BTN_HEADER).click()
        assert self.browser.current_url == "https://takservice.pl/ru/#services_section", \
            "The url is not https://takservice.pl/ru/#services_section"

    def click_about_us_header(self):
        self.browser.find_element(*BasePageLocators.ABOUT_US_BTN_HEADER).click()
        assert self.browser.current_url == "https://takservice.pl/ru/#team_section", \
            "The url is not https://takservice.pl/ru/#team_section"

    def click_reviews_header(self):
        self.browser.find_element(*BasePageLocators.REVIEWS_BTN_HEADER).click()
        assert self.browser.current_url == "https://takservice.pl/ru/#testimonials_section", \
            "The url is not https://takservice.pl/ru/#testimonials_section"

    def click_contacts_header(self):
        self.browser.find_element(*BasePageLocators.CONTACTS_BTN_HEADER).click()
        assert self.browser.current_url == "https://takservice.pl/ru/#contact_section", \
            "The url is not https://takservice.pl/ru/#contact_section"

    def click_call_back_header(self):
        self.browser.find_element(*BasePageLocators.CALL_BACK_BTN_HEADER).click()

    def fill_popup_contact_form_valid_data(self):
        self.browser.find_element(*BasePageLocators.POPUP_NAME_FIELD).send_keys("Nikita_Test")
        self.browser.find_element(*BasePageLocators.POPUP_PHONE_FIELD).send_keys("+48 111 111 111")
        self.browser.find_element(*BasePageLocators.POPUP_MESSAGE_FIELD).send_keys("Test message using Python "
                                                                                   "and Selenium.")
        self.browser.find_element(*BasePageLocators.POPUP_SEND_BTN).click()
        time.sleep(5)
        # add assertion here

    def check_address_text_footer(self):
        address_text = self.browser.find_element(*BasePageLocators.ADDRESS_TEXT_FOOTER)
        assert address_text.text == "ул. Składowa 33, Przezmierowo", "The address number text is different"

    def check_working_hours_text_footer(self):
        working_hours_text = self.browser.find_element(*BasePageLocators.SCHEDULE_TEXT_FOOTER)
        assert working_hours_text.text == "Пн - Пт: 8:30 - 17:00", "The schedule text is different"

    def check_phone_text_footer(self):
        phone_number_text = self.browser.find_element(*BasePageLocators.PHONE_NUMBER_FOOTER)
        assert phone_number_text.text == "+48 66 40 40 599", "The phone number text is different"

    def check_email_text_footer(self):
        email_text = self.browser.find_element(*BasePageLocators.EMAIL_FOOTER)
        assert email_text.text == "info@takservice.com", "The email text is different"

    def check_info_text_footer(self):
        info_text = self.browser.find_element(*BasePageLocators.INFO_TEXT_FOOTER)
        result = " ".join(line.strip() for line in info_text.text.splitlines())
        assert result == "Tak Service Sp. z o.o. NIP: 7831866906 VAT: " \
                         "PL7831866906 REGON: 523481530 EORI: PL783186690600000", "The info text is different"

    def check_about_text_footer(self):
        about_text = self.browser.find_element(*BasePageLocators.ABOUT_TEXT_FOOTER)
        assert about_text.text == "СТО в Познани TAK service - надежный автосервис, предлагающий высококачественные услуги по ремонту " \
                                  "и обслуживанию автомобилей. Наша команда опытных специалистов обеспечит профессиональный подход к вашему автомобилю.", "The about text is different"

    def click_call_back_btn_footer(self):
        call_me_back_btn = self.browser.find_element(*BasePageLocators.CALL_BACK_BTN_FOOTER)
        call_me_back_btn.click()

    def click_instagram_btn_footer(self):
        email_text = self.browser.find_element(*BasePageLocators.EMAIL_FOOTER)
        assert email_text.text == "info@takservice.com", "The email text is different"

    def click_facebook_btn_footer(self):
        email_text = self.browser.find_element(*BasePageLocators.EMAIL_FOOTER)
        assert email_text.text == "info@takservice.com", "The email text is different"

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
