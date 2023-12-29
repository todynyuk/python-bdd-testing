Feature: SauceDemo web Page Practice
  It is created a log in add product to cart make checkout and verify it.

  @demo
  Scenario Outline: SauceDemo open page - Log in - add product to cart - check product is added - finish order and verify it.
    Given User launch browser
    Then User open login page
    When User "<user_login>" enters username and password
    Then User add product to cart "<order_id>"
    Then Products list must be more than 1 in cart orders
    When User click checkout button
    Then User should see the confirm order page
    When User "<user_login>" fill all fields and press confirm order
    Then User should see the all order details
    When User Press finish button
    Then User should see Thank you for your order message
    And  User close browser

    Examples:
      | user_login    | order_id |
      | standard_user | 1        |
      | visual_user   | 2        |