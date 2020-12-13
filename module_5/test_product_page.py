import pytest

from .pages.base_page import generate_random_string
from .pages.basket_page import BasketPage
from .pages.locators import BasePageLocators
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage

# Data
product_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


class TestProductPage:
    def test_guest_can_add_product_to_basket(self, browser):
        # Arrange
        product_page = ProductPage(browser, product_link)
        product_page.open()

        # Act
        product_page.add_product_to_basket()

        # Assert
        product_page.basket_should_contain_name_product()
        product_page.basket_should_contain_price_product()

    def test_guest_cant_see_success_message(self, browser):
        # Arrange
        product_page = ProductPage(browser, product_link)
        product_page.open()

        # Assert
        product_page.should_not_be_success_message()

    @pytest.mark.xfail(reason="Test is expected to fall.")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # Arrange
        product_page = ProductPage(browser, product_link)
        product_page.open()

        # Assert
        product_page.add_product_to_basket()
        product_page.should_not_be_success_message()

    @pytest.mark.xfail(reason="fixing this bug right now.")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # Arrange
        product_page = ProductPage(browser, product_link)
        product_page.open()

        # Assert
        product_page.add_product_to_basket()
        product_page.should_is_disappeared()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        # Arrange
        product_page = ProductPage(browser, product_link)
        product_page.open()

        # Assert
        product_page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        # Arrange
        product_page = ProductPage(browser, product_link)
        product_page.open()

        # Act
        product_page.go_to_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        # Arrange
        product_page = ProductPage(browser, product_link)
        product_page.open()

        # Act
        product_page.basket_opened()
        bucket_page = BasketPage(browser, browser.current_url)

        # Assert
        bucket_page.is_message_about_an_empty_bucket_present()
        bucket_page.basket_has_no_product()


@pytest.mark.login_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Data
        user_email = generate_random_string(8) + "@fakemail.org"
        user_password = generate_random_string(16)

        # Arrange
        main_page = MainPage(browser)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(user_email, user_password)
        yield
        product_page = ProductPage(browser, product_link)
        product_page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        # Arrange
        product_page = ProductPage(browser, product_link)
        product_page.open()

        # Act
        product_page.add_product_to_basket()

        # Assert
        product_page.basket_should_contain_name_product()
        product_page.basket_should_contain_price_product()

    def test_user_cant_see_success_message(self, browser):
        # Arrange
        product_page = ProductPage(browser, product_link)
        product_page.open()

        # Assert
        product_page.should_not_be_success_message()





