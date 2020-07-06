# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'decryption.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from decryptText import decryptText

class Ui_windowDecryption(object):

    def decrypt(self):
        n = int(self.inputN.toPlainText())
        d = int(self.inputD.toPlainText())
        s = self.inputText.toPlainText()
        self.outputText.setText(decryptText(s, n, d))

    def setupUi(self, windowDecryption):
        windowDecryption.setObjectName("windowDecryption")
        windowDecryption.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        windowDecryption.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(windowDecryption)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonDecrypt = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDecrypt.setGeometry(QtCore.QRect(640, 480, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.buttonDecrypt.setFont(font)
        self.buttonDecrypt.setObjectName("buttonDecrypt")
        self.buttonDecrypt.clicked.connect(self.decrypt)
        self.labelD = QtWidgets.QLabel(self.centralwidget)
        self.labelD.setGeometry(QtCore.QRect(440, 370, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelD.setFont(font)
        self.labelD.setObjectName("labelD")
        self.labelN = QtWidgets.QLabel(self.centralwidget)
        self.labelN.setGeometry(QtCore.QRect(60, 370, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelN.setFont(font)
        self.labelN.setObjectName("labelN")
        self.inputN = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputN.setGeometry(QtCore.QRect(90, 370, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.inputN.setFont(font)
        self.inputN.setObjectName("inputN")
        self.inputD = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputD.setGeometry(QtCore.QRect(470, 370, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.inputD.setFont(font)
        self.inputD.setObjectName("inputD")
        self.outputText = QtWidgets.QTextEdit(self.centralwidget)
        self.outputText.setGeometry(QtCore.QRect(60, 50, 571, 261))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.outputText.setFont(font)
        self.outputText.setObjectName("outputText")
        self.inputText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputText.setGeometry(QtCore.QRect(60, 440, 571, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.inputText.setFont(font)
        self.inputText.setObjectName("inputText")
        windowDecryption.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(windowDecryption)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        windowDecryption.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(windowDecryption)
        self.statusbar.setObjectName("statusbar")
        windowDecryption.setStatusBar(self.statusbar)

        self.retranslateUi(windowDecryption)
        QtCore.QMetaObject.connectSlotsByName(windowDecryption)

    def retranslateUi(self, windowDecryption):
        _translate = QtCore.QCoreApplication.translate
        windowDecryption.setWindowTitle(_translate("windowDecryption", "Text Decryption"))
        self.buttonDecrypt.setText(_translate("windowDecryption", "Decrypt Text"))
        self.labelD.setText(_translate("windowDecryption", "D :"))
        self.labelN.setText(_translate("windowDecryption", "N :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    windowDecryption = QtWidgets.QMainWindow()
    ui = Ui_windowDecryption()
    ui.setupUi(windowDecryption)
    windowDecryption.show()
    sys.exit(app.exec_())

