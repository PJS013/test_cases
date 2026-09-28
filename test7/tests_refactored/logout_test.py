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
    miscclass.generated_0(action_keyword_0='[data-test="username"]', action_keyword_1='standard_user', action_keyword_2='secret_sauce', locator_arg_0='[data-test="item-0-title-link"]')
    page.get_by_role('button', name='Open Menu').click()
    expect(page.get_by_text('All ItemsAboutLogoutReset App')).to_be_visible()
    expect(page.locator('[data-test="logout-sidebar-link"]')).to_be_visible()
    page.locator('[data-test="logout-sidebar-link"]').click()
    expect(page.locator('#login_button_container')).to_be_visible()
    page.close()
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)