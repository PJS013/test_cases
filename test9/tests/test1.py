import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page.get_by_role("heading")).to_contain_text("Login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("heading")).to_contain_text("Dashboard")
    expect(page.get_by_text("Time at WorkPunched")).to_be_visible()
    page.get_by_role("listitem").filter(has_text="Demo Source").locator("i").click()
    page.get_by_role("menuitem", name="Logout").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
