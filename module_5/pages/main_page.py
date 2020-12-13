from .base_page import BasePage


class MainPage(BasePage):
    link = "http://selenium1py.pythonanywhere.com"

    def __init__(self, browser):
        super(MainPage, self).__init__(browser, self.link)



