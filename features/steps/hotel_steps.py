from behave import given, when, then
from pages.home_page import HomePage
from pages.hotel_search_page import HotelSearchPage
from pages.hotel_results_page import HotelResultsPage
from pages.hotel_details_page import HotelDetailsPage
from pages.guest_details_page import GuestDetailsPage
from pages.payment_page import PaymentPage
from config.test_data import *

@given("user launches AirAsia website")
def step_launch_site(context):
    context.home = HomePage(context.driver)
    context.home.open_site()

@when("user navigates to Hotels section")
def step_go_to_hotels(context):
    context.home.go_to_hotels()
    
@when('user searches hotel in "{CITY}"')
def step_search_hotel(context, CITY):
    context.search = HotelSearchPage(context.driver)
    context.search.search_hotel(
        CITY,
        CHECKIN_DAY,
        CHECKOUT_DAY,
        ROOMS,
        ADULTS,
        CHILDREN
    )

@when('user selects hotel "{HOTEL}"')
def step_select_hotel(context,HOTEL):
    context.hotel_result=HotelResultsPage(context.driver)
    context.hotel_result.select_hotel_by_name(HOTEL)

@when('user clicks Book Now on hotel details page')
def step_click_book_now(context):
    context.hotel_details = HotelDetailsPage(context.driver)
    context.hotel_details.click_book_now()

@when("user enters guest details")
def step_enter_guest_details(context):
    context.booking = GuestDetailsPage(context.driver)
    context.booking.enter_guest_details(FIRSTNAME,LASTNAME,EMAILADDRESS,MOBILENUMBER)
    context.booking.continue_to_payment()

@then("user should reach payment page")
def step_verify_payment_page(context):
    context.payment=PaymentPage(context.driver)
    assert context.payment.is_payment_page_displayed(), \
        "Secure checkout text is not displayed"