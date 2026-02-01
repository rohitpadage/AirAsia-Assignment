from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class HotelDetailsPage(BasePage):

    BOOK_NOW_BUTTON = (By.XPATH, "(//a[normalize-space()='Book now'])[1]")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_page_load()

    def click_book_now(self):
        self.switch_to_new_tab()
        
        max_scrolls = 15

        for _ in range(max_scrolls):
            if self.is_visible(self.BOOK_NOW_BUTTON, timeout=2):
                element = self.driver.find_element(*self.BOOK_NOW_BUTTON)

                # Smooth visible scroll
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                    element
                )
                time.sleep(2)
                element.click()
                time.sleep(2)
                return

            # Scroll down gradually
            self.driver.execute_script("window.scrollBy(0, 400);")
            time.sleep(2)

        raise Exception("Book Now button not found after scrolling")