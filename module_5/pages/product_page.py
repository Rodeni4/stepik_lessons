from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        # Act
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def basket_should_contain_name_product(self):
        # Act
        product_form = self.browser.find_element(*ProductPageLocators.PRODUCT_FORM)
        product_name = product_form.find_element(*ProductPageLocators.PRODUCT_NAME).text

        alert_message = self.browser.find_element(*ProductPageLocators.ALERT_MESSAGE)
        name_in_message = alert_message.find_element(*ProductPageLocators.MESSAGE_TEXT).text

        # Assert
        assert product_name == name_in_message, \
            f"{product_name} -- Product name not name in message -- {name_in_message}"

    def basket_should_contain_price_product(self):
        # Act
        product_form = self.browser.find_element(*ProductPageLocators.PRODUCT_FORM)
        product_price = product_form.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        alert_message = self.browser.find_element(*ProductPageLocators.ALERT_MESSAGE)
        message_product_price = alert_message.find_element(*ProductPageLocators.MESSAGE_PRICE).text

        # Assert
        assert product_price == message_product_price, \
            f"{product_price} -- Basket value no product price -- {message_product_price}"

    def should_not_be_success_message(self):
        # Assert
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_is_disappeared(self):
        # Assert
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, not is disappeared"
