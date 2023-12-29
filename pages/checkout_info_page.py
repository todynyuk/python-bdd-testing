from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.context = context
        self.first_name_id = "first-name"
        self.last_name_id = "last-name"
        self.zipcode_id = "postal-code"
        self.continue_button_id = "continue"

    def check_is_first_name_input_field_present(self, context):
        return context.driver.find_element(By.XPATH,
                                           "//input[@data-test='firstName']").is_enabled()

    def check_is_last_name_input_field_present(self, context):
        return context.driver.find_element(By.XPATH,
                                           "//input[@data-test='lastName']").is_enabled()

    def check_is_zip_code_input_field_present(self, context):
        return context.driver.find_element(By.XPATH,
                                           "//input[@data-test='postalCode']").is_enabled()

    def set_firstname(self, context, first_name):
        context.driver.find_element(By.XPATH, "//input[@data-test='firstName']").send_keys(first_name)

    def set_lastname(self, context, last_name):
        context.driver.find_element(By.XPATH, "//input[@data-test='lastName']").send_keys(last_name)

    def set_zipcode(self, context, zip_code):
        context.driver.find_element(By.XPATH, "//input[@data-test='postalCode']").send_keys(zip_code)

    def click_continue(self, context):
        context.driver.find_element(By.XPATH, "//input[@data-test='continue']").click()
