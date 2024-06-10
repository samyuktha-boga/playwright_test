import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


def setup(play: Playwright):
    browser = play.chromium.launch(headless=False) #, slow_mo=500)
    #context = browser.new_context()
    # new page
    page = browser.new_page()
    # browser url
    page.goto("https://www.saucedemo.com/")
    expect(page.locator('text=Swag Labs')).to_be_visible()
    print(page.title())