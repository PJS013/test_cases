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
    miscclass.generated_2(locator_arg_0='[data-test="add-to-cart-sauce-labs-backpack"]', locator_arg_1='[data-test="add-to-cart-sauce-labs-bike-light"]')
    page.locator('[data-test="shopping-cart-link"]').click()
    expect(page.get_by_text('1Sauce Labs Backpackcarry.')).to_be_visible()
    expect(page.get_by_text('1Sauce Labs Bike LightA red')).to_be_visible()
    page.locator('[data-test="checkout"]').click()
    miscclass.generated_3(locator_arg_0='[data-test="firstName"]', action_arg_0='test', locator_arg_1='[data-test="lastName"]')
    page.locator('[data-test="postalCode"]').fill('123')
    page.locator('[data-test="continue"]').click()
    expect(page.get_by_text('1Sauce Labs Backpackcarry.')).to_be_visible()
    expect(page.get_by_text('1Sauce Labs Bike LightA red')).to_be_visible()
    miscclass.generated_4(locator_arg_0='[data-test="subtotal-label"]', action_arg_0='Item total: $39.98', locator_arg_1='[data-test="finish"]')
    expect(page.locator('[data-test="complete-header"]')).to_contain_text('Thank you for your order!')
    miscclass.generated_4(locator_arg_0='[data-test="complete-text"]', action_arg_0='Your order has been dispatched, and will arrive just as fast as the pony can get there!', locator_arg_1='[data-test="back-to-products"]')
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)