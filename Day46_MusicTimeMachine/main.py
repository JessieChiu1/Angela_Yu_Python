import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
from spotipy.oauth2 import SpotifyOAuth
import spotipy

# ===========
# load-dotenv
# ===========

load_dotenv()
spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
spotify_username = os.getenv("SPOTIFY_USERNAME")

# ====================================
# grabbing top 100 from a certain date
# ====================================
date = input("Which date do you want to create the spotify playlists from? Please enter date in YYYY-MM-DD format\n")
url = f"https://www.billboard.com/charts/hot-100/{date}"

# fetch html
response = requests.get(url=url)
html = response.text
soup = BeautifulSoup(html, "html.parser")

# isolate the song containers
song_containers = soup.find_all(name="div", class_="o-chart-results-list-row-container")

# find all the song names
song_names = [song.find(name="h3", id="title-of-a-story").text.strip() for song in song_containers]
# print(song_names)

# find the artist name
# We have to do this with span tag because the class name is not very readable
# basically, it is either the index item at position 1/3 of the span list
# if it is a new or re-entry to the top 100, it will be the 3rd span tag

artist_names = []
for song in song_containers:
    span_tags = song.find_all(name="span")
    if span_tags[1].text.strip() == "NEW" or span_tags[1].text.strip() == "RE-\nENTRY":
        artist_names.append(span_tags[3].text.strip())
    else:
        artist_names.append(span_tags[1].text.strip())

# removing any extra artists to only include the first artist name
artist_names = [artist.split("Featuring")[0].strip() for artist in artist_names]
artist_names = [artist.split("&")[0].strip() for artist in artist_names]
artist_names = [artist.split(" X ")[0].strip() for artist in artist_names]
artist_names = [artist.split(" x ")[0].strip() for artist in artist_names]
artist_names = [artist.split(" / ")[0].strip() for artist in artist_names]
# print(artist_names)

# ====================
# Spotipy Access Token
# ====================

# https://spotipy.readthedocs.io/en/2.13.0/#spotipy.oauth2.SpotifyOAuth

# this is like your 0Auth info
# scope - what you allow the project can do
# # cache_path - saving the token somewhere
sp_auth = SpotifyOAuth(
    client_id=spotify_client_id,
    client_secret=spotify_client_secret,
    redirect_uri="http://example.com",
    scope="playlist-modify-private",
    cache_path="token.txt",
    username=spotify_username,
    show_dialog=True,
)

# ======================
# Spotipy Querying Songs
# ======================

# signing into spotify
sp = spotipy.Spotify(auth_manager=sp_auth)
song_uri = []

for i in range(0, len(song_names)):
    query = f"track:{song_names[i]} year:{date.split('-')[0]}"
    search_result = sp.search(q=f"track:{song_names[i]} artist:{artist_names[i]}", type="track", limit=1)
    if search_result["tracks"]["items"]:
        song_uri.append(search_result["tracks"]["items"][0]["uri"])
    else:
        print(f"can't find {song_names[i]} by {artist_names[i]} on spotify")

print(len(song_uri))
