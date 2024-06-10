import pytest

from POM.login_page import LoginPage
from playwright.sync_api import Page,expect
from playwright.sync_api import Playwright, sync_playwright

def test_login_succesful(page: Page):
    page.goto("https://www.saucedemo.com/")

    uname = "standard_user"
    pwd = "secret_sauce"

    l_page = LoginPage(page)
    l_page.login(uname,pwd)

    expect(page.locator('//*[@id="login-button"]')).to_be_visible()
    l_page.login_btn.click()



