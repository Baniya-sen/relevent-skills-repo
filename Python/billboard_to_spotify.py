import re
import json
import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.client import Spotify
from spotipy.oauth2 import SpotifyOAuth


SPOTIFY_CLIENT = "your-spotify-client-id"
SPOTIFY_SECRET = "your-spotify-client-secret"
spotify_user_id = ""
spotify_token = ""
access_consent_scope = "playlist-modify-private"


def get_top_songs_by_date(date):
    """Scrapes 100 top songs for a provided date from billboard website"""
    songs_content = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}").text
    soup = BeautifulSoup(songs_content, "html.parser")

    # Select specific ul element which has songs info
    specific_li_list = soup.select(
        'ul.lrv-a-unstyle-list li.o-chart-results-list__item.lrv-u-flex-grow-1.lrv-u-flex'
    )
    song_list = []
    artist_names_delimiter = '|'.join(("Featuring", "With", "&", "X", "x", ","))

    # Loop through each specific <li> element, find song name and artist name
    for specific_li in specific_li_list:
        h3_element = specific_li.select_one('h3#title-of-a-story.c-title.a-no-trucate')
        span_element = specific_li.select_one('span.c-label.a-no-trucate.a-font-primary-s')

        # Add song name and only 'artist name' to a dict
        if h3_element and span_element:
            song_name = h3_element.getText().strip()
            artist_name = re.split(artist_names_delimiter, span_element.getText().strip())
            song_list.append({
                "song_name": song_name,
                "artist_name": artist_name[0]
            })
    return song_list


def get_oauth_object():
    """Creates a OAuth instance of spotipy"""
    auth_manager = SpotifyOAuth(
        client_id=SPOTIFY_CLIENT,
        client_secret=SPOTIFY_SECRET,
        redirect_uri="https://example.com",
        scope=access_consent_scope
    )
    return auth_manager


def fetch_oauth_spotify_token():
    """Fetches access token from spotify and stores in a .txt file"""
    auth_manager = get_oauth_object()
    with open("token.txt", "w") as token_file:
        json.dump(
            auth_manager.get_access_token(code="200"),
            token_file,
            indent=4
        )


def get_oauth_token():
    """Gets access token from .txt file"""
    try:
        with open("token.txt") as file:
            global spotify_token
            spotify_token = "Bearer " + json.loads(file.read())["access_token"]

    # If token file does not exists, or json variable is corrupted, generate access token
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print("Some error occured in getting stored token, getting a new token from spotify!")
        fetch_oauth_spotify_token()
        get_oauth_token()


def get_user_id():
    """Gets user_id from spotify"""
    headers = {"Authorization": spotify_token}
    user_info = requests.get(url="https://api.spotify.com/v1/me", headers=headers).json()
    try:
        global spotify_user_id
        spotify_user_id = user_info["id"]

    # If token expires, generate a new one
    except KeyError:
        print(f"ERROR: Code {user_info['error']['status']}, Message: {user_info['error']['message']}")
        print("Retrying! Fetching new token...")
        fetch_oauth_spotify_token()
        get_oauth_token()
        get_user_id()


# User input for preferred date for songs
songs_date = input("Which year's top 100 songs do you want? (Format: YYYY-mm-dd) or just specify year (yyyy): ")

# Change date format to yyyy-mm-dd if provided format is yyyy/mm/dd
if "/" in songs_date:
    songs_date = "-".join(songs_date.split("/"))

# Fetch OAuth token and user ID
get_oauth_token()
get_user_id()

# Get songs info list
songs_info = get_top_songs_by_date(songs_date)

# Initialize Spotify client with OAuth token
spotify = spotipy.Spotify(auth_manager=get_oauth_object())
print("Getting songs...", end="\n\n")

# Search each song's URI from Spotify and store them in a list
songs_uri_list = []
for song in songs_info:
    results = spotify.search(q=f'artist:{song["artist_name"]} track:{song["song_name"]}')
    try:
        songs_uri_list.append(results["tracks"]["items"][0]["uri"])
    except (KeyError, IndexError):
        # Log if song not found
        print(f"Can't find '{song['song_name']}' by {song['artist_name']}")

# Create a new private playlist with new tracks
spotify_client = Spotify(auth_manager=get_oauth_object())
playlist_info = spotify_client.user_playlist_create(
    user=spotify_user_id,
    name=f"{songs_date}-Billboard-100",
    public=False,
    description="100 top Songs from Billboard website of a particular date "
                "selected from a Python program by Bhanu Pratap!"
)
# Add songs to the playlist
spotify_client.playlist_add_items(
    playlist_id=playlist_info["id"],
    items=songs_uri_list,
    position=0
)
print("Playlist created successfully!")
