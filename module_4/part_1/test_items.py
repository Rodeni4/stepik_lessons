# Data
link_page = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

button_add_to_basket_locator = ".btn-add-to-basket"

dictionary = {
    "ru": "Добавить в корзину",
    "en-GB": "Add to basket",
    "es": "Añadir al carrito",
    "fr": "Ajouter au panier"
}


def test_add_to_basket_button(browser):
    # Data
    language_value = browser.language_user

    # Arrange
    browser.get(link_page)

    # Act
    button_add_to_basket = browser.find_element_by_css_selector(button_add_to_basket_locator)
    successful_button_text = button_add_to_basket.text

    # Assert
    assert dictionary.get(language_value) in successful_button_text, "button text is different"

