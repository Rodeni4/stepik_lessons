from selenium.webdriver.common.by import By


class BasePageLocators:
    BUTTON_VIEW_BASKET = (By.CSS_SELECTOR, ".row a.btn-default")

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BTN_PROCEED_TO_CHECKOUT = (By.CSS_SELECTOR, ".btn-block")
    BTN_REMOVE = (By.CSS_SELECTOR, ".inline")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-child(1)")

    CHECKOUT_FORM = (By.CSS_SELECTOR, ".form-stacked.well")
    HEADER_MESSAGE = (By.CSS_SELECTOR, ".sub-header")

    SHIPPING_PAYMENT_FORM = (By.CSS_SELECTOR, ".shipping-payment")

    FORM_QUANTITY = (By.CSS_SELECTOR, ".input-group .form-control")
    BUTTON_UPDATE = (By.CSS_SELECTOR, ".input-group-btn")

    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTRATION = (By.NAME, "registration_submit")

    USER_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_login-username")
    USER_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_login-password")
    BUTTON_LOGIN = (By.NAME, "login_submit")

    GREEN_MESSAGE = (By.CSS_SELECTOR, ".alertinner.wicon")





