import pytest
from pages.home_page import HomePage
link = "https://takservice.pl/ru/"


# @pytest.mark.skip(reason=None):
def test_guest_can_visit_home_page(browser):
    """Opening the page."""
    page = HomePage(browser, link)
    page.open()


def test_guest_should_see_address_text(browser):
    """Test for validating address text in header."""
    page = HomePage(browser, link)  # initialize the Object, pass a driver instance to the constructor
    page.open()
    page.should_be_address_text()
    page.check_address_text_header()


def test_guest_should_see_address_icon(browser):
    """Test to validate the presence of icon."""
    page = HomePage(browser, link)
    page.open()
    page.should_be_address_icon()


def test_guest_should_see_phone_text(browser):
    """Test to validate the presence of phone number text and validation."""
    page = HomePage(browser, link)  # initialize the Object, pass a driver instance to the constructor
    page.open()
    page.should_be_phone_text()
    page.check_phone_text_header()


def test_guest_should_see_phone_icon(browser):
    """Test to validate the presence of icon."""
    page = HomePage(browser, link)
    page.open()
    page.should_be_phone_icon()


def test_guest_should_see_whatsapp_icon(browser):
    """Test to validate the presence of icon."""
    page = HomePage(browser, link)
    page.open()
    page.check_whatsapp_link_header()


def test_guest_can_click_logo_in_header(browser):
    """Test for clicking the icon in header and validating browser url after click."""
    page = HomePage(browser, link)
    page.open()
    page.click_logo_header()
    page.check_url_in_logo_header()


def test_guest_can_click_services_in_header(browser):
    """Test for clicking the services btn and validating the url (the url should have anchor)."""
    page = HomePage(browser, link)
    page.open()
    page.click_services_header()


def test_guest_can_click_about_us_in_header(browser):
    """Test for clicking the services btn and validating the url (the url should have anchor)."""
    page = HomePage(browser, link)
    page.open()
    page.click_about_us_header()


def test_guest_can_click_reviews_in_header(browser):
    """Test for clicking the services btn and validating the url (the url should have anchor)."""
    page = HomePage(browser, link)
    page.open()
    page.click_reviews_header()


def test_guest_can_click_contacts_in_header(browser):
    """Test for clicking the services btn and validating the url (the url should have anchor)."""
    page = HomePage(browser, link)
    page.open()
    page.click_contacts_header()


def test_guest_can_click_call_me_back_and_send_valid_data_to_cf(browser):
    """Test for clicking the call me back btn, filling and sending CF in Pop-up."""
    page = HomePage(browser, link)
    page.open()
    page.click_call_back_header()
    page.fill_popup_contact_form_valid_data()


def test_guest_can_click_signup_btn_and_send_cf(browser):
    """Test for clicking the call me back btn, filling and sending CF."""
    page = HomePage(browser, link)
    page.open()
    page.click_sign_up_button()
    # page.fill_contact_form_homepage()


def test_guest_can_click_first_promotion_card(browser):
    """Test for clicking the 1st promotion card."""
    page = HomePage(browser, link)
    page.open()
    page.click_first_promotion_card()


def test_guest_can_click_second_promotion_card(browser):
    """Test for clicking the 2nd promotion card."""
    page = HomePage(browser, link)
    page.open()
    page.click_second_promotion_card()


def test_guest_can_click_third_promotion_card(browser):
    """Test for clicking the 3rd promotion card."""
    page = HomePage(browser, link)
    page.open()
    page.click_third_promotion_card()


def test_guest_can_click_fourth_promotion_card(browser):
    """Test for clicking the 4th promotion card."""
    page = HomePage(browser, link)
    page.open()
    page.click_fourth_promotion_card()
