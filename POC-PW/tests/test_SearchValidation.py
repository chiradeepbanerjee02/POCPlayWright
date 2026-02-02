from playwright.sync_api import expect

def test_SearchValidation(page):
       page.goto("http://localhost:93")
       button = page.get_by_role("button", name="Search", exact=True)
       expect(button).to_be_visible()
       expect(button).to_be_enabled()
       button.click()
       print("Validate that the Search Result is displayed")
       el = page.locator("xpath=//cdk-virtual-scroll-viewport//table")
       expect(el).to_have_count(1)     # exists in DOM
       # or, if it must be visible:
       expect(el).to_be_visible()


