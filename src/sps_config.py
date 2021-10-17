from pathlib import Path
import os
from dotenv import load_dotenv
import logging


class ConfigManager:
    def __init__(self):
        src_path = Path(os.path.dirname(os.path.realpath(__file__ + "../../")))
        load_dotenv(src_path / ".env")

        self.clinet_id = os.getenv("SPOTIPY_CLIENT_ID")
        self.client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
        self.redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

        var_list = [self.clinet_id, self.client_secret, self.redirect_uri]
        for item in var_list:
            if item is None:
                logging.error(f"{item} is not set")
            else:
                logging.debug(f"{item} loaded")
