import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

url = 'https://www.saucedemo.com/'

@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"), 
    ("problem_user", "secret_sauce"),
    #("performance_glitch_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    ("visual_user", "secret_sauce")
])

def test_successful_login(browser, username, password):
    login_page = LoginPage(browser, url)
    login_page.open()
    login_page.should_be_login_page()

    inventory_page = login_page.go_to_inventory_page(username, password)
    inventory_page.should_be_inventory_page_url()


@pytest.mark.parametrize("username, password, expected_error_text", [
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
    ("", "", "Epic sadface: Username is required"), 
    ("", "secret_sauce", "Epic sadface: Username is required"),
    ("standard_user", "", "Epic sadface: Password is required"),
    ("pretty_user", "123", "Epic sadface: Username and password do not match any user in this service")
])

def test_login_with_error(browser, username, password, expected_error_text):
    login_page = LoginPage(browser, url)
    login_page.open()
    login_page.should_be_login_page()
    login_page.check_login_error(username, password, expected_error_text)