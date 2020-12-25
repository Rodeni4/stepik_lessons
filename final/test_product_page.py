import pytest

from .pages.base_page import generate_random_string
from final.pages.basket_page import BasketPage
from final.pages.login_page import LoginPage
from final.pages.product_page import ProductPage


class TestGuestProductPage:
    # Data
    test_product_link = "hacking-exposed-wireless_209/"

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Arrange
        product_page = ProductPage(browser, self.test_product_link)
        product_page.open()
        product_page.click_button_add_to_basket()
        product_page.click_button_view_basket()

    def test_guest_should_see_page_checkout(self, browser):
        # Act
        basket_page = BasketPage(browser)
        basket_page.click_button_proceed_to_checkout()
        # Assert
        basket_page.should_be_checkout_form()
        basket_page.guest_should_see_header_message()

    @pytest.mark.xfail(reason="-- fixing this bug right now. --")
    def test_guest_should_see_empty_bucket(self, browser):
        # Act
        basket_page = BasketPage(browser)
        basket_page.click_button_remove()
        # Assert
        basket_page.should_be_success_message()
        basket_page.is_message_about_an_empty_bucket_present()


class TestUserProductPage:
    # Data
    test_product_link = "hacking-exposed-wireless_209/"

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Data
        test_user_email = "Myuser20@gmail.com"
        test_user_password = "Password2020"
        # Arrange
        login_page = LoginPage(browser)
        login_page.open()
        login_page.user_login(test_user_email, test_user_password)
        basket_page = BasketPage(browser)
        basket_page.open()
        basket_page.user_clear_basket()
        product_page = ProductPage(browser, self.test_product_link)
        product_page.open()
        product_page.click_button_add_to_basket()
        product_page.click_button_view_basket()

    @pytest.mark.User
    def test_user_should_see_page_checkout(self, browser):
        # Act
        basket_page = BasketPage(browser)
        basket_page.click_button_proceed_to_checkout()
        # Assert
        basket_page.should_be_shipping_payment_form()
        basket_page.user_should_see_header_message()

    @pytest.mark.xfail(reason="-- fixing this bug right now. --")
    def test_user_should_see_empty_bucket(self, browser):
        # Act
        basket_page = BasketPage(browser)
        basket_page.click_button_remove()
        # Assert
        basket_page.should_be_success_message()
        basket_page.is_message_about_an_empty_bucket_present()


class TestCreateNewUser:
    def test_register_new_user(self, browser):
        # Data
        user_email = generate_random_string(8) + "@fakemail.org"
        user_password = generate_random_string(16)
        # Act
        login_page = LoginPage(browser)
        login_page.open()
        # Assert
        login_page.should_be_register_form()
        login_page.register_new_user(user_email, user_password)
        login_page.should_be_authorized_user()
        login_page.user_should_see_message_register()

    def test_user_login(self, browser):
        # Data
        test_user_email = "Myuser20@gmail.com"
        test_user_password = "Password2020"
        # Act
        login_page = LoginPage(browser)
        login_page.open()
        # Assert
        login_page.should_be_login_form()
        login_page.user_login(test_user_email, test_user_password)
        login_page.should_be_authorized_user()
        login_page.user_should_see_message_login()

    def test_negative_register_new_user(self, browser):
        # Data
        user_email = generate_random_string(8) + "@fakemail.org"
        user_password = generate_random_string(16)
        repeat_user_password = generate_random_string(16)
        # Act
        login_page = LoginPage(browser)
        login_page.open()
        # Assert
        login_page.should_be_register_form()
        login_page.negative_register_new_user(user_email, user_password, repeat_user_password)
        login_page.should_see_alert_danger()
        login_page.should_see_error_text()


@pytest.mark.User
class TestProductParametrize:
    # Data
    @pytest.mark.parametrize('link_parametrize',
                             ["the-shellcoders-handbook_208/",
                              "hacking-exposed-wireless_209/",
                              "coders-at-work_207/"
                              ])
    def test_click_button_add_to_basket(self, browser, link_parametrize):
        # Arrange
        product_page = ProductPage(browser, link_parametrize)
        product_page.open()
        # Act
        product_page.click_button_add_to_basket()
        # Assert
        product_page.alert_should_added_your_basket()
