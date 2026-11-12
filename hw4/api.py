# api.py: will call the Art Institute of Chicago API to search for artworks.
# SKELETON: search_art() returns fake data for now, so the whole path works before the API does.
import requests

URL = "https://api.artic.edu/api/v1/artworks/search"

# Fake data, same shape as the real API's "data" list.
FAKE_ART = [
    {"title": "Fake Art One", "artist_title": "Montgomery"},
    {"title": "Fake Art Two", "artist_title": "Baldman"},
    {"title": "Fake Art Three", "artist_title": None},   # missing artist
]

FAKE_EMPTY = []      # no results
FAKE_ERROR = None    # API call failed

# Change this line to try a different case
FAKE_DATA = FAKE_ART


def search_art(term):
    # Fake for now. Later this calls the real API.
    return FAKE_DATA


# ---- Next step: the real call ----
# try/except (Class 10) is OPTIONAL for HW4: a status code check is enough.
# It catches the case where the API never answers: no wifi, wrong domain, too slow.
def get_books_real(author):
    try:
        # timeout=10: stop waiting after 10 seconds instead of hanging forever
        r = requests.get(URL, params={"author": author}, timeout=10,
                         headers={"User-Agent": "HCDE310 books app"})
    except requests.RequestException:
        # No answer at all. There's no status code to check, so return None
        print("API error: no answer")     # for you, in the terminal
        return None

    if r.status_code != 200:
        # The API answered, and the answer was "no" (404, 500...)
        print("API error:", r.status_code, r.reason)
        return None

    return r.json()["docs"][:10]          # [:10] = the first 10 books
