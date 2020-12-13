from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")

    PRODUCT_FORM = (By.CSS_SELECTOR, ".product_main")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.TAG_NAME, "p.price_color")

    ALERT_MESSAGE = (By.CSS_SELECTOR, "#messages")
    MESSAGE_TEXT = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    MESSAGE_PRICE = (By.CSS_SELECTOR, ".alert-info strong")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-child(1)")
