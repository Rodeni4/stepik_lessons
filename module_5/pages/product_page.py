from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

        self.solve_quiz_and_get_code()

        self.should_be_name_product()
        self.should_be_price()

    def should_be_name_product(self):
        product_form = self.browser.find_element(*ProductPageLocators.PRODUCT_FORM)
        product_name = product_form.find_element(*ProductPageLocators.PRODUCT_NAME).text

        alert_message = self.browser.find_element(*ProductPageLocators.ALERT_MESSAGE)
        name_in_message = alert_message.find_element(*ProductPageLocators.MESSAGE_TEXT).text

        assert product_name in name_in_message, \
            f"{product_name} -- Product name not name in message -- {name_in_message}"

    def should_be_price(self):

        product_form = self.browser.find_element(*ProductPageLocators.PRODUCT_FORM)
        product_price = product_form.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        alert_message = self.browser.find_element(*ProductPageLocators.ALERT_MESSAGE)
        message_product_price = alert_message.find_element(*ProductPageLocators.MESSAGE_PRICE).text

        assert product_price in message_product_price, \
            f"{product_price} -- Basket value no product price -- {message_product_price}"
