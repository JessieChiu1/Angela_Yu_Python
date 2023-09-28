# Spotify Throwback Playlist Maker 🎶

## Demo Video

<img src="https://github.com/JessieChiu1/Angela_Yu_Python/blob/main/Day46_SpotifyThrowbackPlaylist/Spotify-throwback-playlist-maker.gif" width="800px" alt="Spotify Throwback Playlist Maker demo"/>

## Introduction

This app will prompt the user for a date, web scrape the Billboard Top 100 songs with Beautiful Soup, log in to your Spotify account, create a new playlist with the specified date, and add all the songs from the Billboard Top 100 to the playlist.

## Required Libraries

Before running the script, make sure to install the following Python libraries using `pip`:

- To install `requests`, use the following command:
   ```bash
   pip install requests
   pip install bs4
   pip install python-dotenv
   pip install spotipy
   ```

## Usage

To use this app, simply follow these steps:

1. Run the script and provide a date in the format YYYY-MM-DD when prompted.

2. The script will scrape the Billboard Top 100 songs for the specified date.

3. It will then log in to your Spotify account using OAuth authentication.

4. A new private playlist will be created on Spotify, named with the provided date.

5. All the Billboard Top 100 songs from that date will be added to the playlist.


## Challenges 📚

Developing this project came with its share of challenges:

- Reading and understanding documentation, especially regarding OAuth authentication, required time and effort to figure out the necessary steps.

- Implementing OAuth login with Spotify, while not straightforward, was eventually resolved with the assistance of ChatGPT and online resources.

## Potential Features

1. **Custom Playlist Name**: Allow users to specify a custom name for the Spotify playlist instead of using the date as the default name. This customization can provide a more personalized touch to the playlists created by the app and allow users to add a unique touch to their throwback collections.

