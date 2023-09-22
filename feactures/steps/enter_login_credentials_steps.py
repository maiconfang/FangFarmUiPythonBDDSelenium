import time

from behave import *

from Utilities import configReader
from feactures.pageobjects.LoginCredentialsPage import LoginCredentialsPage


@given(u'I navigate to home page')
def step_impl(context):
    context.reg = LoginCredentialsPage(context.driver)
    context.reg.open(configReader.readConfig("basic info", "url_local_home"))
    context.driver.implicitly_wait(5)
    # Maximize the Chrome window
    context.driver.maximize_window()


@given(u'I navigate to login home')
def step_impl(context):
    context.reg.clickLoginHome()


@when(u'I enter the login as "{login}"')
def step_impl(context, login):
    context.reg.setLogin(login)


@then(u'I enter the password as "{password}"')
def step_impl(context, password):
    print("Stop here")
    context.reg.setPassword(password)


@then(u'I click on the enter button')
def step_impl(context):
    context.reg.clickBtnEnter()


@then(u'The login of user should be displayed "{userLogged}"')
def step_impl(context, userLogged):
    systemUserLogged = context.reg.getValueUserLogged()
    assert userLogged in systemUserLogged
