# Art Search

**Who it's for:** People who want to quickly look up artworks at the Art Institute of Chicago by title, artist, or type.

## How to run it

In the `hw4` folder, with your venv on:

    pip install flask requests
    flask --app app run --debug --port 5001

Then open http://127.0.0.1:5001 in your browser. Ctrl+C stops it.

(Port 5001 instead of 5000, because AirPlay uses 5000 on Macs.)

## Screenshot

![Results page for a search](screenshot.png)