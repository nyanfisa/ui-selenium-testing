from .base_page import BasePage
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
#from selenium.common.exceptions import TimeoutException
from .locators import InventoryPageLocators

class InventoryPage(BasePage):
    def should_be_inventory_page_url(self):
       self.should_be_on_page("/inventory.html")

    def choose_sorting_type(self, value):
        dropdown = self.is_element_clickable(*InventoryPageLocators.SORTING_DROPDOWN)
        Select(dropdown).select_by_value(value)
    
    def get_product_names(self) -> list[str]:
        elements = self.browser.find_elements(*InventoryPageLocators.PRODUCT_NAMES)
        return [el.text for el in elements]

    def get_product_prices(self) -> list[float]:
        elements = self.browser.find_elements(*InventoryPageLocators.PRODUCT_PRICES)
        return [float(el.text.replace("$", "")) for el in elements]    


    


