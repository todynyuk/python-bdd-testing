from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class CartPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.context = context
        self.inventory_name = "inventory_item_name"
        self.checkout_class = "checkout_button"

    def validate_product_in_cart(self, context, product_name):
        item_description_text = context.driver.find_element(By.XPATH, "//div[@class='inventory_item_name']").text
        return product_name == item_description_text

    def continue_to_checkout(self, context):
        context.driver.find_element(By.XPATH, "//button[@data-test='checkout']").click()
        time.sleep(3)
