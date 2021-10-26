import json


class UtilManager:
    def __init__(self, handler):
        self.spotify_handler = handler

    def get_top_tracks(self, limit: int, time_range: str) -> list:
        top_tracks = self.spotify_handler.current_user_top_tracks(
            limit=limit, time_range=time_range)
        items = []

        for item in top_tracks["items"]:
            _artists = item["artists"][0]["name"]
            _name = item["name"]
            item = {
                "artists": _artists,
                "name": _name
            }

            items.append(item)

        return items
