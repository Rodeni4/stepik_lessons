import pytest
from selenium import webdriver

from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="my option: 'ru' or 'en-GB' or 'es' or 'fr' or 'en'")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")

    if user_language not in ["ru", "en-GB", "es", "fr", "en"]:
        raise pytest.UsageError("--language should be 'ru' or 'en-GB' or 'es' or 'fr' or 'en'")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    browser_chrome = webdriver.Chrome(options=options)
    browser_chrome.maximize_window()
    browser_chrome.implicitly_wait(5)
    browser_chrome.language_user = user_language

    yield browser_chrome
    browser_chrome.quit()
