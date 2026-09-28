import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://automationexercise.com/")
    page.get_by_role("button", name="Zgadzam się").click()
    expect(page.get_by_role("link", name="Website for automation")).to_be_visible()
    expect(page.locator("#header")).to_contain_text(" Products")
    page.get_by_role("link", name=" Products").click()
    page.get_by_text("Add to cart").first.click()
    expect(page.locator("#cartModal")).to_contain_text("Added!")
    page.get_by_role("button", name="Continue Shopping").click()
    page.locator("div:nth-child(6) > .product-image-wrapper > .single-products > .productinfo > .btn").click()
    expect(page.locator("#cartModal")).to_contain_text("Added!")
    page.get_by_role("button", name="Continue Shopping").click()
    expect(page.locator("#header")).to_contain_text("Cart")
    page.get_by_role("link", name=" Cart").click()
    expect(page.get_by_role("row", name="Product Image Blue Top Women")).to_be_visible()
    expect(page.get_by_role("row", name="Product Image Stylish Dress")).to_be_visible()
    page.locator("#product-4 > .cart_delete > .cart_quantity_delete").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
