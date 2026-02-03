import pytest

@pytest.mark.order(1)
def test_TitleValidation(shared_page):
       shared_page.goto("http://localhost:93")
       print("Title of Landing page is Validated")
       assert "Audit Manager" in shared_page.title(), "Title does not match the expected value"


