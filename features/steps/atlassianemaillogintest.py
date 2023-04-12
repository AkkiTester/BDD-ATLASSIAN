from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('launch chrome browser for login test')
def lauchBrowser(context):
    context.driver=webdriver.Chrome()


@when('open Atlassian Login Screen for login test')
def openLoginScr(context):
    context.driver.get('https://id.atlassian.com/login')


@when('Enter Email "{email}" validation')
def inputEmail(context,email):
    context.driver.find_element(By.XPATH,"//input[@id='username']").send_keys(email)
    context.driver.find_element(By.ID,"//span[contains(text(),'Continue')]").click()

@then('verify email valid for login')
def emailValidation(context):
    try:
        context.driver.find_element(By.ID, "//span[contains(text(),'Continue')]").is_displayed()
        assert True
    except:
        context.driver.close()
        assert False




