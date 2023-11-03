import pytest
from pages.home_page import HomePage
link = "https://takservice.pl/ru/"


@pytest.mark.skip(reason=None)
def test_guest_can_visit_home_page(browser):
    page = HomePage(browser, link)
    page.open()


def test_guest_should_see_address_text(browser):
    page = HomePage(browser, link)  # initialize the Object, pass a driver instance to the constructor
    page.open()
    page.should_be_address_text()
    page.check_address_text_header()


def test_guest_should_see_address_icon(browser):
    page = HomePage(browser, link)
    page.open()
    page.should_be_address_icon()


def test_guest_should_see_phone_text(browser):
    page = HomePage(browser, link)  # initialize the Object, pass a driver instance to the constructor
    page.open()
    page.should_be_phone_text()
    page.check_phone_text_header()


def test_guest_should_see_phone_icon(browser):
    page = HomePage(browser, link)
    page.open()
    page.should_be_phone_icon()


def test_guest_should_see_whatsapp_icon(browser):
    page = HomePage(browser, link)
    page.open()
    page.check_whatsapp_link_header()


def test_guest_can_click_logo_in_header(browser):
    page = HomePage(browser, link)
    page.open()
    page.click_logo_header()
    page.check_url_in_logo_header()


def test_guest_can_click_services_in_header(browser):
    page = HomePage(browser, link)
    page.open()
    page.click_services_header()


def test_guest_can_click_about_us_in_header(browser):
    page = HomePage(browser, link)
    page.open()
    page.click_about_us_header()


def test_guest_can_click_reviews_in_header(browser):
    page = HomePage(browser, link)
    page.open()
    page.click_reviews_header()


def test_guest_can_click_contacts_in_header(browser):
    page = HomePage(browser, link)
    page.open()
    page.click_contacts_header()


def test_guest_can_click_call_me_back_and_send_valid_data_to_cf(browser):
    page = HomePage(browser, link)
    page.open()
    page.click_call_back_header()
    page.fill_popup_contact_form_valid_data()


def test_guest_can_click_signup_btn_and_send_cf(browser):
    page = HomePage(browser, link)
    page.open()
    page.click_sign_up_button()
    # page.fill_contact_form_homepage()

def test_guest_can_click_first_promotion_card(browser):
    page = HomePage(browser, link)
    page.open()
    page.click_first_promotion_card()


def test_guest_can_click_second_promotion_card(browser):
    page = HomePage(browser, link)
    page.open()
    page.click_second_promotion_card()


def test_guest_can_click_third_promotion_card(browser):
    page = HomePage(browser, link)
    page.open()
    page.click_third_promotion_card()


def test_guest_can_click_fourth_promotion_card(browser):
    page = HomePage(browser, link)
    page.open()
    page.click_fourth_promotion_card()

