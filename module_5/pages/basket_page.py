from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def is_message_about_an_empty_bucket_present(self):
        # Data
        empty_message_template = "Your basket is empty"

        # Assert
        is_empty_basket_msg_present = self.is_element_present(*BasePageLocators.EMPTY_BASKET_MESSAGE)
        assert is_empty_basket_msg_present, "-- Message to bucket is not presented --"

        actual_message_text = self.browser.find_element(*BasePageLocators.EMPTY_BASKET_MESSAGE).text
        assert empty_message_template in actual_message_text, \
            f"{empty_message_template} -- Text message to bucket is not presented -- {actual_message_text}"

    def basket_has_no_product(self):
        # Assert
        is_not_basket_has_product = self.is_not_element_present(*BasePageLocators.BASKET_ITEMS)
        assert is_not_basket_has_product, "-- Basket should not contain any goods, but it does --"
