import re
from playwright.sync_api import Playwright, sync_playwright, expect
from page_objects.MiscClass import MiscClass

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    miscclass = MiscClass(page)
    miscclass.generated_1(action_arg_0='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login', locator_arg_0='textbox', locator_keyword_0='Username', action_arg_1='Admin', locator_keyword_1='Password', action_arg_2='admin123', locator_arg_1='button', locator_keyword_2='Login')
    page.get_by_role('link', name='Leave').click()
    expect(page.locator('h5')).to_contain_text('Leave List')
    page.get_by_role('button').filter(has_text=re.compile('^$')).nth(3).click()
    page.get_by_text('View Leave Details').click()
    expect(page.locator('#app')).to_contain_text('Leave Request Details')
    page.get_by_role('button', name='Back').click()
    expect(page.locator('#app')).to_contain_text('Records Found')
    page.close()
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)