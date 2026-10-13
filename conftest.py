import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

URL = 'https://www.saucedemo.com/'

USERS = {
    "standard": ("standard_user", "secret_sauce"),
    "problem":  ("problem_user",  "secret_sauce"),
    "error":    ("error_user",    "secret_sauce"),
    "visual":   ("visual_user",   "secret_sauce"),
}

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru',
                     help="Choose browser language: en, ru, es, etc.")
                     
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    
    if browser_name == "chrome":
        print(f"\nstart chrome browser for test with language: {user_language}..")
        options = ChromeOptions()

        options.add_experimental_option('prefs', {
            'intl.accept_languages': user_language,
            'credentials_enable_service': False,
            'profile.password_manager_enabled': False,
            'profile.password_manager_leak_detection': False,
        })

        options.add_argument("--disable-features=PasswordLeakDetection")

        #options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        
    elif browser_name == "firefox":
        print(f"\nstart firefox browser for test with language: {user_language}..")
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)
        
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(params=USERS.keys())
def logged_in_page(request, browser):
    username, password = USERS[request.param]

    login_page = LoginPage(browser, URL)
    login_page.open()
    login_page.should_be_login_page()
    inventory_page = login_page.go_to_inventory_page(username, password)
    inventory_page.should_be_inventory_page_url()

    yield inventory_page

