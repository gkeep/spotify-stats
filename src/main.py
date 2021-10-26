import m_config
import m_util
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import json
import logging

cfg = m_config.ConfigManager()

auth = SpotifyOAuth(
    client_id=cfg.client_id,
    client_secret=cfg.client_secret,
    redirect_uri=cfg.redirect_uri,
    scope=cfg.scope
)

spotify_handler = Spotify(auth_manager=auth)

_user = "gkeep77"
user_id = spotify_handler.user(_user)['uri']

util = m_util.UtilManager(spotify_handler)
top_tracks = util.get_top_tracks(15, "medium_term")
print(json.dumps(top_tracks, indent=2))
