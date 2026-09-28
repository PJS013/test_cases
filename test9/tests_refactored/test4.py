import re
from playwright.sync_api import Playwright, sync_playwright, expect
from page_objects.MiscClass import MiscClass

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    miscclass = MiscClass(page)
    miscclass.generated_0(action_arg_0='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login', locator_arg_0='heading', action_arg_1='Login', locator_arg_1='textbox', locator_keyword_0='Username', action_arg_2='Admin', locator_keyword_1='Password', action_arg_3='admin123', locator_arg_2='button', action_arg_4='Dashboard')
    page.get_by_role('link', name='Buzz').click()
    expect(page.locator('#app')).to_contain_text('Buzz Newsfeed')
    page.locator('#heart').first.click()
    page.close()
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)