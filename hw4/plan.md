## 1. Sketch
(photo of your 2 paper screens)

## 2. Data
(the fields you'll show, and where each one is in the JSON)
Fields I need for the results page:

- **title**
  - Path: `data["data"][0]["title"]`
  - Can be null? No (every artwork in my sample has one)
  - If missing, show: "Untitled" (just in case)

- **artist**
  - Path: `data["data"][0]["artist_title"]`
  - Can be null? Yes (e.g. `data["data"][2]["artist_title"]` in my sample)
  - If missing, show: "Unknown artist"

## 3. Specs
### search_art(term)
### / route
### /results route

### search_art(term)
(each one: what goes in, what comes out, 2–3 checks)
- In: the search word the user typed (e.g. "monet")
- Out:
  - a list of artworks if it finds some
  - an empty list `[]` if nothing matches
  - `None` if the API call fails
- Checks:
  1. Search "monet" → see a list of results
  2. Search "xyzqq" → see the "no artworks found" message
  3. Break the URL on purpose → see the "couldn't reach" message

### / route
- In: nothing
- Out: the search page (home.html)
- Checks:
  1. Open http://127.0.0.1:5000 → see the title, label, search box and button
  2. Press Tab → focus moves to the search box, then to the button

### /results route
- In: the search word from the form (e.g. "monet")
- Out:
  - artworks found → results page (results.html) with the list
  - something wrong → search page (home.html) with a message:
    - empty search → "Type something to search…"
    - nothing found → "No artworks found… check the spelling…"
    - API error → "We couldn't reach the Art Institute…"
- Checks:
  1. Press Search with nothing typed → see "Type something to search…"
  2. Search a misspelled word like "xyzqq" → see "No artworks found…"
  3. Find a result with no artist → see "Unknown artist" (not "None")