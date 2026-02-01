from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class GuestDetailsPage(BasePage):

    FIRST_NAME = (By.XPATH, '(//input[@placeholder="Given name"])[1]')
    LAST_NAME = (By.XPATH, '(//input[@placeholder="Family name/Surname"])[1]')
    EMAIL = (By.XPATH, '//input[@placeholder="Email address"]')
    PHONE = (By.XPATH, '//input[@placeholder="Mobile number"]')
    CONTINUE_BUTTON = (By.ID, 'checkout-button')

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_page_load()

    def enter_guest_details(self, first_name, last_name, email, phone):
        self.click(self.LAST_NAME)
        self.send_keys(self.FIRST_NAME, first_name)
        self.send_keys(self.LAST_NAME, last_name)
        self.send_keys(self.EMAIL, email)
        self.send_keys(self.PHONE, phone)
        
    def continue_to_payment(self):
        self.driver.execute_script("window.scrollBy(300, 900);")
        time.sleep(2)
        if self.is_visible(self.CONTINUE_BUTTON):
            self.click(self.CONTINUE_BUTTON)
        else:
            raise Exception("CONTINUE button is not visible on the page")

        

