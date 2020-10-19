Feature: OrangeHRM Login

  Background:
    Given I launch the browser
    When I open the application
    And Enter valid username and password
    And Click login

  Scenario: Login to HRM application
    Then User must login to dashboard

  Scenario: Search User
    When navigate to search page
    Then Search page should display

  Scenario: Advance search user
    When navigate to advanced search page
    Then advance search page should display