# app.py: the routes for the books app.
# SKELETON: the whole path works (form → /results → results page) with fake data.
# Next: replace one piece at a time, and commit each time something works.
from flask import Flask, render_template, request   # request (Flask), not requests!
from api import search_art

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/results")
def results():
    # 1. Read the search word from the form
    term = request.args.get("term_search", "")
    # 2. If the search word is empty → go back to the search page with a message
    if len(term) == 0:
        return render_template("home.html", message="Type a title, artist, or type to search.")
    # 3. Call search_art with the search word
    artworks = search_art(term)
    # 4. If search_art gave back None → We couldn't reach the Art Institute. Please try again.
    if artworks is None:
        return render_template("home.html", message="We couldn't reach the Art Institute. Please try again.")
    # 5. If search_art gave back an empty list →  No artworks found, check the spelling
    if len(artworks) == 0:
        return render_template("home.html", message="No artworks found. Check the spelling")
    # 6. For each artwork, if the artist is missing → Give back Unknown artist
    for art in artworks:
        art["artist_title"] = art.get("artist_title") or "Unknown artist"
    # 7. For each artwork, if the title is missing → "Untitled"
    for art in artworks:
        art["title"] = art.get("title") or "Untitled"
    # 8. Otherwise → results page with the list of artworks

    return render_template("results.html", artworks=artworks)