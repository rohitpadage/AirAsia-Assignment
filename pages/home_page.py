from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class HomePage(BasePage):
    HOTELS_TAB = (By.XPATH, "//p[contains(text(),'Hotels')]/parent::div")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_page_load()
        
    def open_site(self):
        self.driver.get("https://www.airasia.com")

    def go_to_hotels(self):
        self.click(self.HOTELS_TAB)
        time.sleep(5)
        
