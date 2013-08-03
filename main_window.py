# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Sat Aug 03 23:18:10 2013
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_kalah_window(object):
    def setupUi(self, kalah_window):
        kalah_window.setObjectName(_fromUtf8("kalah_window"))
        kalah_window.resize(688, 335)
        self.board = QtGui.QGraphicsView(kalah_window)
        self.board.setGeometry(QtCore.QRect(20, 43, 537, 243))
        self.board.setViewportUpdateMode(QtGui.QGraphicsView.FullViewportUpdate)
        self.board.setObjectName(_fromUtf8("board"))
        self.active_player = QtGui.QLabel(kalah_window)
        self.active_player.setGeometry(QtCore.QRect(30, 13, 361, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.active_player.setFont(font)
        self.active_player.setScaledContents(True)
        self.active_player.setObjectName(_fromUtf8("active_player"))
        self.time_left = QtGui.QLabel(kalah_window)
        self.time_left.setGeometry(QtCore.QRect(400, 13, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.time_left.setFont(font)
        self.time_left.setScaledContents(True)
        self.time_left.setObjectName(_fromUtf8("time_left"))
        self.layoutWidget = QtGui.QWidget(kalah_window)
        self.layoutWidget.setGeometry(QtCore.QRect(570, 43, 111, 181))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.newgame = QtGui.QPushButton(self.layoutWidget)
        self.newgame.setObjectName(_fromUtf8("newgame"))
        self.verticalLayout.addWidget(self.newgame)
        self.savegame = QtGui.QPushButton(self.layoutWidget)
        self.savegame.setEnabled(False)
        self.savegame.setObjectName(_fromUtf8("savegame"))
        self.verticalLayout.addWidget(self.savegame)
        self.loadgame = QtGui.QPushButton(self.layoutWidget)
        self.loadgame.setObjectName(_fromUtf8("loadgame"))
        self.verticalLayout.addWidget(self.loadgame)
        self.history = QtGui.QPushButton(self.layoutWidget)
        self.history.setObjectName(_fromUtf8("history"))
        self.verticalLayout.addWidget(self.history)
        self.options = QtGui.QPushButton(self.layoutWidget)
        self.options.setObjectName(_fromUtf8("options"))
        self.verticalLayout.addWidget(self.options)
        self.layoutWidget1 = QtGui.QWidget(kalah_window)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 300, 171, 27))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.undo = QtGui.QPushButton(self.layoutWidget1)
        self.undo.setEnabled(False)
        self.undo.setObjectName(_fromUtf8("undo"))
        self.horizontalLayout.addWidget(self.undo)
        self.advice = QtGui.QPushButton(self.layoutWidget1)
        self.advice.setObjectName(_fromUtf8("advice"))
        self.horizontalLayout.addWidget(self.advice)

        self.retranslateUi(kalah_window)
        QtCore.QMetaObject.connectSlotsByName(kalah_window)

    def retranslateUi(self, kalah_window):
        kalah_window.setWindowTitle(QtGui.QApplication.translate("kalah_window", "KALAH Gameboard", None, QtGui.QApplication.UnicodeUTF8))
        self.active_player.setText(QtGui.QApplication.translate("kalah_window", "Player 1 moves", None, QtGui.QApplication.UnicodeUTF8))
        self.time_left.setText(QtGui.QApplication.translate("kalah_window", "Time left: 00:00", None, QtGui.QApplication.UnicodeUTF8))
        self.newgame.setText(QtGui.QApplication.translate("kalah_window", "New Game", None, QtGui.QApplication.UnicodeUTF8))
        self.savegame.setText(QtGui.QApplication.translate("kalah_window", "Save Game", None, QtGui.QApplication.UnicodeUTF8))
        self.loadgame.setText(QtGui.QApplication.translate("kalah_window", "Load Game", None, QtGui.QApplication.UnicodeUTF8))
        self.history.setText(QtGui.QApplication.translate("kalah_window", "History", None, QtGui.QApplication.UnicodeUTF8))
        self.options.setText(QtGui.QApplication.translate("kalah_window", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.undo.setText(QtGui.QApplication.translate("kalah_window", "Undo move", None, QtGui.QApplication.UnicodeUTF8))
        self.advice.setText(QtGui.QApplication.translate("kalah_window", "Make an advice", None, QtGui.QApplication.UnicodeUTF8))

