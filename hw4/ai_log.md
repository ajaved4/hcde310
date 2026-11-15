# HW4 AI Log

https://claude.ai/share/017d8873-59a9-4bfa-8c5c-7d70b73b938e

## 1. AI chats
I used Claude as a tutor (Stage 2) for planning and for help with my code.
Chat: [paste the share link here: Share button → copy link]

## 2. What the AI wrote vs. what I wrote
- **Written by the AI:** the fake data block at the top of api.py
  (`FAKE_ART`, `FAKE_EMPTY`, `FAKE_ERROR`, `FAKE_DATA`). It also gave me the
  exact params, header and return line for `search_art`, and the
  `<title>` line in results.html.
- **Changed from the class starter (`get_books_real`):** I renamed it to
  `search_art(term)` and switched it to the Art Institute API.
- **Written by me, with hints:** the `/` route and home.html, every step of
  the `/results` route (reading the term, the empty check, the None check,
  the no-results check, the missing artist/title loop, the final
  render_template), the loop and artist line in results.html, and all
  comments in my own words.
- Copilot: [say whether you accepted any of its suggestions. If not, write
  "Copilot suggested code a few times but I didn't accept it."]

## 3. What surprised me
- Searching "xyzqq" didn't give "No artworks found". It still returned
  results because the AIC search is fuzzy, so I used "12345678901234".
- `http://127.0.0.1:5000` didn't work on my Mac because AirPlay uses port
  5000. Running on port 5001 fixed it.
- My first artist fix (`artist = art.get(...) or "Unknown artist"`) didn't
  change anything on the page. It made a separate variable and left
  `art["artist_title"]` as None. I had to write the value back into the
  dictionary: `art["artist_title"] = ...`.

## 4. What I changed
- Changed my label from text inside `for=` to the right setup:
  `for="term"` matches the input's `id="term"`.
- Renamed everything from books/author to art/term so the form, route and
  template all match (`name="term_search"` ↔ `request.args.get("term_search")`).
- Changed my "no results" check word from "xyzqq" to "12345678901234".
- Replaced the class starter comments with my own.