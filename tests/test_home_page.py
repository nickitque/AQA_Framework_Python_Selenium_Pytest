import pytest
from pages.main_page import MainPage
link = "https://takservice.pl/ru/"


# @pytest.mark.xfail
# def test_guest_can_go_to_login_page(browser):
#     page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()  # открываем страницу
#     page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
#     page.should_be_login_page()


def test_guest_should_see_address_text(browser):
    page = MainPage(browser, link) #initialize the Object, pass a driver instance to the constructor
    page.open()
    page.should_be_address_text()
    page.check_address_text_header()


def test_guest_should_see_address_icon(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_address_icon()


def test_guest_should_see_phone_text(browser):
    page = MainPage(browser, link) #initialize the Object, pass a driver instance to the constructor
    page.open()
    page.should_be_phone_text()
    page.check_phone_text_header()


def test_guest_should_see_phone_icon(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_phone_icon()

def test_guest_should_see_whatsapp_icon(browser):
    page = MainPage(browser, link)
    page.open()
    page.check_whatsapp_link_header()