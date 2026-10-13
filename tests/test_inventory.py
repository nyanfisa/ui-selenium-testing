import pytest
from selenium.webdriver.common.by import By

def test_add_products_to_cart(logged_in_page):
    products = [
        "sauce-labs-backpack",
        "sauce-labs-bike-light",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-fleece-jacket",
    ]
    for product in products:
        logged_in_page.add_to_cart(product)

    #assert logged_in_page.get_cart_badge() == "4"

# BACKPACK_ADD_TO_CART = (By.ID, 'add-to-cart-sauce-labs-backpack')
#     BACKPACK_REMOVE_FROM_CART = (By.ID, 'remove-sauce-labs-backpack')
#     BACKPACK_PAGE_LINK = (By.ID, 'item_4_title_link')

#     BIKE_LIGHT_ADD_TO_CART = (By.ID, 'add-to-cart-sauce-labs-bike-light')
#     BIKE_LIGHT_REMOVE_FROM_CART = (By.ID, 'remove-sauce-labs-bike-light')
#     BIKE_LIGHT_PAGE_LINK = (By.ID, 'item_0_title_link')

#     TSHIRT_ADD_TO_CART = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
#     TSHIRT_REMOVE_FROM_CART = (By.ID, 'remove-sauce-labs-bolt-t-shirt')
#     TSHIRT_PAGE_LINK = (By.ID, 'item_1_title_link')

#     JACKET_ADD_TO_CART = (By.ID, 'add-to-cart-sauce-labs-fleece-jacket')
#     JACKET_REMOVE_FROM_CART = (By.ID, 'remove-sauce-labs-fleece-jacket')
#     JACKET_PAGE_LINK = (By.ID, 'item_5_title_link')

#     ONESIE_ADD_TO_CART = (By.ID, 'add-to-cart-sauce-labs-onesie')
#     ONESIE_REMOVE_FROM_CART = (By.ID, 'remove-sauce-labs-onesie')
#     ONESIE_PAGE_LINK = (By.ID, 'item_2_title_link')

#     RED_TSHIRT_ADD_TO_CART = (By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)')
#     RED_TSHIRT_REMOVE_FROM_CART = (By.ID, 'remove-test.allthethings()-t-shirt-(red)')
#     RED_TSHIRT_PAGE_LINK = (By.ID, 'item_3_title_link')


# PRODUCTS = {
#     "backpack": {
#         "name": "Sauce Labs Backpack",
#         "id": "sauce-labs-backpack",
#     },
#     "bolt_tshirt": {
#         "name": "Sauce Labs Bolt T-Shirt",
#         "id": "sauce-labs-bolt-t-shirt",
#     },
#     "fleece_jacket": {
#         "name": "Sauce Labs Fleece Jacket",
#         "id": "sauce-labs-fleece-jacket",
#     }, 
#     "test_allthethings_tshirt": {
#         "name": "Test.allTheThings() T-Shirt (Red)",
#         "id": "test.allthethings()-t-shirt-(red)",
#     },   
# }