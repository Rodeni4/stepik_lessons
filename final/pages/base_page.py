import random
import string

from selenium.common.exceptions import NoSuchElementException
from final.pages.locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)  # для неявного ожидания

    def open(self):
        # Act
        self.browser.get(self.url)

    def click_button_view_basket(self):
        # Act
        button_view_basket = self.browser.find_element(*BasePageLocators.BUTTON_VIEW_BASKET)
        button_view_basket.click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def should_be_authorized_user(self):  # должен быть авторизованный пользователь
        # Assert
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            "User icon is not presented probably unauthorised user"


# Data
def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string
