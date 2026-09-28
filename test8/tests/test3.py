import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://automationexercise.com/")
    page.get_by_role("button", name="Zgadzam się").click()
    expect(page.get_by_role("link", name="Website for automation")).to_be_visible()
    expect(page.locator("#header")).to_contain_text("Products")
    page.get_by_role("link", name=" Products").click()
    expect(page.get_by_text("All Products  Added! Your")).to_be_visible()
    page.get_by_role("link", name=" View Product").first.click()
    expect(page.locator("section")).to_contain_text("Blue Top")
    expect(page.get_by_text("Category: Women > Tops")).to_be_visible()
    expect(page.locator("section")).to_contain_text("Rs. 500")
    expect(page.locator("section")).to_contain_text("Brand: Polo")
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
