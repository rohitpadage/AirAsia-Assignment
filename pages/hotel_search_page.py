from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class HotelSearchPage(BasePage):

    # ================= LOCATORS =================

    CITY_INPUT = (By.XPATH, "//input[@label='Destination']")
    CONFIRM_BUTTON = (By.XPATH, "//a[contains(text(),'Confirm')]")
    SEARCH_BUTTON = (By.XPATH, "//a[contains(text(),'Search')]")

    GUESTS_ROOMS_BUTTON = (By.XPATH, "//p[contains(text(),'Guests  & Rooms')]")
    DONE_BUTTON = (By.XPATH, "//a[contains(text(),'Done')]//parent::div")

    ADD_ROOMS = (By.XPATH, "//div[@data-test='add-room-button']")

    ADULTS_VALUE = (By.XPATH, "//div[@id='home_adult_remove']//following-sibling::h3")
    ADULTS_PLUS = (By.XPATH, "//div[@id='home_adult_add']")
    ADULTS_MINUS = (By.XPATH, "//div[@id='home_adult_remove']")

    CHILDREN_VALUE = (By.XPATH, "//div[@id='home_child_remove']//following-sibling::h3")
    CHILDREN_PLUS = (By.XPATH, "//div[@id='home_child_add']")
    CHILDREN_MINUS = (By.XPATH, "//div[@id='home_child_remove']")

    # ================= MAIN FLOW =================

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_for_page_load()

    def search_hotel(self, city, checkin, checkout, rooms, adults, children):
        self.enter_destination(city)
        self.select_stay_dates(checkin, checkout)
        self.select_guests_and_rooms(rooms, adults, children)
        self.click_search()
        time.sleep(10)

    # ================= PAGE ACTIONS =================

    def enter_destination(self, city):
        if self.is_visible(self.CITY_INPUT):
            self.send_keys(self.CITY_INPUT, city)
            city_option = (By.XPATH, f"(//span[contains(normalize-space(),'{city}')])[1]")
            if self.is_visible(city_option):
                self.click(city_option)
            else:
                raise Exception(f"City dropdown option '{city}' not visible")
        else:
            raise Exception("Destination input is not visible on the page")

    def select_stay_dates(self, checkin, checkout):
        self.select_date(checkin)
        time.sleep(2)
        self.select_date(checkout)

        if self.is_visible(self.CONFIRM_BUTTON):
            self.click(self.CONFIRM_BUTTON)
        else:
            raise Exception("CONFIRM button is not visible on the page")

    def select_guests_and_rooms(self, rooms, adults, children):

        if self.is_visible(self.GUESTS_ROOMS_BUTTON):
            self.click(self.GUESTS_ROOMS_BUTTON)
        else:
            raise Exception("Guests & Rooms button is not displayed")

        ADULTS_DEFAULTVALUE = self.get_text(self.ADULTS_VALUE)
        CHILDREN_DEFAULTVALUE = self.get_text(self.CHILDREN_VALUE)

        def adjust_value(value, plus_locator, minus_locator, desired_value):
            current_value = int(value)
            diff = desired_value - current_value

            if diff > 0:
                for _ in range(diff):
                    self.click(plus_locator)
                    time.sleep(1)
            elif diff < 0:
                for _ in range(abs(diff)):
                    self.click(minus_locator)
                    time.sleep(1)

        adjust_value(ADULTS_DEFAULTVALUE, self.ADULTS_PLUS, self.ADULTS_MINUS, adults)
        time.sleep(5)
        adjust_value(CHILDREN_DEFAULTVALUE, self.CHILDREN_PLUS, self.CHILDREN_MINUS, children)

        self.click(self.DONE_BUTTON)

    def click_search(self):
        if self.is_visible(self.SEARCH_BUTTON):
            self.click(self.SEARCH_BUTTON)
        else:
            raise Exception("Search button is not visible on the page")

    # ================= HELPERS =================

    def select_date(self, day):
        date_locator = (
            By.XPATH,
            f"//div[contains(@class,'calendarInstance__DayStyling') and normalize-space()='{day}']"
        )
        if self.is_visible(date_locator):
            self.click(date_locator)
        else:
            raise Exception("Day is not displaying in Calendar")
