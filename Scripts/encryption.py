# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'encryption.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from encryptText import encryptText

class Ui_windowEncryption(object):

    def setupUi(self, windowEncryption):
        windowEncryption.setObjectName("windowEncryption")
        windowEncryption.resize(800, 600)
        windowEncryption.setMinimumSize(800, 600)
        windowEncryption.setMaximumSize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        windowEncryption.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(windowEncryption)
        self.centralwidget.setObjectName("centralwidget")
        self.labelN = QtWidgets.QLabel(self.centralwidget)
        self.labelN.setGeometry(QtCore.QRect(70, 380, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelN.setFont(font)
        self.labelN.setObjectName("labelN")
        self.labelE = QtWidgets.QLabel(self.centralwidget)
        self.labelE.setGeometry(QtCore.QRect(450, 380, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelE.setFont(font)
        self.labelE.setObjectName("labelE")
        self.buttonEncrypt = QtWidgets.QPushButton(self.centralwidget)
        self.buttonEncrypt.setGeometry(QtCore.QRect(648, 490, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonEncrypt.setFont(font)
        self.buttonEncrypt.setObjectName("buttonEncrypt")
        self.buttonEncrypt.clicked.connect(self.encrypt)
        self.inputN = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputN.setGeometry(QtCore.QRect(100, 380, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inputN.setFont(font)
        self.inputN.setObjectName("inputN")
        self.inputE = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputE.setGeometry(QtCore.QRect(480, 380, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inputE.setFont(font)
        self.inputE.setObjectName("inputE")
        self.outputText = QtWidgets.QTextEdit(self.centralwidget)
        self.outputText.setGeometry(QtCore.QRect(70, 50, 571, 261))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.outputText.setFont(font)
        self.outputText.setObjectName("outputText")
        self.inputText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputText.setGeometry(QtCore.QRect(70, 450, 571, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.inputText.setFont(font)
        self.inputText.setObjectName("inputText")
        windowEncryption.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(windowEncryption)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        windowEncryption.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(windowEncryption)
        self.statusbar.setObjectName("statusbar")
        windowEncryption.setStatusBar(self.statusbar)

        self.retranslateUi(windowEncryption)
        QtCore.QMetaObject.connectSlotsByName(windowEncryption)


    def encrypt(self):
        x = self.inputN.toPlainText()
        y = self.inputE.toPlainText()
        s = self.inputText.toPlainText()

        if (not len(x) or not len(y) or not len(s)):
            self.displayInfo("Enter Input.")
            return
        
        bad = False
        if (x[0] == '0' or y[0] == '0'):
            bad = True

        for ch in x:
            if (ch > '9' or ch < '0'):
                bad = True
                break
        for ch in y:
            if (ch > '9' or ch < '0'):
                bad = True
                break

        if bad:
            self.displayInfo("Input N or E must be positive integers and should not contain any leading zeros.")
            return

        n = int(x)
        e = int(y)
        if e < 3:
            self.displayInfo("E must be greater than 2")
            return

        self.outputText.setText(encryptText(s, n, e))

    
    def displayInfo(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Info")
        msg.setText(message)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()


    def retranslateUi(self, windowEncryption):
        _translate = QtCore.QCoreApplication.translate
        windowEncryption.setWindowTitle(_translate("windowEncryption", "Text Encryption"))
        self.labelN.setText(_translate("windowEncryption", "N :"))
        self.labelE.setText(_translate("windowEncryption", "E :"))
        self.buttonEncrypt.setText(_translate("windowEncryption", "Encrypt Text"))
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    windowEncryption = QtWidgets.QMainWindow()
    ui = Ui_windowEncryption()
    ui.setupUi(windowEncryption)
    windowEncryption.show()
    sys.exit(app.exec_())
