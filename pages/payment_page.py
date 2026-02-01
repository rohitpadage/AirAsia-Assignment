from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PaymentPage(BasePage):

    SECURE_CHECKOUT_TEXT = (By.XPATH,"//*[normalize-space()='Secure Checkout']")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_page_load()

    def is_payment_page_displayed(self):
        return self.is_visible(self.SECURE_CHECKOUT_TEXT, timeout=30)
