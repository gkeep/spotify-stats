import m_config
from m_util import UtilManager
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import logging
import sys

from PyQt5 import QtWidgets

import gui_helper

logging.basicConfig(filename='spotify-stats.log', filemode='w', encoding='utf-8', level=logging.DEBUG)
logging.getLogger('urllib3').setLevel(logging.WARNING)
logging.getLogger('spotipy').setLevel(logging.WARNING)


def start_window(metadata):
    logging.debug("starting gui")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gui_helper.UI_Main(MainWindow, util)

    ui.setupUi(MainWindow)
    ui.display(metadata)

    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    logging.debug("starting the application")

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

    # top = util.get_top_artists(10, "medium_term", dump=False)
    # print(json.dumps(top, indent=2))

    top = util.get_top_tracks(10, "medium_term", dump=False)
    # print(json.dumps(top, indent=2))

    start_window(top)
