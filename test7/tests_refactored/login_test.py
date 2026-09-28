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
    miscclass.generated_0(action_keyword_0='[data-test="username"]', action_keyword_1='standard_user', action_keyword_2='secret_sauce', locator_arg_0='[data-test="item-4-title-link"]')
    expect(page.locator('[data-test="item-0-title-link"] [data-test="inventory-item-name"]')).to_contain_text('Sauce Labs Bike Light')
    context.close()
    browser.close()