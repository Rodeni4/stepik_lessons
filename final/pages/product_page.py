from final.pages.base_page import BasePage
from final.pages.locators import ProductPageLocators


class ProductPage(BasePage):
    # Data
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"

    def __init__(self, browser):
        super(ProductPage, self).__init__(browser, self.link)

    def click_button_add_to_basket(self):
        click_button = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        click_button.click()


