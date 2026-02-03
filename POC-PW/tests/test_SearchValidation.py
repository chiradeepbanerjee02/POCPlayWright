from playwright.sync_api import expect

def test_SearchValidation(page):
       page.goto("http://localhost:93")
       startdatebutton= page.locator("xpath=//*[@id='cdk-accordion-child-0']//mat-form-field[.//mat-label[normalize-space()='Event start date']]//button[@matsuffix and @aria-label='Select date']")
       expect(startdatebutton).to_be_visible()
       expect(startdatebutton).to_be_enabled()
       startdatebutton.click()
       clearbutton=page.locator("xpath=//mat-dialog-container//app-lookup-date//div[contains(@class,'mat-dialog-actions') or self::mat-dialog-actions]//button[normalize-space()='Clear']")
       expect(clearbutton).to_be_visible()
       expect(clearbutton).to_be_enabled()
       clearbutton.click()
       searchbutton = page.locator("xpath=(//*[@id='cdk-accordion-child-0']//button)[last()-0]")
       expect(searchbutton).to_be_visible()
       expect(searchbutton).to_be_enabled()
       searchbutton.click()
       print("Validate that the Search Result is displayed")
       el = page.locator("xpath=//cdk-virtual-scroll-viewport//table")
       expect(el).to_have_count(1)     # exists in DOM
       # or, if it must be visible:
       expect(el).to_be_visible()



