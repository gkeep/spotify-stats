from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QColor, QPainter, QBrush
from PyQt5.QtCore import Qt
import logging

import ui_main


class UI_Main(ui_main.Ui_MainWindow):
    def __init__(self, m_MainWindow, Util):
        super().setupUi(m_MainWindow)
        self.util = Util

        self.items_list = [""]
        for i in range(2, 11):
            self.items_list.append(f"_{i}")

    def display(self, metadata):
        for idx, postfix in enumerate(self.items_list):
            img_path = str(self.util.get_base_folder() / "images" / metadata[idx]["album_id"])
            song_name = metadata[idx]["song_name"]
            artists = metadata[idx]["artists"]
            album_name = metadata[idx]["album_name"]
            self.set_song_name(getattr(self, f"songName{postfix}"), song_name)
            self.set_artist_name(getattr(self, f"artsitName{postfix}"), artists)
            self.set_album_name(getattr(self, f"albumName{postfix}"), album_name)
            self.set_image(getattr(self, f"albumArt{postfix}"), img_path)

    @staticmethod
    def set_song_name(item: QtWidgets.QLabel, song_name: str):
        item.setText(song_name)

    @staticmethod
    def set_artist_name(item: QtWidgets.QLabel, artist_name: str):
        item.setText(artist_name)

    @staticmethod
    def set_album_name(item: QtWidgets.QLabel, album_name: str):
        item.setText(album_name)

    @staticmethod
    def set_image(item: QtWidgets.QGraphicsView, img_path: str):
        pixmap = QPixmap(img_path)

        radius = 30
        rounded = QPixmap(pixmap.size())
        rounded.fill(QColor("transparent"))
        # rounded.fill(QColor("#d6d2d0"))  # change to background color

        painter = QPainter(rounded)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(pixmap))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(pixmap.rect(), radius, radius)
        painter.end()

        pix_item = QtWidgets.QGraphicsPixmapItem(rounded)

        scene = QtWidgets.QGraphicsScene()
        scene.addItem(pix_item)

        item.setScene(scene)

        scale_w = item.maximumWidth() / scene.width()
        scale_h = item.maximumHeight() / scene.height()
        item.scale(scale_w, scale_h)
