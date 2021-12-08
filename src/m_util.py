import json
import logging
import os
from pathlib import Path
import requests
import shutil
import appdirs

class UtilManager:
    def __init__(self, handler):
        self.spotify_handler = handler
        self.data_handler = DataManager()

    def clean_cache(self):
        logging.info("cleaning cache...")
        self.data_handler.cleanup()

    def get_current_user(self) -> str:
        return self.spotify_handler.current_user()['display_name']

    def get_base_folder(self) -> Path:
        return self.data_handler.base_folder

    def get_top_tracks(self, limit: int, time_range: str, dump: bool = False) -> list:
        logging.debug(f"getting top tracks in {time_range}")

        top_tracks = self.spotify_handler.current_user_top_tracks(
            limit=limit, time_range=time_range)
        items = []

        if dump:
            print(json.dumps(top_tracks, indent=2))

        for item in top_tracks["items"]:
            item = {
                "artists": item["artists"][0]["name"],
                "song_name": item["name"],
                "album_name": item["album"]["name"],
                "album_id": item["album"]["id"],
                "image_link": item["album"]["images"][1]["url"]
            }

            items.append(item)

        self.data_handler.cache_images(items)
        return items

    def get_top_artists(self, limit: int, time_range: str, dump: bool = False) -> list:
        top_artists = self.spotify_handler.current_user_top_artists(
            limit=limit, time_range=time_range)
        items = []

        if dump:
            print(json.dumps(top_artists, indent=2))

        for item in top_artists["items"]:
            item = {
                "name": item["name"],
                "popularity": item["popularity"],
                "id": item["id"],
                "image": item["images"][1]["url"],
                "link": item["external_urls"]["spotify"]
            }

            items.append(item)

        self.data_handler.cache_images(items)
        return items


class DataManager:
    def __init__(self):
        self.base_folder = (DirManager().cache_dir())

        if not os.path.exists(self.base_folder / "images"):
            if not os.path.exists(self.base_folder):
                os.mkdir(self.base_folder)
            os.mkdir(self.base_folder / "images")

    def cleanup(self):
        try:
            shutil.rmtree(self.base_folder)
        except FileNotFoundError:
            logging.error("Couldn't remove temp folder")
        finally:
            logging.debug("Successfully removed temp folder")

        if not os.path.exists(self.base_folder / "images"):
            if not os.path.exists(self.base_folder):
                os.mkdir(self.base_folder)
            os.mkdir(self.base_folder / "images")

    def cache_images(self, metadata):
        logging.debug("caching images...")
        for image in metadata:
            filename = self.base_folder / "images" / image["album_id"]
            link = image["image_link"]
            try:
                if not os.path.exists(filename):
                    _req = requests.get(link, timeout=2)
                    with open(filename, "wb") as file:
                        file.write(_req.content)
                        logging.debug(f"saved album art with id=[{image['album_id']}]")
                else:
                    logging.debug(f"album art [{image['album_id']}] is already cached")
            except requests.exceptions.ConnectionError as error:
                logging.error("Couldn't download {}: {}".format(link, error))
            except requests.exceptions.MissingSchema as error:
                logging.debug("Broken image link: {}".format(error))

class DirManager:
    def __init__(self):
        author = "gkeep"
        app_name = "spotify-stats"

        self.config_directory = appdirs.user_config_dir(app_name, author)
        self.cache_directory = appdirs.user_cache_dir(app_name, author)
        self.log_directory = appdirs.user_log_dir(app_name, author)

    def config_dir(self) -> Path:
        if not os.path.exists(self.config_directory):
            os.mkdir(self.config_directory)
        return Path(self.config_directory)

    def cache_dir(self) -> Path:
        if not os.path.exists(self.cache_directory):
            os.mkdir(self.cache_directory)
        return Path(self.cache_directory)

    def log_dir(self) -> Path:
        if not os.path.exists(self.log_directory):
            os.mkdir(self.log_directory)
        return Path(self.log_directory)