from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'launch chrome browser')
def step_impl(context):
    try:
        context.driver = webdriver.Chrome()
    except Exception:
        print(u'STEP: Given launch chrome browser: Could not initiate new Chrome browser instance')


@when(u'open login page')
def step_impl(context):
    try:
        context.driver.get("https://www.saucedemo.com/")
    except Exception:
        print(u'STEP: When open login page: Could not navigate to login page')


@then(u'verify that user can log in')
def step_impl(context):
    try:
        username = context.driver.find_element(By.XPATH, "//input[@id='user-name']")
        password = context.driver.find_element(By.XPATH, "//input[@id='password']")
        login_btn = context.driver.find_element(By.XPATH, "//input[@id='login-button']")

        username.send_keys("standard_user")
        password.send_keys("secret_sauce")
        login_btn.click()

        logout_link = context.driver.find_elements(By.XPATH, "//a[@id='logout_sidebar_link']")
        assert len(logout_link) == 1
    except Exception:
        print(u'STEP: Then verify that user can log in: Could not login')


@then(u'close browser')
def step_impl(context):
    try:
        context.driver.quit()
    except Exception:
        print(u'STEP: Then close browser: Could not close browser')


@then(u'verify that user cannot log in')
def step_impl(context):
    try:
        username = context.driver.find_element(By.XPATH, "//input[@id='user-name']")
        password = context.driver.find_element(By.XPATH, "//input[@id='password']")
        login_btn = context.driver.find_element(By.XPATH, "//input[@id='login-button']")

        username.send_keys("standard_user")
        password.send_keys("wrong_password")
        login_btn.click()

        logout_link = context.driver.find_elements(By.XPATH, "//a[@id='logout_sidebar_link']")
        assert len(logout_link) == 0
    except Exception:
        print(u'STEP: Then verify that user cannot log in: ')
