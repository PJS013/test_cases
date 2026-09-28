import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://automationexercise.com/")
    page.get_by_role("button", name="Zgadzam się").click()
    expect(page.get_by_role("link", name="Website for automation")).to_be_visible()
    expect(page.locator("#header")).to_contain_text("Signup / Login")
    page.get_by_role("listitem").filter(has_text="Signup / Login").click()
    expect(page.locator("#form")).to_contain_text("Login to your account")
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").click()
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").fill("test@test.nottest")
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").press("Tab")
    page.get_by_role("textbox", name="Password").fill("IncorrectPassword")
    page.get_by_role("button", name="Login").click()
    expect(page.locator("#form")).to_contain_text("Your email or password is incorrect!")
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
