from final.pages.base_page import BasePage
from final.pages.locators import LoginPageLocators


class LoginPage(BasePage):
    login_link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    dictionary_login = {
        "ru": {
            "message_login": "Рады видеть вас снова",
            "message_register": "Спасибо за регистрацию!",
            "message_alert_danger": "Опаньки! Мы нашли какие-то ошибки",
            "error_text": "Два поля с паролями не совпадают"
        },
        "en-GB": {
            "message_login": "Welcome back",
            "message_register": "Thanks for registering!",
            "message_alert_danger": "Oops! We found some errors",
            "error_text": "The two password fields didn't match"
        }
    }

    def __init__(self, browser):
        super(LoginPage, self).__init__(browser, self.login_link)

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)
        repeat_password_input = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_INPUT)
        repeat_password_input.send_keys(password)
        button_registration = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION)
        button_registration.click()

    def negative_register_new_user(self, email, password1, password2):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password1)
        repeat_password_input = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_INPUT)
        repeat_password_input.send_keys(password2)
        button_registration = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION)
        button_registration.click()

    def user_login(self, email, password):
        user_email_input = self.browser.find_element(*LoginPageLocators.USER_EMAIL_INPUT)
        user_email_input.send_keys(email)
        user_password_input = self.browser.find_element(*LoginPageLocators.USER_PASSWORD_INPUT)
        user_password_input.send_keys(password)
        button_registration = self.browser.find_element(*LoginPageLocators.BUTTON_LOGIN)
        button_registration.click()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "-- Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "-- Register form is not presented"

    def user_should_see_message_login(self):
        language_value = self.browser.language_user
        expected_message = self.dictionary_login.get(language_value)["message_login"]
        actual_message_text = self.browser.find_element(*LoginPageLocators.GREEN_MESSAGE).text
        assert expected_message in actual_message_text, \
            f"{expected_message} -- Login message is different -- {actual_message_text}"

    def user_should_see_message_register(self):
        language_value = self.browser.language_user
        expected_message = self.dictionary_login.get(language_value)["message_register"]
        actual_message_text = self.browser.find_element(*LoginPageLocators.GREEN_MESSAGE).text
        assert expected_message in actual_message_text, \
            f"{expected_message} -- Register message is different -- {actual_message_text}"

    def should_see_alert_danger(self):
        language_value = self.browser.language_user
        expected_alert_danger = self.dictionary_login.get(language_value)["message_alert_danger"]
        actual_alert_danger = self.browser.find_element(*LoginPageLocators.ALERT_DANGER).text
        assert expected_alert_danger in actual_alert_danger, \
            f"{expected_alert_danger} -- Alert danger message is different -- {actual_alert_danger}"

    def should_see_error_text(self):
        language_value = self.browser.language_user
        expected_error_text = self.dictionary_login.get(language_value)["error_text"]
        actual_error_text = self.browser.find_element(*LoginPageLocators.ERROR_TEXT).text
        assert expected_error_text in actual_error_text, \
            f"{expected_error_text} -- Error text message is different -- {actual_error_text}"
