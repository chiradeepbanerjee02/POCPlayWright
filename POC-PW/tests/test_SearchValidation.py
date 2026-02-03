import pytest
from playwright.sync_api import expect
import re
import html

@pytest.mark.order(2)
def test_SearchValidation(shared_page):
       """
       This test depends on test_TitleValidation running first.
       It reuses the same browser page that was navigated to http://localhost:93
       by test_TitleValidation, maintaining all browser state and DOM.
       
       Note: If test_TitleValidation fails or is skipped, this test will also fail.
       """
       # Browser continues from where test_TitleValidation left off
       # No need to navigate again - reusing the same page
       startdatebutton= shared_page.locator("xpath=//*[@id='cdk-accordion-child-0']//mat-form-field[.//mat-label[normalize-space()='Event start date']]//button[@matsuffix and @aria-label='Select date']")
       expect(startdatebutton).to_be_visible()
       expect(startdatebutton).to_be_enabled()
       startdatebutton.click()
       clearbutton=shared_page.locator("xpath=//mat-dialog-container//app-lookup-date//div[contains(@class,'mat-dialog-actions') or self::mat-dialog-actions]//button[normalize-space()='Clear']")
       expect(clearbutton).to_be_visible()
       expect(clearbutton).to_be_enabled()
       clearbutton.click()
       searchbutton = shared_page.locator("xpath=(//*[@id='cdk-accordion-child-0']//button)[last()-0]")
       expect(searchbutton).to_be_visible()
       expect(searchbutton).to_be_enabled()
       searchbutton.click()
       print("Validate that the Search Result is displayed")
       el = shared_page.locator("xpath=//cdk-virtual-scroll-viewport//table")
       expect(el).to_have_count(1)     # exists in DOM
       # or, if it must be visible:
       expect(el).to_be_visible()
       print("Copy the first audit log to output")
       print("*************************************************")
       searchresultrow=page.locator("xpath=//cdk-virtual-scroll-viewport//table//tbody/tr[2]")
       expect(searchresultrow).to_be_visible()
       searchresultrow.click()
       auditmsg=page.locator("xpath=//app-record-viewer//app-record-details/*[1]/*[1]")
       expect(auditmsg).to_be_visible()
       outer_html = auditmsg.evaluate("el => el.outerHTML")
       m = re.search(r"<textarea\b[^>]*>(.*?)</textarea>", outer_html, flags=re.DOTALL | re.IGNORECASE)
       textarea_inner = m.group(1).strip() if m else None
       xml_text = html.unescape(textarea_inner)
       print(xml_text)
       print("*************************************************")





