import time
from behave import *
from selenium import webdriver
from pages.login_page import LoginPage
from pages.card_page import CartPage
from pages.checkout_info_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.order_completion import OrderCompletion
from pages.product_page import ProductPage
import queries


@given(u'User launch browser')
def step_impl(context):
    try:
        context.driver = webdriver.Chrome()
    except Exception:
        print(u'STEP: Given launch chrome browser: Could not initiate new Chrome browser instance')


@then(u'User open login page')
def step_impl(context):
    try:
        context.driver.get("https://www.saucedemo.com/")
        context.driver.maximize_window()
    except Exception:
        print(u'STEP: When open login page: Could not navigate to login page')


@when(u'User "{user_login}" enters username and password')
def step_impl(context, user_login):
    login = LoginPage(context)
    time.sleep(3)
    assert login.check_is_username_input_field_present(context), "Username input field is not presented"
    assert login.check_is_password_input_field_present(context), "Password input field is not presented"
    assert login.check_is_login_button_present(context), "Sign in button is not presented"
    login.set_valid_username(context, user_login)
    login.set_valid_password(context, queries.get_password_by_login(user_login))
    login.click_sign_in_button(context)


@then(u'User add product to cart "{order_id}"')
def step_impl(context, order_id):
    product_page = ProductPage(context)
    items_list = queries.get_item_name_by_user_id(order_id)
    for value in items_list:
        product_page.add_product_to_cart(context, value)
    product_page.open_shopping_cart(context)


@then(u'Products list must be more than 1 in cart orders')
def step_impl(context):
    card_page = CartPage(context)
    assert card_page.validate_products_list_in_cart(context), "Items less or equal 1"


@when(u'User click checkout button')
def step_impl(context):
    card_page = CartPage(context)
    card_page.continue_to_checkout(context)


@then(u'User should see the confirm order page')
def step_impl(context):
    checkout = CheckoutPage(context)
    assert checkout.check_is_first_name_input_field_present(context), "Input field First Name is not presented"
    assert checkout.check_is_last_name_input_field_present(context), "Input field Last Name is not presented"
    assert checkout.check_is_zip_code_input_field_present(context), "Input field Postal code is not presented"


@when(u'User "{user_login}" fill all fields and press confirm order')
def step_impl(context, user_login):
    checkout = CheckoutPage(context)
    f_name = queries.get_first_name_by_login(user_login)
    l_name = queries.get_last_name_by_login(user_login)
    zip_code = queries.get_zip_code_by_login(user_login)
    checkout.set_firstname(context, f_name)
    checkout.set_lastname(context, l_name)
    checkout.set_zipcode(context, zip_code)
    checkout.click_continue(context)


@then(u'User should see the all order details')
def step_impl(context):
    checkout_overview = CheckoutOverviewPage(context)
    assert checkout_overview.check_is_all_order_details_present(context), "All order info is not presented"


@when(u'User Press finish button')
def step_impl(context):
    checkout_overview = CheckoutOverviewPage(context)
    checkout_overview.click_finish_button(context)


@then(u'User should see Thank you for your order message')
def step_impl(context):
    order_completion = OrderCompletion(context)
    time.sleep(5)
    assert order_completion.validate_message(context), "Successful order message is not presented"


@then(u'User close browser')
def step_impl(context):
    try:
        context.driver.quit()
    except Exception:
        print(u'STEP: Then close browser: Could not close browser')
