Feature: Checkout

  Scenario Outline: Login with correct credentials
    Given I launch chrome browser
    When I open login page
    Then I verify that user can log in with "<username>" and "<password>"
    When I add an "<item>" to the cart
    Then I should see the "<item>" in the cart
    When I click checkout button
    Then I should see the confirm order page
    When Fill "<f_name>" and "<l_name>" and "<zip_code>" fields and press confirm order
    Then I should see the all order details
    When Press finish button
    Then I should see Thank you for your order message
    And  I close browser

    Examples:
      | item                     | username      | password     | f_name | l_name | zip_code |
      | Sauce Labs Bike Light    | standard_user | secret_sauce | John   | Smith  | 151000   |
      | Sauce Labs Fleece Jacket | visual_user   | secret_sauce | Joshua | Mayer  | 155500   |