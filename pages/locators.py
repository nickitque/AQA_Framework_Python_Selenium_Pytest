from selenium.webdriver.common.by import By


class BasePageLocators:
    ADDRESS_TEXT_HEADER = (By.CSS_SELECTOR, "#wrapper-navbar > div.header1.header > div > ul > li:nth-child(2)")
    ADDRESS_ICON_HEADER = (By.CSS_SELECTOR, "#wrapper-navbar > div.header1.header > div > ul > li:nth-child(2) > img")
    PHONE_NUMBER_HEADER = (By.CSS_SELECTOR, "#wrapper-navbar > div.header1.header > div > ul > li.phone > a > span")
    PHONE_NUMBER_ICON_HEADER = (By.CSS_SELECTOR, "#wrapper-navbar > div.header1.header > div > ul > li.phone > a > img")
    EMAIL_HEADER = (By.CSS_SELECTOR, "#wrapper-navbar > div.header1.header > div > ul > li:nth-child(4) > a > span")
    WHATSAPP_BTN_HEADER = (By.CSS_SELECTOR, "#wrapper-navbar > div.header1.header > div > div > ul > li:nth-child(1) > a")
    MESSENGER_BTN_HEADER = (By.CSS_SELECTOR, "#wrapper-navbar > div.header1.header > div > div > ul > li:nth-child(2) > a")
    LOGO_HEADER = (By.CSS_SELECTOR, "#wrapper-navbar > div.header.header2 > div > div.left_piece > a")
    SERVICES_BTN_HEADER = (By.CSS_SELECTOR, "#menu-item-51 > a")
    ABOUT_US_BTN_HEADER = (By.CSS_SELECTOR, "#menu-item-49 > a")
    REVIEWS_BTN_HEADER = (By.CSS_SELECTOR, "#menu-item-52 > a")
    CONTACTS_BTN_HEADER = (By.CSS_SELECTOR, "#menu-item-53 > a")
    CALL_BACK_BTN_HEADER = (By.CSS_SELECTOR, "#wrapper-navbar > div.header.header2 > div > button")
    POPUP_NAME_FIELD = (By.CSS_SELECTOR, "#wpcf7-f182-o2 > form > label:nth-child(2) > span > input")
    POPUP_PHONE_FIELD = (By.CSS_SELECTOR, "#wpcf7-f182-o2 > form > label:nth-child(3) > span > input")
    POPUP_MESSAGE_FIELD = (By.CSS_SELECTOR, "#wpcf7-f182-o2 > form > label.textarea-label > span > textarea")
    POPUP_SEND_BTN = (By.CSS_SELECTOR, "#wpcf7-f182-o2 > form > input")


class HomePageLocators:
    SIGN_UP_BTN = (By.CSS_SELECTOR, "#main-section > div > div > div.grid-bonus__content > a")
    CF_NAME_FIELD = (By.CSS_SELECTOR, "#wpcf7-f179-o1 > form > label:nth-child(2) > span > input")
    CF_PHONE_FIELD = (By.CSS_SELECTOR, "#wpcf7-f179-o1 > form > label:nth-child(3) > span > input")
    CF_MESSAGE_FIELD = (By.CSS_SELECTOR, "#wpcf7-f179-o1 > form > label.textarea-label > span > textarea")
    CF_SEND_BTN = (By.CSS_SELECTOR, "#wpcf7-f179-o1 > form > input")
    FIRST_PROMOTION = (By.CSS_SELECTOR, "#other_deals > div > ul > li:nth-child(1) > a")
    SECOND_PROMOTION = (By.CSS_SELECTOR, "#other_deals > div > ul > li:nth-child(2) > a")
    THIRD_PROMOTION = (By.CSS_SELECTOR, "#other_deals > div > ul > li:nth-child(3) > a")
    FOURTH_PROMOTION = (By.CSS_SELECTOR, "#other_deals > div > ul > li:nth-child(4) > a")


class PromotionsPageLocators:
    PROMOTION_DUE_DATE = (By.CSS_SELECTOR, "#page > main > section.main_section_deals > div:nth-child(1) > p")
    BACK_TO_HOMEPAGE_BTN = (By.CSS_SELECTOR, "#page > main > section.main_section_deals > div:nth-child(1) > a")