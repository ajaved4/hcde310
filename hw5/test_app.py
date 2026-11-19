# HW5 test_app.py: one example test. Add your own below it (step 5).
# Run from this folder:  python3 -m pytest
from app import app


def test_home_shows_search_form():
    client = app.test_client()        # a pretend browser, no server needed
    page = client.get("/")            # like typing "/" in the address bar
    assert page.status_code == 200    # the page loaded
    assert b"Artist name" in page.data  # the form's label is on the page


def test_empty_search_shows_message():
    client = app.test_client()
    page = client.get("/results?artist=")
    assert page.status_code == 200
    assert b"No search term entered." in page.data      # the message from app.py line 17


def test_monet_search_shows_results():
    client = app.test_client()
    page = client.get("/results?artist=Monet")
    assert page.status_code == 200
    assert b"Results for" in page.data      # the heading text from results.html <h1>