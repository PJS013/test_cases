import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    expect(page.get_by_role("heading")).to_contain_text("Dashboard")
    page.get_by_role("link", name="Recruitment").click()
    expect(page.locator("h6")).to_contain_text("Recruitment")
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(3).click()
    expect(page.locator("#app")).to_contain_text("Application Stage")
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
