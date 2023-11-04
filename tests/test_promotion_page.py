import pytest
from pages.promotions_page import PromotionsPage

link = "https://takservice.pl/ru/deals/"
endpoints = ["to15/", "check0zl/", "diagnostics0zl/", "takclub/"]


def test_guest_can_visit_home_page_from_first_endpoint(browser):
    page = PromotionsPage(browser, link + endpoints[0])
    page.open()
    page.click_back_to_homepage_button()


def test_guest_can_visit_home_page_from_second_endpoint(browser):
    page = PromotionsPage(browser, link + endpoints[1])
    page.open()
    page.click_back_to_homepage_button()


def test_guest_can_visit_home_page_from_third_endpoint(browser):
    page = PromotionsPage(browser, link + endpoints[2])
    page.open()
    page.click_back_to_homepage_button()


def test_guest_can_visit_home_page_from_fourth_endpoint(browser):
    page = PromotionsPage(browser, link + endpoints[3])
    page.open()
    page.click_back_to_homepage_button()


def test_guest_can_click_call_back_button_and_fill_cf(browser):
    page = PromotionsPage(browser, link + endpoints[0])
    page.open()
    page.click_call_back_header()
    page.fill_popup_contact_form_valid_data()
    #needs update because of the selectors