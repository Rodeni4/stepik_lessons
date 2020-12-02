import pytest
from selenium import webdriver

from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="my option: 'ru' or 'en-GB' or 'es' or 'fr'")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser = None
    if user_language in ["ru", "en-GB", "es", "fr"]:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    else:
        raise pytest.UsageError("--language should be 'ru' or 'en-GB' or 'es' or 'fr'")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
