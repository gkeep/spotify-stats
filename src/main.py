import sps_config
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import logging


def prompt_user() -> str:
    username = input("Username: ")

    if not username:
        prompt_user()

    return username

config_manager = sps_config.ConfigManager()

scope = "user-library-read"
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# user = prompt_user()
user = "gkeep77"

result = spotify.current_user_top_artists(15, 0, "long_term")
print()

# results = spotify.search(q='artist:' + "Radiohead", type='artist')
# items = results['artists']['items']
# print(items)
# if len(items) > 0:
#     artist = items[0]
#     print(artist['name'], artist["images"][0]['url'])
