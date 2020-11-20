import random
import string
import time

from selenium import webdriver
import unittest


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


class TestRegister(unittest.TestCase):

    def test_new_user_registration(self):
        # Data
        login_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

        user_email = generate_random_string(8) + "@gmail.com"
        user_password1 = user_password2 = generate_random_string(16)

        email_input_locator = "id_registration-email"
        password1_input_locator = "id_registration-password1"
        password2_input_locator = "id_registration-password2"
        button_registration_locator = "registration_submit"
        messages_text_locator = "messages"

        expected_text = "Спасибо за регистрацию!"

        try:
            # Arrange
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get(login_page_link)

            email_input = browser.find_element_by_id(email_input_locator)
            email_input.send_keys(user_email)
            password1_input = browser.find_element_by_id(password1_input_locator)
            password1_input.send_keys(user_password1)
            password2_input = browser.find_element_by_id(password2_input_locator)
            password2_input.send_keys(user_password2)

            # Act
            button_registration = browser.find_element_by_name(button_registration_locator)
            button_registration.click()

            # Assert
            messages_text_elt = browser.find_element_by_id(messages_text_locator)
            messages_text = messages_text_elt.text

            self.assertIn(expected_text, messages_text, "No message about successful registration!!!")

        finally:
            time.sleep(5)
            browser.quit()

    def test_log_in(self):
        # Data
        login_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

        user_email = "Myuser20@gmail.com"
        user_password = "Password2020"

        email_input_locator = "id_login-username"
        password_input_locator = "id_login-password"
        button_registration_locator = "login_submit"
        messages_text_locator = "messages"

        expected_text = "Рады видеть вас снова"

        try:
            # Arrange
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get(login_page_link)

            email_input = browser.find_element_by_id(email_input_locator)
            email_input.send_keys(user_email)
            password_input = browser.find_element_by_id(password_input_locator)
            password_input.send_keys(user_password)

            # Act
            button_registration = browser.find_element_by_name(button_registration_locator)
            button_registration.click()

            # Assert
            messages_text_elt = browser.find_element_by_id(messages_text_locator)
            messages_text = messages_text_elt.text

            self.assertIn(expected_text, messages_text, "No message about successful login!!!")

        finally:
            time.sleep(5)
            browser.quit()


if __name__ == "__main__":
    unittest.main()
