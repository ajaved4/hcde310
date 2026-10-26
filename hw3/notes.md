# HW3 Part 1 – Read the response first

AI Use: Stage 2 (Tutor)

Open `sample_response.json` (a saved Art Institute of Chicago search). In `notes.md`:

---

## 1. The total number of results is at `data["pagination"]["total"]`. What's the path to the first artwork's title?

data["data"][0]["title"]


## 2. Find 3 more fields you'd want to show a user, and their paths
data["data"][0]["place_of_origin"]
data["data"][4]["dimensions"]
data["data"][2]["artwork_type_title"]

## 3. Which fields are `null` for some works?
artist title is null for data["data"][2]["artist_title"]

## 4. Predict
*open `fetch.py` and read it, but don't change anything yet. What do you think will happen when you run it?*

it will say invalid url since it has no url nothing will run


## 5. Run it
*run `python3 fetch.py`. When it asks for a search term, type a word (like `cat`) and press Enter. What actually happened? Read the traceback bottom line first: what went wrong, and which line of your file caused it?*
it was caused by this line 
response = requests.get(url, params=params)
and ut says no scheme supplied invalid url
MissingSchema at line 16