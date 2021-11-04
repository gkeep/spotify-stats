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
                "image": item["images"][0]["url"],
                "link": item["external_urls"]["spotify"]
            }

            items.append(item)

        return items

