
Feature: AirAsia Hotel Booking

    Scenario: Book hotel till payment page
        Given user launches AirAsia website
        When user navigates to Hotels section
        And user searches hotel in "Bengaluru"
        And user selects hotel "Hyatt Centric MG Road Bangalore"
        And user clicks Book Now on hotel details page
        And user enters guest details
        Then user should reach payment page 
    