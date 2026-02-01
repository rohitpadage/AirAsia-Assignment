from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class HotelResultsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_page_load()

    def select_hotel_by_name(self, hotel):
        time.sleep(5)
        hotel_locator=(By.XPATH,f"//div[normalize-space()='{hotel}']")
        max_scrolls = 20

        for _ in range(max_scrolls):
            if self.is_visible(hotel_locator, timeout=2):
                element = self.driver.find_element(*hotel_locator)

                # Smooth scroll to element (VISIBLE TRANSITION)
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                    element
                )
                time.sleep(2)
                element.click()
                time.sleep(5)
                return

        # Scroll down gradually (visible movement)
        self.driver.execute_script("window.scrollBy(0, 400);")
        time.sleep(1)

        raise Exception(f"Hotel '{hotel_locator}' not found after scrolling")    



