import pytest
from selenium import webdriver
from datetime import datetime

from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en-GB",
                     help="my option: 'ru' or 'en-GB' or 'es' or 'fr'")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")

    if user_language not in ["ru", "en-GB", "es", "fr"]:
        raise pytest.UsageError("--language should be 'ru' or 'en-GB' or 'es' or 'fr'")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    browser_chrome = webdriver.Chrome(options=options)
    browser_chrome.maximize_window()
    browser_chrome.implicitly_wait(5)
    browser_chrome.language_user = user_language

    yield browser_chrome
    # получаем переменную с текущей датой и временем в формате ГГГГ-ММ-ДД_ЧЧ-ММ-СС
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # делаем скриншот с помощью команды Selenium'а и сохраняем его с именем "screenshot-ГГГГ-ММ-ДД_ЧЧ-ММ-СС"
    browser_chrome.save_screenshot('Screenshots/screenshot-%s.png' % now)
    browser_chrome.quit()

