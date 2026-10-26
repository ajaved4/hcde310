# HW3 Part 2 + Part 3 + Part 4
#
# Instructions: README.md in this folder (same as the assignment on Canvas).

import requests

FIELDS = "id,title,artist_title,artist_display,date_display,place_of_origin,dimensions,artwork_type_title"

def count_by_artist(artworks):
    counts = {}
    for art in artworks:
        artist = art.get("artist_title") or "Unknown"
        counts[artist] = counts.get(artist, 0) + 1
    return counts

# AI-written
def save_results(artworks, filename):
    """Takes a list of artwork dicts and a filename, writes one line per artwork, returns nothing."""
    with open(filename, "w") as file:
        for art in artworks:
            artist = art["artist_title"]
            if artist is None:
                artist = "Unknown"
            file.write(art["title"] + " - " + artist + " - " + art["date_display"] + "\n")
    
term = input("Search the Art Institute for: ")

url = "https://api.artic.edu/api/v1/artworks/search"
params = {"q": term, "fields": FIELDS}
response = requests.get(url, params=params, headers={"AIC-User-Agent": "hcde310-hw3 (arsalanjaved2005@gmail.com)"})

if response.status_code != 200:
        print(f"Sorry, the search didn't work: {response.status_code} {response.reason}")
    
else:
    data = response.json()
    results = data["data"]
    if len(results) == 0:
        print(f"No artworks found for '{term}'. Try a different search.")
    else:
            for art in results:
                artist = art.get("artist_title") or "Unknown artist"
                print(f"{art['title']} - {artist} {art.get('place_of_origin')} {art.get('date_display')} {art.get('dimensions')} {art.get('artwork_type_title')}")
            print(count_by_artist(results))
            save_results(results, "results.txt")
