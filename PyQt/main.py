# -*- coding: utf-8 -*-
import sys
import mss
import cv2
import numpy as np

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class OpencvImageEditorClass(object):
    def setupUi(self, OpencvImageEditor):
        if not OpencvImageEditor.objectName():
            OpencvImageEditor.setObjectName(u"OpencvImageEditor")
        OpencvImageEditor.resize(840, 680)
        self.centralwidget = QWidget(OpencvImageEditor)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 10, 821, 41))
        font = QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(630, 610, 91, 41))
        self.pushButton_2.setFont(font)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(630, 610, 91, 41))
        self.pushButton_3.setFont(font)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 10, 821, 41))
        self.pushButton_4.setFont(font)
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(740, 610, 91, 41))
        self.pushButton_5.setFont(font)
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(10, 60, 131, 41))
        self.pushButton_6.setFont(font)
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(160, 60, 181, 41))
        self.pushButton_7.setFont(font)
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(360, 60, 251, 41))
        font1 = QFont()
        font1.setPointSize(18)
        self.pushButton_8.setFont(font1)
        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(630, 60, 201, 41))
        self.pushButton_9.setFont(font1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 200, 821, 401))
        self.label.setPixmap(QPixmap())
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(10, 110, 821, 22))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider_2 = QSlider(self.centralwidget)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setGeometry(QRect(10, 140, 821, 22))
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)
        self.horizontalSlider_3 = QSlider(self.centralwidget)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setGeometry(QRect(10, 170, 821, 22))
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)
        OpencvImageEditor.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(OpencvImageEditor)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setCursor(QCursor(Qt.CrossCursor))
        OpencvImageEditor.setStatusBar(self.statusbar)

        self.retranslateUi(OpencvImageEditor)

        QMetaObject.connectSlotsByName(OpencvImageEditor)

        self.screenshot = np.array([])
        self.size = 1

        self.pushButton_3.clicked.connect(self.Zoomin)
        self.pushButton_5.clicked.connect(self.Zoomout)
        self.pushButton_4.clicked.connect(self.GuiCaptureScreen)
        self.pushButton_6.clicked.connect(self.Cv2GrayScale)
    # setupUi
    
    # 확대
    def Zoomin(self) -> None:
        if (self.screenshot == None).all():
            self.screenshot = self.Capture()
            self.screenshot = cv2.resize(self.screenshot, (820, 400))

        self.size = self.size + 0.1
        self.screenshot = cv2.resize(self.screenshot, (0, 0), fx=self.size, fy=self.size)
        self.ImageShow(self.screenshot)

    # 축소
    def Zoomout(self) -> None:
        if (self.screenshot == None).all():
            self.screenshot = self.Capture()
            self.screenshot = cv2.resize(self.screenshot, (820, 400))

        self.self = self.size - 0.1
        self.screenshot = cv2.resize(self.screenshot, (0, 0), fx=self.size, fy=self.size)
        self.ImageShow(self.screenshot)
        
    def GuiCaptureScreen(self) -> None:
        self.size = 1
        self.screenshot = self.Capture()
        self.ImageShow(self.screenshot)

    def Cv2GrayScale(self) -> None:
        self.size = 1
        self.screenshot = self.Capture()
        self.screenshot = cv2.resize(self.screenshot, (820, 400))

        if (len(self.screenshot.shape) != 2):
            self.screenshot = cv2.cvtColor(self.screenshot, cv2.COLOR_BGR2GRAY)
        self.ImageShow(self.screenshot)

    def Capture(self) -> np.array:
        with mss.mss() as sct:
            monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}
            screenshot = sct.grab(monitor)
            screenshot = np.array(screenshot)

            screenshot = cv2.resize(screenshot, (820, 400))
            screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)
        return screenshot

    def ImageShow(self, Image) -> None:
        if len(Image.shape) == 2:  # GrayScale
            h, w = Image.shape
            ch = 1
        else:  # 컬러 이미지
            h, w, ch = Image.shape

        bytes_per_line = ch * w
        if len(Image.shape) == 2:
            qt_image = QImage(Image.data, w, h, bytes_per_line, QImage.Format_Grayscale8)
        else:
            qt_image = QImage(Image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_image)
        self.label.setPixmap(pixmap)
        

    def retranslateUi(self, OpencvImageEditor):
        OpencvImageEditor.setWindowTitle(QCoreApplication.translate("OpencvImageEditor", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("OpencvImageEditor", u"\uc2a4\ud06c\ub9b0\uc0f7", None))
        self.pushButton_2.setText(QCoreApplication.translate("OpencvImageEditor", u"\ud655\ub300", None))
        self.pushButton_3.setText(QCoreApplication.translate("OpencvImageEditor", u"\ud655\ub300", None)) # 확대
        self.pushButton_4.setText(QCoreApplication.translate("OpencvImageEditor", u"\uc2a4\ud06c\ub9b0\uc0f7", None))
        self.pushButton_5.setText(QCoreApplication.translate("OpencvImageEditor", u"\ucd95\uc18c", None)) # 축소
        self.pushButton_6.setText(QCoreApplication.translate("OpencvImageEditor", u"grayscale", None))
        self.pushButton_7.setText(QCoreApplication.translate("OpencvImageEditor", u"Thresholding", None))
        self.pushButton_8.setText(QCoreApplication.translate("OpencvImageEditor", u"AdaptiveThresholding", None))
        self.pushButton_9.setText(QCoreApplication.translate("OpencvImageEditor", u"Gaussian Blur", None))
        self.label.setText("")
    # retranslateUi

if (__name__ == "__main__"):
    app = QApplication([])
    window = QMainWindow()
    ui = OpencvImageEditorClass()
    ui.setupUi(window)
    window.show()
    app.exec()