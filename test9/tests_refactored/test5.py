import re
from playwright.sync_api import Playwright, sync_playwright, expect
from page_objects.MiscClass import MiscClass

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    miscclass = MiscClass(page)
    miscclass.generated_0(action_arg_0='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login', locator_arg_0='alert', action_arg_1='Login', locator_arg_1='textbox', locator_keyword_0='Username', action_arg_2='Admin', locator_keyword_1='Password', action_arg_3='WrongPassword', locator_arg_2='button', action_arg_4='Invalid credentials')
    page.close()
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)