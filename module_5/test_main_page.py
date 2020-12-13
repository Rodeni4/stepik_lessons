from .pages.login_page import LoginPage
from .pages.main_page import MainPage


class TestMainPage:

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser)
        page.open()
        page.should_be_login_link()


class TestLoginPage:
    def test_quest_should_be_login_url(self, browser):
        page = MainPage(browser)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_url()

    def test_quest_should_be_login_form(self, browser):
        page = MainPage(browser)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_form()

    def test_quest_should_be_register_form(self, browser):
        page = MainPage(browser)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_register_form()
