Feature: Login

  Scenario: Login with correct credentials
    Given launch chrome browser
    When open login page
    Then verify that user can log in
    And close browser

  Scenario: Login with incorrect credentials
    Given launch chrome browser
    When open login page
    Then verify that user cannot log in
    And close browser

