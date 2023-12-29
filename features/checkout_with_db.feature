Feature: SauceDemo web Page Practice
  It is created a log in add product to cart make checkout and verify it.

  @demo
  Scenario: SauceDemo open page - Log in - add product to cart - check product is added - finish order and verify it.
    Given User launch browser
    Then User open login page
    When User enters username and password
    Then User add product to cart
    Then Product title must be present in cart orders
    When User click checkout button
    Then User should see the confirm order page
    When User fill all fields and press confirm order
    Then User should see the all order details
    When User Press finish button
    Then User should see Thank you for your order message
    And  User close browser