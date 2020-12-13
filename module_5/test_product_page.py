import pytest

from .pages.product_page import ProductPage

product_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


class TestProductPage:
    def test_guest_can_add_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, product_link)
        page.open()

        # Act
        page.add_product_to_basket()

        # Assert
        page.basket_should_contain_name_product()
        page.basket_should_contain_price_product()

    @pytest.mark.xfail(reason="Test is expected to fall.")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.add_product_to_basket()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail(reason="fixing this bug right now.")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.add_product_to_basket()
        page.should_is_disappeared()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.go_to_login_page()



