from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class CheckoutOverviewPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)
        self.context = context
        self.finish_cta_name = "finish"

    def check_is_all_order_details_present(self, context):
        return context.driver.find_element(By.XPATH,
                                           "//div[@class='summary_info']").is_enabled()

    def click_finish_button(self, context):
        time.sleep(3)
        context.driver.find_element(By.XPATH, "//button[@data-test='finish']").click()
