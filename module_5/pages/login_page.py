from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):

        # Assert
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # Assert
        assert "login" in self.browser.current_url, "String 'login' is not in current url of browser"

    def should_be_login_form(self):
        # Assert
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # Assert
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
