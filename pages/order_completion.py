from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderCompletion(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.context = context
        self.order_completion_message_class = "complete-header"

    def validate_message(self, context):
        return context.driver.find_element(By.XPATH, "//div[@class='checkout_complete_container']").is_enabled()
