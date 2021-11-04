import json
import logging
import os
from pathlib import Path
import requests
import shutil


class UtilManager:
    def __init__(self, handler):
        self.spotify_handler = handler
        self.data_handler = DataManager()

    def get_top_tracks(self, limit: int, time_range: str, dump: bool = False) -> list:
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
                "id": item["album"]["id"],
                "image": item["album"]["images"][2]["url"]
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
        self.base_folder = (
                Path(os.path.dirname(os.path.realpath(__file__ + "/..")))
                / "cache"
        )  # ? change cache dir later?

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
        for image in metadata:
            filename = self.base_folder / "images" / image["id"]
            link = image["image"]
            try:
                if not os.path.exists(filename):
                    _req = requests.get(link, timeout=2)
                    with open(filename, "wb") as file:
                        file.write(_req.content)
            except requests.exceptions.ConnectionError as error:
                logging.error("Couldn't download {}: {}".format(link, error))
            except requests.exceptions.MissingSchema as error:
                logging.debug("Broken image link: {}".format(error))
