from playwright.sync_api import Page, Playwright
from playwright.sync_api import Playwright, sync_playwright, expect


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.page.goto("https://www.saucedemo.com/")

        self.username_ = self.page.locator("[data-test=\"username\"]")
        self.password_ = self.page.locator("[data-test=\"password\"]")

        self.login_btn = self.page.locator('//*[@id="login-button"]')

    def login(self, uname, pwd):
        self.username_ = uname
        self.password_ = pwd
        self.login_btn.click()

