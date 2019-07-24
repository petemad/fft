# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 350)
        MainWindow.setMinimumSize(QtCore.QSize(500, 350))
        MainWindow.setMaximumSize(QtCore.QSize(500, 350))
        MainWindow.setBaseSize(QtCore.QSize(500, 350))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(38, 38, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(38, 38, 38))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        MainWindow.setPalette(palette)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Fourier.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setEnabled(False)
        self.btnStart.setGeometry(QtCore.QRect(20, 20, 81, 61))
        self.btnStart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("start.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStart.setIcon(icon1)
        self.btnStart.setObjectName("btnStart")
        self.btnPause = QtWidgets.QPushButton(self.centralwidget)
        self.btnPause.setEnabled(False)
        self.btnPause.setGeometry(QtCore.QRect(110, 20, 101, 31))
        self.btnPause.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPause.setMouseTracking(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("index.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPause.setIcon(icon2)
        self.btnPause.setObjectName("btnPause")
        self.btnBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.btnBrowse.setGeometry(QtCore.QRect(220, 20, 161, 61))
        self.btnBrowse.setObjectName("btnBrowse")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(40, 280, 431, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.lblOriginal = QtWidgets.QLabel(self.centralwidget)
        self.lblOriginal.setGeometry(QtCore.QRect(130, 250, 67, 17))
        self.lblOriginal.setObjectName("lblOriginal")
        self.lblFft = QtWidgets.QLabel(self.centralwidget)
        self.lblFft.setGeometry(QtCore.QRect(320, 250, 81, 17))
        self.lblFft.setObjectName("lblFft")
        self.TextBoxPixel = QtWidgets.QTextEdit(self.centralwidget)
        self.TextBoxPixel.setGeometry(QtCore.QRect(393, 50, 101, 31))
        self.TextBoxPixel.setProperty("integer", 1)
        self.TextBoxPixel.setObjectName("TextBoxPixel")
        self.lblPixel = QtWidgets.QLabel(self.centralwidget)
        self.lblPixel.setGeometry(QtCore.QRect(400, 20, 91, 31))
        self.lblPixel.setObjectName("lblPixel")
        self.lblImg = QtWidgets.QLabel(self.centralwidget)
        self.lblImg.setGeometry(QtCore.QRect(86, 106, 128, 128))
        self.lblImg.setMinimumSize(QtCore.QSize(128, 128))
        self.lblImg.setMaximumSize(QtCore.QSize(128, 128))
        self.lblImg.setText("")
        self.lblImg.setObjectName("lblImg")
        self.lblImgFft = QtWidgets.QLabel(self.centralwidget)
        self.lblImgFft.setGeometry(QtCore.QRect(286, 106, 128, 128))
        self.lblImgFft.setMinimumSize(QtCore.QSize(128, 128))
        self.lblImgFft.setMaximumSize(QtCore.QSize(128, 128))
        self.lblImgFft.setText("")
        self.lblImgFft.setObjectName("lblImgFft")
        self.timeText = QtWidgets.QTextEdit(self.centralwidget)
        self.timeText.setGeometry(QtCore.QRect(120, 50, 81, 31))
        self.timeText.setProperty("integer", 1)
        self.timeText.setObjectName("timeText")
        self.lblOriginal.raise_()
        self.btnStart.raise_()
        self.lblFft.raise_()
        self.btnPause.raise_()
        self.btnBrowse.raise_()
        self.progressBar.raise_()
        self.TextBoxPixel.raise_()
        self.lblPixel.raise_()
        self.lblImg.raise_()
        self.lblImgFft.raise_()
        self.timeText.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fourier Transfromer"))
        self.btnStart.setText(_translate("MainWindow", "Start"))
        self.btnPause.setText(_translate("MainWindow", "Pause/Edit"))
        self.btnBrowse.setText(_translate("MainWindow", "Choose Image"))
        self.lblOriginal.setText(_translate("MainWindow", "Image"))
        self.lblFft.setText(_translate("MainWindow", "Image FFT"))
        self.lblPixel.setText(_translate("MainWindow", "num of pixels"))
