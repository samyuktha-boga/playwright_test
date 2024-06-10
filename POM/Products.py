from playwright.sync_api import Page, Playwright
from playwright.sync_api import Playwright, sync_playwright, expect

class details:
    def __init__(self, page: Page):
        self.firstname = self.page.locator("[data-test=\"firstName\"]")
        self.lastname = self.page.locator("[data-test=\"lastName\"]")
        self.postalcode = self.page.locator("[data-test=\"continue\"]")

    def f_details(self, fname, lname, pcode):
        self.firstname = fname
        self.lastname = lname
        self.postalcode = pcode

