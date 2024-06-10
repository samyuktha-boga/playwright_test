from playwright.sync_api import Playwright, sync_playwright, expect

def test_page():
    with sync_playwright() as play:
        browser = play.chromium.launch(headless=False) #, slow_mo=500)
        # new page
        page = browser.new_page()
        # browser url
        page.goto("https://www.saucedemo.com/")
        expect(page.locator('text=Swag Labs')).to_be_visible()
        print(page.title())

        username = page.locator("[data-test=\"username\"]")
        username.fill('standard_user')
        page.locator("[data-test=\"password\"]").click()
        page.locator("[data-test=\"password\"]").fill("secret_sauce")
        page.locator("[data-test=\"password\"]").click()
        submit = page.locator('//*[@id="login-button"]')
        # print attribute id
        print("button", submit.get_attribute('id'))
        submit.click()
        # assert login button
        expect(page.locator('//*[@id="login-button"]')).not_to_be_visible()
        # print page title using locator
        Products = page.locator("//div[@data-test='secondary-header']/span[text()='Products']")
        print("secondary title:", Products.text_content())
        expect(Products).to_be_visible()
       # page.get_by_text("Login").click()
        page.locator("[data-test=\"item-4-title-link\"]").click()
        page.locator("[data-test=\"add-to-cart\"]").click()
        page.go_back()
        # page.locator("[data-test=\"back-to-products\"]").click()
        page.locator("[data-test=\"inventory-list\"] div").filter(has_text="Test.allTheThings() T-Shirt (").nth(1).click()
        page.locator("[data-test=\"item-3-img-link\"]").click()
        page.locator("[data-test=\"add-to-cart\"]").click()
        page.locator("[data-test=\"back-to-products\"]").click()
        page.locator("[data-test=\"add-to-cart-sauce-labs-onesie\"]").click()
        page.locator("[data-test=\"shopping-cart-link\"]").click()
        page.locator("[data-test=\"remove-sauce-labs-onesie\"]").click()
        page.locator("[data-test=\"checkout\"]").click()
        page.locator("id=first-name").fill("Janny")
        page.locator("[data-test=\"lastName\"]").click()
        page.locator("[data-test=\"lastName\"]").fill("Phill")
        page.locator("[data-test=\"postalCode\"]").click()
        page.locator("[data-test=\"postalCode\"]").fill("32323")
        page.locator("[data-test=\"continue\"]").click()
        page.locator("[data-test=\"finish\"]").click()
        page.locator("[data-test=\"back-to-products\"]").click()
        page.get_by_role("button", name="Open Menu").click()
        page.wait_for_selector("[data-test=\"logout-sidebar-link\"]").click()

        browser.close()






