import pytest
from selenium import webdriver

from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="my option: ru or en")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser = None
    if user_language == "ru":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': "ru"})
    elif user_language == "en-GB":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': "en-GB"})
    elif user_language == "es":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': "es"})
    elif user_language == "fr":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': "fr"})
    else:
        raise pytest.UsageError("--user_language should be 'ru' or 'en-GB' or 'es' or 'fr'")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
