import m_config
from m_util import UtilManager
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import json
import logging
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

import gui_helper


def start_window(metadata):
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gui_helper.UI_Main(MainWindow)

    ui.setupUi(MainWindow)
    ui.set_song_name(metadata[0]["song_name"])
    ui.set_artist_name(metadata[0]["artists"])
    ui.set_image(str(util.get_base_folder() / "images" / metadata[0]["id"]))
    # ui.set_image(str(util.get_base_folder() / "images" / "0dAMC0nNikIjhD8LeRZfhH"))
    ui.set_album_name(metadata[0]["album_name"])

    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
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

    util = UtilManager(spotify_handler)
    # util.clean_cache()

    # top = util.get_top_artists(5, "medium_term", dump=False)
    # print(json.dumps(top, indent=2))

    top = util.get_top_tracks(5, "short_term", dump=False)
    # print(json.dumps(top, indent=2))

    start_window(top)
