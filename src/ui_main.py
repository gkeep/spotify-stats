# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(806, 636)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(600, 550))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.albumArt = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.albumArt.sizePolicy().hasHeightForWidth())
        self.albumArt.setSizePolicy(sizePolicy)
        self.albumArt.setMaximumSize(QtCore.QSize(100, 100))
        self.albumArt.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.albumArt.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.albumArt.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.albumArt.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.albumArt.setSceneRect(QtCore.QRectF(0.0, 0.0, 0.0, 0.0))
        self.albumArt.setObjectName("albumArt")
        self.horizontalLayout.addWidget(self.albumArt)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, -1, -1, -1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.artsitName = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.artsitName.setFont(font)
        self.artsitName.setObjectName("artsitName")
        self.verticalLayout.addWidget(self.artsitName)
        self.albumName = QtWidgets.QLabel(self.centralwidget)
        self.albumName.setObjectName("albumName")
        self.verticalLayout.addWidget(self.albumName)
        self.songName = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songName.sizePolicy().hasHeightForWidth())
        self.songName.setSizePolicy(sizePolicy)
        self.songName.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.songName.setFont(font)
        self.songName.setObjectName("songName")
        self.verticalLayout.addWidget(self.songName)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_11.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.albumArt_2 = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.albumArt_2.sizePolicy().hasHeightForWidth())
        self.albumArt_2.setSizePolicy(sizePolicy)
        self.albumArt_2.setMaximumSize(QtCore.QSize(100, 100))
        self.albumArt_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.albumArt_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.albumArt_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.albumArt_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.albumArt_2.setSceneRect(QtCore.QRectF(0.0, 0.0, 0.0, 0.0))
        self.albumArt_2.setObjectName("albumArt_2")
        self.horizontalLayout_2.addWidget(self.albumArt_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(5, -1, -1, -1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.artsitName_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.artsitName_2.setFont(font)
        self.artsitName_2.setObjectName("artsitName_2")
        self.verticalLayout_2.addWidget(self.artsitName_2)
        self.albumName_2 = QtWidgets.QLabel(self.centralwidget)
        self.albumName_2.setObjectName("albumName_2")
        self.verticalLayout_2.addWidget(self.albumName_2)
        self.songName_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songName_2.sizePolicy().hasHeightForWidth())
        self.songName_2.setSizePolicy(sizePolicy)
        self.songName_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.songName_2.setFont(font)
        self.songName_2.setObjectName("songName_2")
        self.verticalLayout_2.addWidget(self.songName_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_11.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.albumArt_3 = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.albumArt_3.sizePolicy().hasHeightForWidth())
        self.albumArt_3.setSizePolicy(sizePolicy)
        self.albumArt_3.setMaximumSize(QtCore.QSize(100, 100))
        self.albumArt_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.albumArt_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.albumArt_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.albumArt_3.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.albumArt_3.setSceneRect(QtCore.QRectF(0.0, 0.0, 0.0, 0.0))
        self.albumArt_3.setObjectName("albumArt_3")
        self.horizontalLayout_3.addWidget(self.albumArt_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(5, -1, -1, -1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.artsitName_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.artsitName_3.setFont(font)
        self.artsitName_3.setObjectName("artsitName_3")
        self.verticalLayout_3.addWidget(self.artsitName_3)
        self.albumName_3 = QtWidgets.QLabel(self.centralwidget)
        self.albumName_3.setObjectName("albumName_3")
        self.verticalLayout_3.addWidget(self.albumName_3)
        self.songName_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songName_3.sizePolicy().hasHeightForWidth())
        self.songName_3.setSizePolicy(sizePolicy)
        self.songName_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.songName_3.setFont(font)
        self.songName_3.setObjectName("songName_3")
        self.verticalLayout_3.addWidget(self.songName_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_11.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.albumArt_4 = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.albumArt_4.sizePolicy().hasHeightForWidth())
        self.albumArt_4.setSizePolicy(sizePolicy)
        self.albumArt_4.setMaximumSize(QtCore.QSize(100, 100))
        self.albumArt_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.albumArt_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.albumArt_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.albumArt_4.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.albumArt_4.setSceneRect(QtCore.QRectF(0.0, 0.0, 0.0, 0.0))
        self.albumArt_4.setObjectName("albumArt_4")
        self.horizontalLayout_4.addWidget(self.albumArt_4)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(5, -1, -1, -1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.artsitName_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.artsitName_4.setFont(font)
        self.artsitName_4.setObjectName("artsitName_4")
        self.verticalLayout_4.addWidget(self.artsitName_4)
        self.albumName_4 = QtWidgets.QLabel(self.centralwidget)
        self.albumName_4.setObjectName("albumName_4")
        self.verticalLayout_4.addWidget(self.albumName_4)
        self.songName_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songName_4.sizePolicy().hasHeightForWidth())
        self.songName_4.setSizePolicy(sizePolicy)
        self.songName_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.songName_4.setFont(font)
        self.songName_4.setObjectName("songName_4")
        self.verticalLayout_4.addWidget(self.songName_4)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_11.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.albumArt_5 = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.albumArt_5.sizePolicy().hasHeightForWidth())
        self.albumArt_5.setSizePolicy(sizePolicy)
        self.albumArt_5.setMaximumSize(QtCore.QSize(100, 100))
        self.albumArt_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.albumArt_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.albumArt_5.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.albumArt_5.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.albumArt_5.setSceneRect(QtCore.QRectF(0.0, 0.0, 0.0, 0.0))
        self.albumArt_5.setObjectName("albumArt_5")
        self.horizontalLayout_5.addWidget(self.albumArt_5)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(5, -1, -1, -1)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.artsitName_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.artsitName_5.setFont(font)
        self.artsitName_5.setObjectName("artsitName_5")
        self.verticalLayout_5.addWidget(self.artsitName_5)
        self.albumName_5 = QtWidgets.QLabel(self.centralwidget)
        self.albumName_5.setObjectName("albumName_5")
        self.verticalLayout_5.addWidget(self.albumName_5)
        self.songName_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songName_5.sizePolicy().hasHeightForWidth())
        self.songName_5.setSizePolicy(sizePolicy)
        self.songName_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.songName_5.setFont(font)
        self.songName_5.setObjectName("songName_5")
        self.verticalLayout_5.addWidget(self.songName_5)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_11.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_11.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.albumArt_6 = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.albumArt_6.sizePolicy().hasHeightForWidth())
        self.albumArt_6.setSizePolicy(sizePolicy)
        self.albumArt_6.setMaximumSize(QtCore.QSize(100, 100))
        self.albumArt_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.albumArt_6.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.albumArt_6.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.albumArt_6.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.albumArt_6.setSceneRect(QtCore.QRectF(0.0, 0.0, 0.0, 0.0))
        self.albumArt_6.setObjectName("albumArt_6")
        self.horizontalLayout_6.addWidget(self.albumArt_6)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(5, -1, -1, -1)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.artsitName_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.artsitName_6.setFont(font)
        self.artsitName_6.setObjectName("artsitName_6")
        self.verticalLayout_6.addWidget(self.artsitName_6)
        self.albumName_6 = QtWidgets.QLabel(self.centralwidget)
        self.albumName_6.setObjectName("albumName_6")
        self.verticalLayout_6.addWidget(self.albumName_6)
        self.songName_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songName_6.sizePolicy().hasHeightForWidth())
        self.songName_6.setSizePolicy(sizePolicy)
        self.songName_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.songName_6.setFont(font)
        self.songName_6.setObjectName("songName_6")
        self.verticalLayout_6.addWidget(self.songName_6)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.verticalLayout_12.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.albumArt_7 = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.albumArt_7.sizePolicy().hasHeightForWidth())
        self.albumArt_7.setSizePolicy(sizePolicy)
        self.albumArt_7.setMaximumSize(QtCore.QSize(100, 100))
        self.albumArt_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.albumArt_7.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.albumArt_7.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.albumArt_7.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.albumArt_7.setSceneRect(QtCore.QRectF(0.0, 0.0, 0.0, 0.0))
        self.albumArt_7.setObjectName("albumArt_7")
        self.horizontalLayout_7.addWidget(self.albumArt_7)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(5, -1, -1, -1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.artsitName_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.artsitName_7.setFont(font)
        self.artsitName_7.setObjectName("artsitName_7")
        self.verticalLayout_7.addWidget(self.artsitName_7)
        self.albumName_7 = QtWidgets.QLabel(self.centralwidget)
        self.albumName_7.setObjectName("albumName_7")
        self.verticalLayout_7.addWidget(self.albumName_7)
        self.songName_7 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songName_7.sizePolicy().hasHeightForWidth())
        self.songName_7.setSizePolicy(sizePolicy)
        self.songName_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.songName_7.setFont(font)
        self.songName_7.setObjectName("songName_7")
        self.verticalLayout_7.addWidget(self.songName_7)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        self.verticalLayout_12.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.albumArt_8 = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.albumArt_8.sizePolicy().hasHeightForWidth())
        self.albumArt_8.setSizePolicy(sizePolicy)
        self.albumArt_8.setMaximumSize(QtCore.QSize(100, 100))
        self.albumArt_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.albumArt_8.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.albumArt_8.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.albumArt_8.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.albumArt_8.setSceneRect(QtCore.QRectF(0.0, 0.0, 0.0, 0.0))
        self.albumArt_8.setObjectName("albumArt_8")
        self.horizontalLayout_8.addWidget(self.albumArt_8)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(5, -1, -1, -1)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.artsitName_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.artsitName_8.setFont(font)
        self.artsitName_8.setObjectName("artsitName_8")
        self.verticalLayout_8.addWidget(self.artsitName_8)
        self.albumName_8 = QtWidgets.QLabel(self.centralwidget)
        self.albumName_8.setObjectName("albumName_8")
        self.verticalLayout_8.addWidget(self.albumName_8)
        self.songName_8 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songName_8.sizePolicy().hasHeightForWidth())
        self.songName_8.setSizePolicy(sizePolicy)
        self.songName_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.songName_8.setFont(font)
        self.songName_8.setObjectName("songName_8")
        self.verticalLayout_8.addWidget(self.songName_8)
        self.horizontalLayout_8.addLayout(self.verticalLayout_8)
        self.verticalLayout_12.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.albumArt_9 = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.albumArt_9.sizePolicy().hasHeightForWidth())
        self.albumArt_9.setSizePolicy(sizePolicy)
        self.albumArt_9.setMaximumSize(QtCore.QSize(100, 100))
        self.albumArt_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.albumArt_9.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.albumArt_9.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.albumArt_9.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.albumArt_9.setSceneRect(QtCore.QRectF(0.0, 0.0, 0.0, 0.0))
        self.albumArt_9.setObjectName("albumArt_9")
        self.horizontalLayout_9.addWidget(self.albumArt_9)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(5, -1, -1, -1)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.artsitName_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.artsitName_9.setFont(font)
        self.artsitName_9.setObjectName("artsitName_9")
        self.verticalLayout_9.addWidget(self.artsitName_9)
        self.albumName_9 = QtWidgets.QLabel(self.centralwidget)
        self.albumName_9.setObjectName("albumName_9")
        self.verticalLayout_9.addWidget(self.albumName_9)
        self.songName_9 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songName_9.sizePolicy().hasHeightForWidth())
        self.songName_9.setSizePolicy(sizePolicy)
        self.songName_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.songName_9.setFont(font)
        self.songName_9.setObjectName("songName_9")
        self.verticalLayout_9.addWidget(self.songName_9)
        self.horizontalLayout_9.addLayout(self.verticalLayout_9)
        self.verticalLayout_12.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.albumArt_10 = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.albumArt_10.sizePolicy().hasHeightForWidth())
        self.albumArt_10.setSizePolicy(sizePolicy)
        self.albumArt_10.setMaximumSize(QtCore.QSize(100, 100))
        self.albumArt_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.albumArt_10.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.albumArt_10.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.albumArt_10.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.albumArt_10.setSceneRect(QtCore.QRectF(0.0, 0.0, 0.0, 0.0))
        self.albumArt_10.setObjectName("albumArt_10")
        self.horizontalLayout_10.addWidget(self.albumArt_10)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(5, -1, -1, -1)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.artsitName_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.artsitName_10.setFont(font)
        self.artsitName_10.setObjectName("artsitName_10")
        self.verticalLayout_10.addWidget(self.artsitName_10)
        self.albumName_10 = QtWidgets.QLabel(self.centralwidget)
        self.albumName_10.setObjectName("albumName_10")
        self.verticalLayout_10.addWidget(self.albumName_10)
        self.songName_10 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songName_10.sizePolicy().hasHeightForWidth())
        self.songName_10.setSizePolicy(sizePolicy)
        self.songName_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.songName_10.setFont(font)
        self.songName_10.setObjectName("songName_10")
        self.verticalLayout_10.addWidget(self.songName_10)
        self.horizontalLayout_10.addLayout(self.verticalLayout_10)
        self.verticalLayout_12.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11.addLayout(self.verticalLayout_12)
        self.verticalLayout_13.addLayout(self.horizontalLayout_11)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.artsitName.setText(_translate("MainWindow", "Unknown Artist"))
        self.albumName.setText(_translate("MainWindow", "Unknown Album"))
        self.songName.setText(_translate("MainWindow", "Unknown Song"))
        self.artsitName_2.setText(_translate("MainWindow", "Unknown Artist"))
        self.albumName_2.setText(_translate("MainWindow", "Unknown Album"))
        self.songName_2.setText(_translate("MainWindow", "Unknown Song"))
        self.artsitName_3.setText(_translate("MainWindow", "Unknown Artist"))
        self.albumName_3.setText(_translate("MainWindow", "Unknown Album"))
        self.songName_3.setText(_translate("MainWindow", "Unknown Song"))
        self.artsitName_4.setText(_translate("MainWindow", "Unknown Artist"))
        self.albumName_4.setText(_translate("MainWindow", "Unknown Album"))
        self.songName_4.setText(_translate("MainWindow", "Unknown Song"))
        self.artsitName_5.setText(_translate("MainWindow", "Unknown Artist"))
        self.albumName_5.setText(_translate("MainWindow", "Unknown Album"))
        self.songName_5.setText(_translate("MainWindow", "Unknown Song"))
        self.artsitName_6.setText(_translate("MainWindow", "Unknown Artist"))
        self.albumName_6.setText(_translate("MainWindow", "Unknown Album"))
        self.songName_6.setText(_translate("MainWindow", "Unknown Song"))
        self.artsitName_7.setText(_translate("MainWindow", "Unknown Artist"))
        self.albumName_7.setText(_translate("MainWindow", "Unknown Album"))
        self.songName_7.setText(_translate("MainWindow", "Unknown Song"))
        self.artsitName_8.setText(_translate("MainWindow", "Unknown Artist"))
        self.albumName_8.setText(_translate("MainWindow", "Unknown Album"))
        self.songName_8.setText(_translate("MainWindow", "Unknown Song"))
        self.artsitName_9.setText(_translate("MainWindow", "Unknown Artist"))
        self.albumName_9.setText(_translate("MainWindow", "Unknown Album"))
        self.songName_9.setText(_translate("MainWindow", "Unknown Song"))
        self.artsitName_10.setText(_translate("MainWindow", "Unknown Artist"))
        self.albumName_10.setText(_translate("MainWindow", "Unknown Album"))
        self.songName_10.setText(_translate("MainWindow", "Unknown Song"))
