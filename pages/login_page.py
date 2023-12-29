from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class LoginPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.context = context
        self.username_id = "user-name"
        self.password_id = "password"
        self.login_button_id = "login-button"
        self.error_message_class = "error-message-container"

    def check_is_username_input_field_present(self, context):
        return context.driver.find_element(By.ID, self.username_id).is_enabled()

    def check_is_password_input_field_present(self, context):
        return context.driver.find_element(By.ID, self.password_id).is_enabled()

    def check_is_login_button_present(self, context):
        return context.driver.find_element(By.XPATH, "//input[@id='login-button']").is_enabled()

    def set_valid_username(self, context, username):
        context.driver.find_element(By.ID, self.username_id).send_keys(username)

    def set_valid_password(self, context, password):
        context.driver.find_element(By.ID, self.password_id).send_keys(password)

    def click_sign_in_button(self, context):
        context.driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        time.sleep(3)
