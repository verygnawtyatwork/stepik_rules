import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Передаем язык, указанный в коммандной строке. Если не указали язык, то по умолчанию будет english
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en", help="type language")
    # Необязательная часть: можно запустить с указанным браузером chrome или firefox в коммандной строке, по умолчанию будет chrome
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")

# Запускаем браузер с указанным язком
@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language") 
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
