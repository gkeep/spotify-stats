from pathlib import Path
import os
from dotenv import load_dotenv
import logging
from m_util import DirManager


class ConfigManager:
    def __init__(self):
        cfg_dir_path = DirManager().config_dir()
        load_dotenv(cfg_dir_path / "env")

        self.client_id = os.getenv("SPOTIPY_CLIENT_ID")
        self.client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
        self.redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")
        self.scope = os.getenv("SPOTIFY_SCOPE")

        var_list = ["client_id", "client_secret", "redirect_uri", "scope"]
        for item in var_list:
            value = getattr(self, item)
            if not value:
                logging.error(f"env:{item} is not set")
