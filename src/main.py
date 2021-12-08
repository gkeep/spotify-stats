import m_config
from m_util import UtilManager, DirManager
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import logging
import sys

from PyQt5 import QtWidgets

import gui_helper

logging.basicConfig(filename=DirManager().log_dir() / 'spotify-stats.log', filemode='w', level=logging.DEBUG)
logging.getLogger('urllib3').setLevel(logging.WARNING)
logging.getLogger('spotipy').setLevel(logging.WARNING)


def start_window(metadata: list):
    logging.debug("starting gui")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = gui_helper.UI_Main(MainWindow, util)
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
    util = UtilManager(spotify_handler)

    # util.clean_cache()

    # top = util.get_top_artists(10, "medium_term", dump=False)

    top = util.get_top_tracks(10, "medium_term", dump=False)

    start_window(top)
