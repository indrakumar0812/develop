Feature: OrangeHRM Login

  Scenario: Login to HRM using valid parameters
    Given I launch the chrome browser
    When I open the HRM home page
    And Enter username "admin" and password "admin123"
    And click on the login button
    Then User must successfully login to the dashboard

  Scenario Outline: Login to HRM using multiple parameters
    Given I launch the chrome browser
    When I open the HRM home page
    And Enter username "<username>" and password "<password>"
    And click on the login button
    Then User must successfully login to the dashboard

    Examples:
      | username   | password |
      | admin      | admin123 |
      | admin123   | admin    |
      | adminxyz   | admin123 |
      | admin      | adminxyz |
