from playwright.sync_api import expect
import re
import html
import random

def test_PortValidation(page):
       page.goto("http://localhost:93/home/arr/actioncenter")
       #Enter UDP port in the text box
       porttext= page.locator('xpath=//input[@type="number" and starts-with(@id,"mat-input-")]')
       expect(porttext).to_be_visible()
       expect(porttext).to_be_enabled()
       randno=str(random.randint(3000, 4000))
       porttext.fill(randno)
       #click on the + sign to add the port as listening port
       addportbtn=page.locator('xpath=//button[@aria-label="Add"]')
       expect(addportbtn).to_be_enabled()
       addportbtn.click()
       print("A new port added successfully:",randno)
       

