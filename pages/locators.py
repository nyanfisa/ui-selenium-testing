from selenium.webdriver.common.by import By

class LoginPageLocators():
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR_TEXT = (By.XPATH, '//h3[@role="alert"]')

class InventoryPageLocators():
    SORTING_DROPDOWN = (By.TAG_NAME, "select")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")




        