from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage


class TestMainPage:

    def test_guest_can_go_to_login_page(self, browser):
        # Arrange
        main_page = MainPage(browser)
        main_page.open()

        # Act
        main_page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        # Arrange
        main_page = MainPage(browser)
        main_page.open()

        # Assert
        main_page.should_be_login_link()


class TestLoginPage:
    def test_quest_should_be_login_url(self, browser):
        # Arrange
        main_page = MainPage(browser)
        main_page.open()

        # Act
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)

        # Assert
        login_page.should_be_login_url()

    def test_quest_should_be_login_form(self, browser):
        # Arrange
        main_page = MainPage(browser)
        main_page.open()

        # Act
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)

        # Assert
        login_page.should_be_login_form()

    def test_quest_should_be_register_form(self, browser):
        # Arrange
        main_page = MainPage(browser)
        main_page.open()

        # Act
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)

        # Assert
        login_page.should_be_register_form()


class TestBasketPage:
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        # Arrange
        main_page = MainPage(browser)
        main_page.open()

        # Act
        main_page.basket_opened()
        bucket_page = BasketPage(browser, browser.current_url)

        # Assert
        bucket_page.is_message_about_an_empty_bucket_present()
        bucket_page.basket_has_no_product()


