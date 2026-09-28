from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"password\"]").press("Enter")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"item-0-title-link\"]")).to_be_visible()
    page.get_by_role("button", name="Open Menu").click()
    expect(page.get_by_text("All ItemsAboutLogoutReset App")).to_be_visible()
    expect(page.locator("[data-test=\"logout-sidebar-link\"]")).to_be_visible()
    page.locator("[data-test=\"logout-sidebar-link\"]").click()
    expect(page.locator("#login_button_container")).to_be_visible()
    page.close()
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
