from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
from .inventory_page import InventoryPage

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_form()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.USERNAME_FIELD), 'Username field is not presented'
        assert self.is_element_present(*LoginPageLocators.PASSWORD_FIELD), 'Password field is not presented'
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), 'Login button is not presented'

    def go_to_inventory_page(self, username, password):
        self.fill_the_login_form(username, password)
        self.should_be_no_error_message()
        return InventoryPage(browser=self.browser, url=self.browser.current_url) 

    def check_login_error(self, username, password, expected_text):
        self.fill_the_login_form(username, password)
        self.should_be_error_message(expected_text)

    def fill_the_login_form(self, username, password):
        self.browser.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys(username)    
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        
    def should_be_no_error_message(self):
        assert not self.is_element_visible(*LoginPageLocators.ERROR_TEXT), \
            "Сообщение об ошибке не ожидалось, но появилось"

    def should_be_error_message(self, expected_text):
        assert self.is_element_visible(*LoginPageLocators.ERROR_TEXT), \
            "Сообщение об ошибке не появилось"
        actual_text = self.get_text(*LoginPageLocators.ERROR_TEXT)
        assert expected_text in actual_text, \
            f"Текст ошибки не совпадает. Ожидалось: '{expected_text}', получено: '{actual_text}'"


        

