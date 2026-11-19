# AI Use – HW5

## Tools
Claude (claude.ai), used in two chats on Nov 18, 2026: one for the Step 4 code review, one as a tutor for the whole assignment.

## 1. Step 4 code review (Claude)
I asked: "Review this Flask app for bugs, missing error handling, accessibility and security problems. For each one, point to the line." I pasted app.py and api.py.

Main things it flagged:
- **Security:** `debug=True` (app.py line 26) is dangerous if deployed; showing the raw exception to users (line 21) leaks internal details; search should be GET-only (line 13); no length limit on the input (line 15)
- **Bugs:** `q` does a full-text search, so results aren't actually filtered by artist (api.py line 8); `[:10]` is redundant since `limit` is already 10; `image_id`/`artist_title` can be `None`
- **Error handling:** `except Exception` is too broad and can hide my own bugs; `.json()` can fail; error pages return status 200
- **Accessibility:** error messages need `aria-live`/`role="alert"` and images need alt text (it couldn't check my templates because I didn't send them)

## 2. My two questions (same chat)
1. What does `{% for art in artworks %}` do in results.html?
   → It loops through every artwork in the list and makes the HTML for each one.
2. What does `request.values` do in app.py?
   → It gets whatever the user typed, whether it was sent as GET or POST.

## 3. Tutoring chat (Claude)
- Explained Steps 1–3 and which steps allow AI.
- Fixed my setup: pip couldn't find requirements.txt because I was in hcde310, not hw5.
- **Step 1:** it didn't draw the diagram. It asked me questions one arrow at a time, and I found each label in the code myself. Then it summarized my answers so I could copy the diagram.
- Gave me a command to convert my .HEIC photo to JPG.
- **Step 2:** suggested example questions; I picked 2.
- **Step 3:** gave me 2 pytest outlines with blanks. I filled in "No search term entered." and "Results for" and ran them (3 passed). It suggested hand checks; I ran the app and found the fails myself (no ?artist= in the URL, no artist name, broken images, fake word "zxqwv" shows 10 random artworks).
- **Step 4:** helped me sort what the review found that I missed vs. what it got wrong, and reworded that section.
- **Step 5:** walked me through the POST → GET fix, git diff, and both commits (01a8114 → af93bec). It wrote the section 5 text; I checked it matched what I did.
- **Step 6:** I wrote my own ship-it answer. It suggested starting with "No." and adding a few words, and it wrote the 2 HW4 comparison lines.
- Helped me put this file together.

## 4. What I did myself
Read the code, drew the diagram, picked and answered my questions, ran the app and tests, found the failing checks, made the fix, checked the diff, and committed.

## 5. Reflection
Claude worked best when it asked me questions instead of giving answers, like the drawing step. Near the deadline I let it write more of the wording, so sections 4 and 5 of findings.md are less in my own words than the rest. The review found security issues I'd never have checked, like debug=True, but I only knew which of its points were wrong because I had run the app myself first.