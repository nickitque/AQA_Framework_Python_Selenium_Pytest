from .base_page import BasePage
from .locators import Page404Locators


class Page404(BasePage):

    def click_back_to_homepage_button(self):
        self.browser.find_element(*Page404Locators.BACK_TO_HOMEPAGE_BTN).click()
        assert self.browser.current_url == "https://takservice.pl/ru/", "The url is not https://takservice.pl/ru/"

    def check_subtitle_text(self):
        subtitle_text = self.browser.find_element(*Page404Locators.SUBTITLE)
        assert subtitle_text.text == "Страница не найдена", "There subtitle text is not 'Страница не найдена'."

    def check_error_code_text(self):
        error_code_text = self.browser.find_element(*Page404Locators.ERROR_CODE)
        assert error_code_text.text == "404", "There subtitle text is not '404'."

    def check_message_text(self):
        message_text = self.browser.find_element(*Page404Locators.MESSAGE)
        assert message_text.text == "Упс! Что-то пошло не так, этой страницы не существует", \
            "There subtitle text is not 'Упс! Что-то пошло не так, этой страницы не существует'."
