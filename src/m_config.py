from pathlib import Path
import os
from dotenv import load_dotenv
import logging
from m_util import DirManager


class ConfigManager:
    def __init__(self, custom_config: None):
        if custom_config:
            config = custom_config
        else:
            cfg_dir_path = DirManager().config_dir()
            config = cfg_dir_path / "config"

        load_dotenv(config)
        logging.debug(f"loading cfg from [{os.path.abspath(config)}]")

        self.client_id = os.getenv("SPOTIPY_CLIENT_ID")
        self.client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
        self.redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")
        self.scope = os.getenv("SPOTIFY_SCOPE")

        var_list = ["client_id", "client_secret", "redirect_uri", "scope"]
        for item in var_list:
            value = getattr(self, item)
            if not value:
                logging.error(f"env:{item} is not set")
