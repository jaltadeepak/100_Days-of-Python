import requests
from bs4 import BeautifulSoup

dateInp = input(
    "Which year would you like to travel to? Type the date in this format YYYY-MM-DD: "
)

datedUrl = f"https://www.billboard.com/charts/hot-100/{dateInp}/"

response = requests.get(datedUrl)

website_data = response.text

soup = BeautifulSoup(website_data, "html.parser")

listData = soup.select("li ul li h3")

songList = [listItem.getText().strip() for listItem in listData]

# print(songList)

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id="YOUR ID",
        client_secret="YOUR SECRET",
        redirect_uri="http://example.com",
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path=r"46_SpotifyPlaylist+MusicalTimeMachine\token.txt",
        username="YOUR USERNAME",
    )
)

user_id = sp.current_user()["id"]


song_uris = []
year = dateInp.split("-")[0]

for song in songList:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist on Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{dateInp} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

