from selenium.webdriver.common.by import By

class LoginPageLocators():
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR_TEXT = (By.XPATH, '//h3[@role="alert"]')

class InventoryPageLocators():
    #items
    BACKPACK_ADD_TO_CART = (By.ID, 'add-to-cart-sauce-labs-backpack')
    BACKPACK_REMOVE_FROM_CART = (By.ID, 'remove-sauce-labs-backpack')
    BACKPACK_PAGE_LINK = (By.ID, 'item_4_title_link')

    BIKE_LIGHT_ADD_TO_CART = (By.ID, 'add-to-cart-sauce-labs-bike-light')
    BIKE_LIGHT_REMOVE_FROM_CART = (By.ID, 'remove-sauce-labs-bike-light')
    BIKE_LIGHT_PAGE_LINK = (By.ID, 'item_0_title_link')

    TSHIRT_ADD_TO_CART = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    TSHIRT_REMOVE_FROM_CART = (By.ID, 'remove-sauce-labs-bolt-t-shirt')
    TSHIRT_PAGE_LINK = (By.ID, 'item_1_title_link')

    JACKET_ADD_TO_CART = (By.ID, 'add-to-cart-sauce-labs-fleece-jacket')
    JACKET_REMOVE_FROM_CART = (By.ID, 'remove-sauce-labs-fleece-jacket')
    JACKET_PAGE_LINK = (By.ID, 'item_5_title_link')

    ONESIE_ADD_TO_CART = (By.ID, 'add-to-cart-sauce-labs-onesie')
    ONESIE_REMOVE_FROM_CART = (By.ID, 'remove-sauce-labs-onesie')
    ONESIE_PAGE_LINK = (By.ID, 'item_2_title_link')

    RED_TSHIRT_ADD_TO_CART = (By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)')
    RED_TSHIRT_REMOVE_FROM_CART = (By.ID, 'remove-test.allthethings()-t-shirt-(red)')
    RED_TSHIRT_PAGE_LINK = (By.ID, 'item_3_title_link')

        