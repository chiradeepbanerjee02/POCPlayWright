def test_TitleValidation(page):
       page.goto("http://localhost:93")
       print("Title of Landing page is Validated")
       assert "Audit Manager" in page.title(), "Title does not match the expected value"


