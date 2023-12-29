from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class ProductPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.context = context
        self.heading_class = "title"
        self.inventory_items_class = "inventory_item"
        self.inventory_item_names_class = "inventory_item_name"
        self.add_to_cart_button_class = "btn_inventory"
        self.shopping_cart_class = "shopping_cart_link"

    def add_product_to_cart(self, context, product_name):
        context.driver.find_element(By.XPATH,
                                    f"//div[contains(text(),'{product_name}')]/../../following-sibling::div/button[contains(@class,'btn_inventory')]").click()

    def open_shopping_cart(self, context):
        context.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        time.sleep(3)
