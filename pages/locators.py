from selenium.webdriver.common.by import By


class BasePageLocators:
    ADDRESS_TEXT_HEADER = (By.CSS_SELECTOR, "#wrapper-navbar > div.header1.header > div > ul > li:nth-child(2)")
    ADDRESS_ICON_HEADER = (By.CSS_SELECTOR, "#wrapper-navbar > div.header1.header > div > ul > li:nth-child(2) > img")
    PHONE_NUMBER_HEADER = (By.CSS_SELECTOR, "#wrapper-navbar > div.header1.header > div > ul > li.phone > a > span")
    PHONE_NUMBER_ICON_HEADER = (By.CSS_SELECTOR, "#wrapper-navbar > div.header1.header > div > ul > li.phone > a > img")
    EMAIL_HEADER = (By.CSS_SELECTOR, "#wrapper-navbar > div.header1.header > div > ul > li:nth-child(4) > a > span")
    WHATSAPP_HEADER = (By.CSS_SELECTOR, "#wrapper-navbar > div.header1.header > div > div > ul > li:nth-child(1) > a")
    MESSENGER_HEADER = (By.CSS_SELECTOR, "#wrapper-navbar > div.header1.header > div > div > ul > li:nth-child(2) > a")
    LOGO_HEADER = (By.CSS_SELECTOR, "#wrapper-navbar > div.header.header2 > div > div.left_piece > a")
    SERVICES_HEADER = (By.CSS_SELECTOR, "#menu-item-51 > a")
    ABOUT_US_HEADER = (By.CSS_SELECTOR, "#menu-item-49 > a")
    REVIEWS_HEADER = (By.CSS_SELECTOR, "#menu-item-52 > a")
    CONTACTS_HEADER = (By.CSS_SELECTOR, "#menu-item-53 > a")
    CALL_BACK_HEADER = (By.CSS_SELECTOR, "#wrapper-navbar > div.header.header2 > div > button")
    POPUP_NAME_FIELD = (By.CSS_SELECTOR, "#wpcf7-f182-o2 > form > label:nth-child(2) > span > input")
    POPUP_PHONE_FIELD = (By.CSS_SELECTOR, "#wpcf7-f182-o2 > form > label:nth-child(3) > span > input")
    POPUP_MESSAGE_FIELD = (By.CSS_SELECTOR, "#wpcf7-f182-o2 > form > label.textarea-label > span > textarea")
    POPUP_SEND_BTN = (By.CSS_SELECTOR, "#wpcf7-f182-o2 > form > input")


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")

    """Слекторы полей формы регистрации"""
    LOGIN_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")

    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
    LOGIN_IMAGE = (By.CSS_SELECTOR, ".icon-user")


class ProductPageLocators:
    ADD_TO_CART = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    SUCCESS_MESSAGE = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div")
    ALERT_INNER_DISCOUNT = (By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/div")
    SUCCESS_MASSAGE_LINK = (By.CSS_SELECTOR, ".alert-success")


class BasketPageLocators:
    CART_MESSAGE_EMPTY = (By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/p")
