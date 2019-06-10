# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Game_interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1053, 695)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1031, 521))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setRowCount(16)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(400, 580, 121, 61))
        self.tableWidget_2.setRowCount(1)
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(540, 590, 91, 41))
        self.label.setObjectName("label")
        self.buttonStart = QtWidgets.QPushButton(self.centralwidget)
        self.buttonStart.setGeometry(QtCore.QRect(110, 590, 75, 23))
        self.buttonStart.setObjectName("buttonStart")
        self.label_score = QtWidgets.QLabel(self.centralwidget)
        self.label_score.setGeometry(QtCore.QRect(870, 570, 151, 71))
        self.label_score.setObjectName("label_score")
        self.label_level = QtWidgets.QLabel(self.centralwidget)
        self.label_level.setGeometry(QtCore.QRect(200, 580, 131, 51))
        self.label_level.setObjectName("label_level")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1053, 21))
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
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.buttonStart.setText(_translate("MainWindow", "Start"))
        self.label_score.setText(_translate("MainWindow", "Score: 0"))
        self.label_level.setText(_translate("MainWindow", "Level 0"))

