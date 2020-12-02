# Data
link_page = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

button_add_to_basket_locator = ".btn-add-to-basket"
language_locator = ".no-js"
language_value_locator = "lang"

dictionary = {"ru": "Добавить в корзину", "en-GB": "Add to basket", "es": "Añadir al carrito", "fr": "Ajouter au panier"}


def test_add_to_basket_button(browser):
    # Arrange
    browser.get(link_page)

    language = browser.find_element_by_css_selector(language_locator)
    language_value = language.get_attribute(language_value_locator)

    # Act
    button_add_to_basket = browser.find_element_by_css_selector(button_add_to_basket_locator)
    successful_button_text = button_add_to_basket.text

    # Assert
    if language_value in dictionary.keys():
        assert dictionary.get(language_value) in successful_button_text, "button text is different"
    else:
        assert language_value is None, "Invalid language selected"
