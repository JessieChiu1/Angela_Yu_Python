import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
from spotipy.oauth2 import SpotifyOAuth

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

response = requests.get(url=url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

# =======
# Spotipy
# =======

# https://spotipy.readthedocs.io/en/2.13.0/#spotipy.oauth2.SpotifyOAuth

# this is like your 0Auth info
# scope - what you allow the project can do
# cache_path - saving the token somewhere
sp_auth = SpotifyOAuth(
    client_id=spotify_client_id,
    client_secret=spotify_client_secret,
    redirect_uri="http://example.com",
    scope="playlist-modify-private",
    cache_path="token.txt",
    username=spotify_username,
)

# Send the OAuth object to get an access token
access_token_info = sp_auth.get_access_token()
