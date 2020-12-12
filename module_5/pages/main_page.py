from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    link = "http://selenium1py.pythonanywhere.com/"

    def __init__(self, browser):
        super(MainPage, self).__init__(browser, self.link)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"


