import pytest

from .pages.base_page import generate_random_string
from final.pages.basket_page import BasketPage
from final.pages.login_page import LoginPage
from final.pages.product_page import ProductPage


class TestGuestProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Arrange
        product_page = ProductPage(browser)
        product_page.open()
        product_page.click_button_add_to_basket()
        product_page.click_button_view_basket()

    def test_guest_should_see_page_checkout(self, browser):  # гость должен увидеть страницу оформления заказа
        # Act
        basket_page = BasketPage(browser)
        basket_page.click_button_proceed_to_checkout()
        # Assert
        basket_page.should_be_checkout_form()  # должна быть форма оформления заказа
        basket_page.guest_should_see_header_message()  # гость должен увидеть заголовок сообщения

    @pytest.mark.xfail(reason="-- fixing this bug right now. --")
    def test_guest_should_see_empty_bucket(self, browser):  # гость должен увидеть пустую корзину
        # Act
        basket_page = BasketPage(browser)
        basket_page.click_button_remove()
        # Assert
        basket_page.should_be_success_message()  # должно быть сообщение об успехе
        basket_page.is_message_about_an_empty_bucket_present()  # присутствует ли сообщение о пустой корзине


@pytest.mark.User
class TestUserProductPage:
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

        product_page = ProductPage(browser)
        product_page.open()
        product_page.click_button_add_to_basket()
        product_page.click_button_view_basket()

    def test_user_should_see_page_checkout(self, browser):  # пользователь должен увидеть страницу оформления заказа
        # Act
        basket_page = BasketPage(browser)
        basket_page.click_button_proceed_to_checkout()
        # Assert
        basket_page.should_be_shipping_payment_form()
        basket_page.user_should_see_header_message()

    @pytest.mark.xfail(reason="-- fixing this bug right now. --")
    def test_user_should_see_empty_bucket(self, browser):  # пользователь должен увидеть пустую корзину
        # Act
        basket_page = BasketPage(browser)
        basket_page.click_button_remove()
        # Assert
        basket_page.should_be_success_message()  # должно быть сообщение об успехе
        basket_page.is_message_about_an_empty_bucket_present()  # присутствует ли сообщение о пустой корзине


class TestCreateNewUser:
    @pytest.mark.User
    def test_register_new_user(self, browser):  # регистрация нового пользователя
        # Data
        user_email = generate_random_string(8) + "@fakemail.org"
        user_password = generate_random_string(16)
        # Arrange
        login_page = LoginPage(browser)
        login_page.open()
        # Assert
        login_page.should_be_register_form()  # должна быть регистрационная форма
        login_page.register_new_user(user_email, user_password)
        login_page.should_be_authorized_user()  # должен быть авторизованный пользователь
        login_page.user_should_see_message_register()

    def test_user_login(self, browser):  # вход пользователя
        # Data
        test_user_email = "Myuser20@gmail.com"
        test_user_password = "Password2020"
        # Arrange
        login_page = LoginPage(browser)
        login_page.open()
        # Assert
        login_page.should_be_login_form()  # должна быть форма входа в систему
        login_page.user_login(test_user_email, test_user_password)
        login_page.should_be_authorized_user()  # должен быть авторизованный пользователь
        login_page.user_should_see_message_login()  # должно быть приветственное сообщение



