# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from keyGenerator import Ui_windowKeyGenerator
from encryption import Ui_windowEncryption
from decryption import Ui_windowDecryption

class Ui_windowCypher(object):
    
    def openKeyGenerator(self):
        self.windowKeyGenerator = QtWidgets.QMainWindow()
        self.ui = Ui_windowKeyGenerator()
        self.ui.setupUi(self.windowKeyGenerator)
        self.windowKeyGenerator.show()

    def openEncryption(self):
        self.windowEncryption = QtWidgets.QMainWindow()
        self.ui = Ui_windowEncryption()
        self.ui.setupUi(self.windowEncryption)
        self.windowEncryption.show()

    def openDecryption(self):
        self.windowDecryption = QtWidgets.QMainWindow()
        self.ui = Ui_windowDecryption()
        self.ui.setupUi(self.windowDecryption)
        self.windowDecryption.show()
    
    def setupUi(self, windowCypher):
        windowCypher.setObjectName("windowCypher")
        windowCypher.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        windowCypher.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(windowCypher)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonGenerate = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGenerate.setGeometry(QtCore.QRect(250, 150, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.buttonGenerate.setFont(font)
        self.buttonGenerate.setObjectName("buttonGenerate")
        self.buttonGenerate.clicked.connect(self.openKeyGenerator)
        self.buttonDecrypt = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDecrypt.setGeometry(QtCore.QRect(250, 350, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.buttonDecrypt.setFont(font)
        self.buttonDecrypt.setObjectName("buttonDecrypt")
        self.buttonDecrypt.clicked.connect(self.openDecryption)
        self.buttonEncrypt = QtWidgets.QPushButton(self.centralwidget)
        self.buttonEncrypt.setGeometry(QtCore.QRect(250, 250, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.buttonEncrypt.setFont(font)
        self.buttonEncrypt.setObjectName("buttonEncrypt")
        self.buttonEncrypt.clicked.connect(self.openEncryption)
        windowCypher.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(windowCypher)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        windowCypher.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(windowCypher)
        self.statusbar.setObjectName("statusbar")
        windowCypher.setStatusBar(self.statusbar)

        self.retranslateUi(windowCypher)
        QtCore.QMetaObject.connectSlotsByName(windowCypher)

    def retranslateUi(self, windowCypher):
        _translate = QtCore.QCoreApplication.translate
        windowCypher.setWindowTitle(_translate("windowCypher", "Cypher"))
        self.buttonGenerate.setText(_translate("windowCypher", "Generate Public-Private Key"))
        self.buttonDecrypt.setText(_translate("windowCypher", "Decrypt Message"))
        self.buttonEncrypt.setText(_translate("windowCypher", "Encrypt Message"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    windowCypher = QtWidgets.QMainWindow()
    ui = Ui_windowCypher()
    ui.setupUi(windowCypher)
    windowCypher.show()
    sys.exit(app.exec_())

