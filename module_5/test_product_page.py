import pytest

from .pages.basket_page import BasketPage
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

    @pytest.mark.xfail(reason="Test is expected to fall.")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # Arrange
        product_page = ProductPage(browser, product_link)
        product_page.open()

        # Assert
        product_page.add_product_to_basket()
        product_page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        # Arrange
        product_page = ProductPage(browser, product_link)
        product_page.open()

        # Assert
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




