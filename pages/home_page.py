from .base_page import BasePage
from .locators import HomePageLocators
import time


class HomePage(BasePage):
    def __init__(self, *args, **kwargs):
        super(HomePage, self).__init__(*args, **kwargs)

    def click_sign_up_button(self):
        self.browser.find_element(*HomePageLocators.SIGN_UP_BTN).click()

    def fill_contact_form_homepage(self):
        self.browser.find_element(*HomePageLocators.CF_NAME_FIELD).send_keys("Nikita_test")
        self.browser.find_element(*HomePageLocators.CF_PHONE_FIELD).send_keys("+48 111 111 111")
        self.browser.find_element(*HomePageLocators.CF_MESSAGE_FIELD).send_keys("Test with using Python and selenium.")
        self.browser.find_element(*HomePageLocators.CF_SEND_BTN).click()

    def click_first_promotion_card(self):
        self.browser.find_element(*HomePageLocators.FIRST_PROMOTION).click()
        assert self.browser.title == "Комплексное обслуживание (ТО) автомобиля с выгодой 15% - TAK Service"

    def click_second_promotion_card(self):
        self.browser.find_element(*HomePageLocators.SECOND_PROMOTION).click()
        assert self.browser.title == "Комплексная проверка автомобиля за 0 zl - TAK Service"

    def click_third_promotion_card(self):
        self.browser.find_element(*HomePageLocators.THIRD_PROMOTION).click()
        assert self.browser.title == "Компьютерная диагностика за 0 zl - TAK Service"

    def click_fourth_promotion_card(self):
        self.browser.find_element(*HomePageLocators.FOURTH_PROMOTION).click()
        assert self.browser.title == 'Программа лояльности "Так Клуб" - TAK Service'