import re
from playwright.sync_api import Playwright, sync_playwright, expect
from page_objects.MiscClass import MiscClass

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    miscclass = MiscClass(page)
    miscclass.generated_1(action_arg_0='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login', locator_arg_0='textbox', locator_keyword_0='Username', action_arg_1='Admin', locator_keyword_1='Password', action_arg_2='admin123', locator_arg_1='button', locator_keyword_2='Login')
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index')
    expect(page.get_by_role('heading')).to_contain_text('Dashboard')
    page.get_by_role('link', name='Recruitment').click()
    expect(page.locator('h6')).to_contain_text('Recruitment')
    page.get_by_role('button').filter(has_text=re.compile('^$')).nth(3).click()
    expect(page.locator('#app')).to_contain_text('Application Stage')
    page.close()
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)