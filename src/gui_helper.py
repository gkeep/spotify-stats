from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap

import ui_main


class UI_Main(ui_main.Ui_MainWindow):
    def __init__(self, m_MainWindow):
        super().setupUi(m_MainWindow)

    def set_song_name(self, song_name: str):
        self.songName.setText(song_name)

    def set_artist_name(self, artist_name: str):
        self.artsitName.setText(artist_name)

    def set_image(self, img_path: str):
        pic = QPixmap(img_path)
        item = QtWidgets.QGraphicsPixmapItem(pic)
        scene = QtWidgets.QGraphicsScene()
        scene.addItem(item)
        self.albumArt.setScene(scene)
        scale_w = self.albumArt.maximumWidth() / scene.width()
        scale_h = self.albumArt.maximumHeight() / scene.height()
        self.albumArt.scale(scale_w, scale_h)

    def set_album_name(self, album_name: str):
        self.albumName.setText(album_name)
