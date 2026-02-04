import pytest
from playwright.sync_api import expect
import re
import html
import random

@pytest.mark.order(4)
def test_SupportedLog(page):
       page.goto("http://localhost:93/home/arr/supportedlog")
       #Capture the number of supported log
       logtext= page.locator('xpath=//mat-chip[@role="option" and normalize-space() = string(number(normalize-space()))]')
       #get the outerhtml and the value
       expect(logtext).to_be_visible()
       outer_html = logtext.evaluate("el => el.outerHTML")
       m = re.search(r'(\d+)\s*</mat-chip>', outer_html)
       value = m.group(1) if m else None
       print("The number of supported log is:",value)
