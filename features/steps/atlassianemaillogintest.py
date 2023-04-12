from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# behave -f allure_behave.formatter:AllureFormatter -o reports2/ ./features
# allure serve reports2/
@given('launch chrome browser for login test')
def lauchBrowser(context):
    context.driver = webdriver.Chrome()


@when('open Atlassian Login Screen for login test')
def openLoginScr(context):
    context.driver.get('https://id.atlassian.com/login')


@when('Enter Email "{email}" validation')
def inputEmail(context, email):
    context.driver.find_element(By.XPATH, "//input[@id='username']").send_keys(email)
    context.driver.find_element(By.XPATH, "(//span[contains(text(),'Continue')])[1]").click()
    time.sleep(1)

@then('verify email valid for login')
def emailValidation(context):
    try:
        a = context.driver.find_element(By.XPATH,"//input[@id='password']").is_displayed()
    except:
        a=False
    if a:
        context.driver.close()
        assert a
    else:
        context.driver.close()
        assert a



