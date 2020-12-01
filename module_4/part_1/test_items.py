# Data
link_page = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

button_add_to_basket_locator = ".btn-add-to-basket"
language_locator = "[selected='selected']"

button_text_ru = "Добавить в корзину"
button_text_en_GB = "Add to basket"
button_text_es = "Añadir al carrito"
button_text_fr = "Ajouter au panier"


def test_add_to_basket_button(browser):

    # Arrange
    browser.get(link_page)

    # Act
    button_add_to_basket = browser.find_element_by_css_selector(button_add_to_basket_locator)
    successful_button_text = button_add_to_basket.text

    language = browser.find_element_by_css_selector(language_locator)
    language_text = language.text

    # Assert
    if "Русский" in language_text:
        assert button_text_ru in successful_button_text, "button text is different"
    elif "British English" in language_text:
        assert button_text_en_GB in successful_button_text, "button text is different"
    elif "español" in language_text:
        assert button_text_es in successful_button_text, "button text is different"
    elif "français" in language_text:
        assert button_text_fr in successful_button_text, "button text is different"
    else:
        assert language_text is None, "Invalid language selected"