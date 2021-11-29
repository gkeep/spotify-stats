from pathlib import Path
import os
from dotenv import load_dotenv
import logging


class ConfigManager:
    def __init__(self):
        src_path = Path(os.path.dirname(os.path.realpath(__file__ + "../../")))
        load_dotenv(src_path / ".env")

        self.client_id = os.getenv("SPOTIPY_CLIENT_ID")
        self.client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
        self.redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")
        self.scope = os.getenv("SPOTIFY_SCOPE")

        var_list = ["client_id", "client_secret", "redirect_uri", "scope"]
        for item in var_list:
            value = getattr(self, item)
            if not value:
                logging.error(f"env:{item} is not set")
