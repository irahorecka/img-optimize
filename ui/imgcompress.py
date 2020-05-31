# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imgcompress.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(602, 504)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.file_list = QtWidgets.QListWidget(self.centralwidget)
        self.file_list.setGeometry(QtCore.QRect(75, 40, 451, 192))
        self.file_list.setObjectName("file_list")
        self.img_quality_slider = QtWidgets.QSlider(self.centralwidget)
        self.img_quality_slider.setGeometry(QtCore.QRect(80, 260, 181, 22))
        self.img_quality_slider.setOrientation(QtCore.Qt.Horizontal)
        self.img_quality_slider.setObjectName("img_quality_slider")
        self.source_button = QtWidgets.QPushButton(self.centralwidget)
        self.source_button.setGeometry(QtCore.QRect(80, 310, 113, 32))
        self.source_button.setObjectName("source_button")
        self.destination_button = QtWidgets.QPushButton(self.centralwidget)
        self.destination_button.setGeometry(QtCore.QRect(80, 360, 113, 32))
        self.destination_button.setObjectName("destination_button")
        self.download_button = QtWidgets.QPushButton(self.centralwidget)
        self.download_button.setGeometry(QtCore.QRect(80, 410, 113, 32))
        self.download_button.setObjectName("download_button")
        self.source_path = QtWidgets.QLabel(self.centralwidget)
        self.source_path.setGeometry(QtCore.QRect(220, 315, 301, 21))
        self.source_path.setObjectName("source_path")
        self.destination_path = QtWidgets.QLabel(self.centralwidget)
        self.destination_path.setGeometry(QtCore.QRect(220, 366, 301, 20))
        self.destination_path.setObjectName("destination_path")
        self.img_quality_box = QtWidgets.QLineEdit(self.centralwidget)
        self.img_quality_box.setGeometry(QtCore.QRect(280, 260, 61, 21))
        self.img_quality_box.setObjectName("img_quality_box")
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setGeometry(QtCore.QRect(200, 410, 113, 32))
        self.cancel_button.setObjectName("cancel_button")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 250, 113, 32))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 602, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.source_button.setText(_translate("MainWindow", "Source"))
        self.destination_button.setText(_translate("MainWindow", "Destination"))
        self.download_button.setText(_translate("MainWindow", "Download"))
        self.source_path.setText(_translate("MainWindow", "source"))
        self.destination_path.setText(_translate("MainWindow", "destination"))
        self.cancel_button.setText(_translate("MainWindow", "Cancel"))
        self.pushButton.setText(_translate("MainWindow", "Remove"))
