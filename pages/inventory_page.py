from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import TimeoutException
#from .locators import InventoryPageLocators

class InventoryPage(BasePage):
    def should_be_inventory_page_url(self):
       self.should_be_on_page("/inventory.html")

    def add_to_cart(self, product_name):
        btn = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.ID, f"add-to-cart-{product_name}"))
        )
        btn.click()
        self. should_be_remove_button(product_name)

    def should_be_remove_button(self, product_name):
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((By.ID, f"remove-{product_name}"))
        )    