import time
from pages.login_page import LoginPage
from pages.card_page import CartPage
from pages.checkout_info_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.order_completion import OrderCompletion
from pages.product_page import ProductPage
from behave import *
from selenium import webdriver


@given(u'I launch chrome browser')
def step_impl(context):
    try:
        context.driver = webdriver.Chrome()
    except Exception:
        print(u'STEP: Given launch chrome browser: Could not initiate new Chrome browser instance')


@when(u'I open login page')
def step_impl(context):
    try:
        context.driver.get("https://www.saucedemo.com/")
        context.driver.maximize_window()
    except Exception:
        print(u'STEP: When open login page: Could not navigate to login page')


@then(u'I verify that user can log in with "{username}" and "{password}"')
def step_impl(context, username, password):
    login = LoginPage(context)
    time.sleep(3)
    assert login.check_is_username_input_field_present(context), "Username input field is not presented"
    assert login.check_is_password_input_field_present(context), "Password input field is not presented"
    assert login.check_is_login_button_present(context), "Sign in button is not presented"
    login.set_valid_username(context, username)
    login.set_valid_password(context, password)
    login.click_sign_in_button(context)


@when(u'I add an "{item}" to the cart')
def step_impl(context, item):
    product_page = ProductPage(context)
    product_page.add_product_to_cart(context, item)
    product_page.open_shopping_cart(context)


@then(u'I should see the "{item}" in the cart')
def step_impl(context, item):
    card_page = CartPage(context)
    assert card_page.validate_product_in_cart(context, item), "Item names are not equals"


@when(u'I click checkout button')
def step_impl(context):
    card_page = CartPage(context)
    card_page.continue_to_checkout(context)


@then(u'I should see the confirm order page')
def step_impl(context):
    checkout = CheckoutPage(context)
    assert checkout.check_is_first_name_input_field_present(context), "Input field First Name is not presented"
    assert checkout.check_is_last_name_input_field_present(context), "Input field Last Name is not presented"
    assert checkout.check_is_zip_code_input_field_present(context), "Input field Postal code is not presented"


@when(u'Fill "{f_name}" and "{l_name}" and "{zip_code}" fields and press confirm order')
def step_impl(context, f_name, l_name, zip_code):
    checkout = CheckoutPage(context)
    checkout.set_firstname(context, f_name)
    checkout.set_lastname(context, l_name)
    checkout.set_zipcode(context, zip_code)
    checkout.click_continue(context)


@then(u'I should see the all order details')
def step_impl(context):
    checkout_overview = CheckoutOverviewPage(context)
    assert checkout_overview.check_is_all_order_details_present(context), "All order info is not presented"


@when(u'Press finish button')
def step_impl(context):
    checkout_overview = CheckoutOverviewPage(context)
    checkout_overview.click_finish_button(context)


@then(u'I should see Thank you for your order message')
def step_impl(context):
    order_completion = OrderCompletion(context)
    time.sleep(5)
    assert order_completion.validate_message(context), "Successful order message is not presented"


@then(u'I close browser')
def step_impl(context):
    try:
        context.driver.quit()
    except Exception:
        print(u'STEP: Then close browser: Could not close browser')
