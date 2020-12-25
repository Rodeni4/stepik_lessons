import pytest

from final.pages.base_page import BasePage
from final.pages.locators import ProductPageLocators


class ProductPage(BasePage):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"

    dictionary = {
        "ru": {
            "expected_alert": "был добавлен в вашу корзину",
        },
        "en-GB": {
            "expected_alert": "has been added to your basket",
        }
    }

    def __init__(self, browser, link_parametrize = None):
        super(ProductPage, self).__init__(browser, self.link)

    def click_button_add_to_basket(self):
        click_button = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        click_button.click()

    def alert_should_added_your_basket(self):
        language_value = self.browser.language_user
        expected_alert = self.dictionary.get(language_value)["expected_alert"]
        actual_alert_text = self.browser.find_element(*ProductPageLocators.ALERT_MESSAGE_TEXT).text
        assert expected_alert in actual_alert_text, \
            f"{expected_alert} -- Alert text is different -- {actual_alert_text}"


