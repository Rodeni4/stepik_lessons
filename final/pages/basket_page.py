from final.pages.base_page import BasePage
from final.pages.locators import BasketPageLocators


class BasketPage(BasePage):
    # Data
    basket_link = "http://selenium1py.pythonanywhere.com/basket/"

    dictionary = {
        "ru": {
            "guest_header_message": "Кто Вы?",
            "user_header_message": "Адрес доставки",
            "message_template": "Ваша корзина пуста"
        },
        "en-GB": {
            "guest_header_message": "Who are you?",
            "user_header_message": "Shipping address",
            "message_template": "Your basket is empty"
        }
    }

    def __init__(self, browser):
        super(BasketPage, self).__init__(browser, self.basket_link)

    def click_button_proceed_to_checkout(self):
        # Act
        click_button = self.browser.find_element(*BasketPageLocators.BTN_PROCEED_TO_CHECKOUT)
        click_button.click()

    def click_button_remove(self):
        # Act
        click_btn_remove = self.browser.find_element(*BasketPageLocators.BTN_REMOVE)
        click_btn_remove.click()

    def should_be_checkout_form(self):
        # Assert
        assert self.is_element_present(*BasketPageLocators.CHECKOUT_FORM), \
            "-- Checkout form is not presented --"  # Форма оформления заказа не представлена

    def should_be_shipping_payment_form(self):  # должна быть форма доставки-оплаты
        # Assert
        assert self.is_element_present(*BasketPageLocators.SHIPPING_PAYMENT_FORM), \
            "-- Shipping-payment form is not presented --"  # Форма доставки-оплаты не представлена

    def guest_should_see_header_message(self):
        # Data
        language_value = self.browser.language_user

        expected_message = self.dictionary.get(language_value)["guest_header_message"]
        header_message = self.browser.find_element(*BasketPageLocators.HEADER_MESSAGE).text
        print("Expected result, message text - " + expected_message)
        # Assert
        assert self.is_element_present(*BasketPageLocators.HEADER_MESSAGE), \
            "-- Header message is not presented --"  # Заголовок сообщения не представлен
        assert expected_message in header_message, \
            f"{expected_message} -- Header message is different -- {header_message}"  # Заголовок сообщения отличается

    def user_should_see_header_message(self):  # пользователь должен увидеть заголовок сообщения
        # Data
        language_value = self.browser.language_user

        expected_message = self.dictionary.get(language_value)["user_header_message"]
        header_message = self.browser.find_element(*BasketPageLocators.HEADER_MESSAGE).text
        print("Expected result, message text - " + expected_message)
        # Assert
        assert self.is_element_present(*BasketPageLocators.HEADER_MESSAGE), \
            "-- Header message is not presented"  # Заголовок сообщения не представлен
        assert expected_message in header_message, \
            f"{expected_message} -- Header message is different -- {header_message}"
        # Заголовок сообщения отличается

    def should_be_success_message(self):  # должно быть сообщение об успехе
        # Assert
        assert self.is_element_present(*BasketPageLocators.SUCCESS_MESSAGE), \
            " -- Success remove message not presented"  # Успешное удаление, сообщение не представлено

    def is_message_about_an_empty_bucket_present(self):  # присутствует ли сообщение о пустой корзине
        # Data
        language_value = self.browser.language_user

        empty_message_template = self.dictionary.get(language_value)["message_template"]
        actual_message_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        print("Expected result, message text - " + empty_message_template)
        # Assert
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "-- Message to bucket is not presented --"  # Сообщение о корзине не представлено

        assert empty_message_template in actual_message_text, \
            f"{empty_message_template} -- Text message to bucket is different -- {actual_message_text}"
        # Текстовое сообщение совсем другое

    def user_clear_basket(self):  # пользователь очищает корзину
        # Act
        while self.is_element_present(*BasketPageLocators.BASKET_ITEMS):
            form_quantity = self.browser.find_element(*BasketPageLocators.FORM_QUANTITY)
            form_quantity.click()
            form_quantity.clear()
            form_quantity.send_keys(0)
            button_update = self.browser.find_element(*BasketPageLocators.BUTTON_UPDATE)
            button_update.click()
        # Assert
        self.is_message_about_an_empty_bucket_present()
