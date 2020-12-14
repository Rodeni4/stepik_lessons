import random
import string
import unittest

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


class TestRegister(unittest.TestCase):

    def test_new_user_registration(self):
        # Data
        login_page_link = "http://selenium1py.pythonanywhere.com/accounts/login/"

        user_email = generate_random_string(8) + "@gmail.com"
        user_password = user_repeat_password = generate_random_string(16)

        email_input_locator = "id_registration-email"
        password_input_locator = "id_registration-password1"
        repeat_password_input_locator = "id_registration-password2"
        button_registration_locator = "registration_submit"
        successful_message_locator = "messages"

        expected_text = "Спасибо за регистрацию!"

        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(login_page_link)

        try:
            # Arrange
            email_input = browser.find_element_by_id(email_input_locator)
            email_input.send_keys(user_email)
            password_input = browser.find_element_by_id(password_input_locator)
            password_input.send_keys(user_password)
            repeat_password_input = browser.find_element_by_id(repeat_password_input_locator)
            repeat_password_input.send_keys(user_repeat_password)

            # Act
            button_registration = browser.find_element_by_name(button_registration_locator)
            button_registration.click()

            # Assert
            successful_message = browser.find_element_by_id(successful_message_locator)
            successful_message_text = successful_message.text

            self.assertIn(expected_text, successful_message_text, "No message about successful registration!!!")

        finally:
            browser.quit()

    def test_log_in(self):
        # Data
        login_page_link = "http://selenium1py.pythonanywhere.com/accounts/login/"

        user_email = "Myuser20@gmail.com"
        user_password = "Password2020"

        email_input_locator = "id_login-username"
        password_input_locator = "id_login-password"
        button_registration_locator = "login_submit"
        successful_message_locator = "messages"

        expected_text = "Рады видеть вас снова"

        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(login_page_link)

        try:
            # Arrange
            email_input = browser.find_element_by_id(email_input_locator)
            email_input.send_keys(user_email)
            password_input = browser.find_element_by_id(password_input_locator)
            password_input.send_keys(user_password)

            # Act
            button_registration = browser.find_element_by_name(button_registration_locator)
            button_registration.click()

            # Assert
            successful_message = browser.find_element_by_id(successful_message_locator)
            successful_message_text = successful_message.text

            self.assertIn(expected_text, successful_message_text, "No message about successful login!!!")

        finally:
            browser.quit()


class TestDeleteProduct(unittest.TestCase):
    @unittest.skip("Temporarily skip - error working with the 'Delete' link")
    def test_delete_product(self):
        # Data
        catalog_page_link = "http://selenium1py.pythonanywhere.com/catalogue/"

        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(catalog_page_link)

        button_add_to_cart_locator = "li:nth-child(2) button"
        button_view_cart_locator = ".btn-info:nth-child(1)"
        button_delete_locator = "[data-behaviours='remove']"

        successful_message_locator = ".alertinner p"

        expected_text = "Ваша корзина теперь пуста"

        try:
            # Arrange
            button_add_to_cart = browser.find_element_by_css_selector(button_add_to_cart_locator)
            button_add_to_cart.click()

            button_view_cart = browser.find_element_by_css_selector(button_view_cart_locator)
            button_view_cart.click()

            # Act
            button_delete = browser.find_element_by_css_selector(button_delete_locator)
            button_delete.click()

            # Assert
            wait = WebDriverWait(browser, 10)
            successful_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, successful_message_locator)))
            successful_message_text = successful_message.text

            self.assertIn(expected_text, successful_message_text, "There is no message that the cart is empty")

        finally:
            browser.quit()

    def test_go_to_checkout(self):
        # Data
        login_page_link = "http://selenium1py.pythonanywhere.com/accounts/login/"

        user_email = "Myuser20@gmail.com"
        user_password = "Password2020"

        email_input_locator = "id_login-username"
        password_input_locator = "id_login-password"
        button_login_locator = "login_submit"
        menu_all_products_locator = "[data-navigation='dropdown-menu'] li:nth-child(1)"
        button_add_to_cart_locator = "li:nth-child(2) button"
        button_view_cart_locator = ".btn-info:nth-child(1)"
        button_checkout_locator = ".btn-block"
        successful_message_locator = ".sub-header"
        form_is_displayed_locator = ".well"
        expected_text = "Адрес доставки"

        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(login_page_link)

        try:
            # Arrange
            email_input = browser.find_element_by_id(email_input_locator)
            email_input.send_keys(user_email)
            password_input = browser.find_element_by_id(password_input_locator)
            password_input.send_keys(user_password)

            button_login = browser.find_element_by_name(button_login_locator)
            button_login.click()

            menu_all_products = browser.find_element_by_css_selector(menu_all_products_locator)
            menu_all_products.click()

            button_add_to_cart = browser.find_element_by_css_selector(button_add_to_cart_locator)
            button_add_to_cart.click()

            button_view_cart = browser.find_element_by_css_selector(button_view_cart_locator)
            button_view_cart.click()

            # Act
            button_checkout = browser.find_element_by_css_selector(button_checkout_locator)
            button_checkout.click()

            # Assert
            successful_message = browser.find_element_by_css_selector(successful_message_locator)
            successful_message_text = successful_message.text

            self.assertIn(expected_text, successful_message_text, "No such header")

            wait = WebDriverWait(browser, 10)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, form_is_displayed_locator)))

        finally:
            browser.quit()


if __name__ == "__main__":
    unittest.main()
