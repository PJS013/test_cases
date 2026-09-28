from playwright.sync_api import Playwright, sync_playwright, expect
from page_objects.LoginPage import LoginPage
from page_objects.MiscClass import MiscClass

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.saucedemo.com/')
    loginpage = LoginPage(page)
    miscclass = MiscClass(page, loginpage)
    miscclass.generated_1(action_keyword_0='[data-test="username"]', action_keyword_1='standard_user', action_keyword_2='abc', locator_arg_0='[data-test="error"]', action_arg_0='Epic sadface: Username and password do not match any user in this service')
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)