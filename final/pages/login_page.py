from final.pages.base_page import BasePage
from final.pages.locators import LoginPageLocators


class LoginPage(BasePage):
    # Data
    login_link = "http://selenium1py.pythonanywhere.com/accounts/login/"

    dictionary_login = {
        "ru": {
            "message_login": "Рады видеть вас снова",
            "message_register": "Спасибо за регистрацию!"
        },
        "en-GB": {
            "message_login": "Welcome back",
            "message_register": "Thanks for registering!"
        }
    }

    def __init__(self, browser):
        super(LoginPage, self).__init__(browser, self.login_link)

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

    def user_login(self, email, password):
        # Arrange
        user_email_input = self.browser.find_element(*LoginPageLocators.USER_EMAIL_INPUT)
        user_email_input.send_keys(email)
        user_password_input = self.browser.find_element(*LoginPageLocators.USER_PASSWORD_INPUT)
        user_password_input.send_keys(password)
        # Act
        button_registration = self.browser.find_element(*LoginPageLocators.BUTTON_LOGIN)
        button_registration.click()

    def should_be_login_form(self):  # должна быть форма входа в систему
        # Assert
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "-- Login form is not presented"

    def should_be_register_form(self):  # должна быть регистрационная форма
        # Assert
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "-- Register form is not presented"

    def user_should_see_message_login(self):
        # Data
        language_value = self.browser.language_user

        expected_message = self.dictionary_login.get(language_value)["message_login"]
        actual_message_text = self.browser.find_element(*LoginPageLocators.GREEN_MESSAGE).text
        print("Expected result, message text - " + expected_message)
        # Assert
        assert expected_message in actual_message_text, \
            f"{expected_message} -- Login message is different -- {actual_message_text}"

    def user_should_see_message_register(self):
        # Data
        language_value = self.browser.language_user

        expected_message = self.dictionary_login.get(language_value)["message_register"]
        actual_message_text = self.browser.find_element(*LoginPageLocators.GREEN_MESSAGE).text
        print("Expected result, message text - " + expected_message)
        # Assert
        assert expected_message in actual_message_text, \
            f"{expected_message} -- Register message is different -- {actual_message_text}"
