# HW5 findings

## 1. Drawing: one search for "Monet"

![drawing](drawing.jpg)


## 2. Two questions about the code
1. what does {% for art in artworks %} do in results.html
2  What does request.values do in app.py? 

## 3. Checks (4 or more, at least 2 as pytest tests)
| # | Check | Pass or fail |
|---|---|---|
| 1 | pytest: empty search → "No search term entered." | Pass |
| 2 | pytest: search Monet → page says "Results for" | Pass |
| 3 | After searching, URL shows ?artist=Monet so it can be bookmarked | Fail: URL is just /results (form uses POST) |
| 4 | Each result shows the artist's name | Fail: artist_title is fetched but never shown |
| 5 | Search a made-up word (zxqwv) → see "No results found." | Fail: shows 10 unrelated artworks |
| 6 | Each result shows the artwork's image | Fail: broken image icon, only alt text shows |

## 4. AI review
What it found that I missed: The biggest one was debug=True on line 26 of app.py. I didn’t know that if someone hits an error page they can run code on your computer. It also caught that the error message prints {e} straight to the user, which shows internal stuff they shouldn’t see. Other things I missed: except Exception catches everything, so it could hide actual bugs; there’s no limit on how long the search can be; the error pages still send back a 200; and the error message isn’t set up for screen readers.
What it got wrong: It said the broken images were probably from image_id being None, but results.html already checks for that, and my results had an image_id and were still broken, so that’s not the reason. It also told me to add a “no results” message, but the template already has one. The actual problem is that a fake word like “zxqwv” still returns 10 random artworks, so that message never shows. It said alt text was missing, but the template already uses the title as alt. It also didn’t notice that artist_title gets requested but never shows up on the page, and it called [:10] a bug when it’s really just extra.
Answers to my two questions, in my own words:
1. It loops through every artwork in the list and gives the html for each one
2. it takes whatever the user inputted either as a GET or a POST.

## 5. My fix
What was wrong:
What I changed:
How I checked it works:
Commit before: (hash)  Commit after: (hash)

## 6. Can we ship it? (100–150 words)
Yes or no, and why:

One thing my HW4 does better:
One thing the AI's app does better:

AI use goes in `ai_use.md` (the five points on the AI Use Card).
