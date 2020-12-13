from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):

        # Assert
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        #Data
        expected_result = "login"
        url_browser = self.browser.current_url

        # Assert
        assert expected_result in url_browser, \
            f"{expected_result} -- String is not in url of browser -- {url_browser}"

    def should_be_login_form(self):
        # Assert
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # Assert
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        # Arrange
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)
        repeat_password_input = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_INPUT)
        repeat_password_input.send_keys(password)

        # Act
        button_registration = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION)
        button_registration.click()
