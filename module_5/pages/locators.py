from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTRATION = (By.NAME, "registration_submit")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")

    PRODUCT_FORM = (By.CSS_SELECTOR, ".product_main")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.TAG_NAME, "p.price_color")

    ALERT_MESSAGE = (By.CSS_SELECTOR, "#messages")
    MESSAGE_TEXT = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    MESSAGE_PRICE = (By.CSS_SELECTOR, ".alert-info strong")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-child(1)")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    BUTTON_BASKET_OPENED = (By.CSS_SELECTOR, ".row a.btn-default")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner")

    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
