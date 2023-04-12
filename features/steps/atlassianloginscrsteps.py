from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('launch chrome browser')
def launchBrowser(context):
    context.driver=webdriver.Chrome()

@when('open Atlassian Login Screen')
def openLoginScr(context):
    context.driver.get('https://id.atlassian.com/login')

@then('verify that the logo present on page')
def verifyLogo(context):
    status= context.driver.find_element(By.XPATH,"//span[@class='css-a3l9jr']//*[name()='svg']")

@then('close browser')
def closeBrowser(context):
    context.driver.close()
