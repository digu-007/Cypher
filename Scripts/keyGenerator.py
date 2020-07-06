# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'key_generator.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from keyGeneration import keyGeneration

class Ui_windowKeyGenerator(object):
    
    def retrievePrimes(self):
        p = int(self.inputP.toPlainText())
        q = int(self.inputQ.toPlainText())
        n, e, d = keyGeneration(p, q)
        self.outputN.setText(str(n))
        self.outputE.setText(str(e))
        self.outputD.setText(str(d))

    def setupUi(self, windowKeyGenerator):
        windowKeyGenerator.setObjectName("windowKeyGenerator")
        windowKeyGenerator.resize(800, 602)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        windowKeyGenerator.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(windowKeyGenerator)
        self.centralwidget.setObjectName("centralwidget")
        self.labelEnterPrime = QtWidgets.QLabel(self.centralwidget)
        self.labelEnterPrime.setGeometry(QtCore.QRect(30, 90, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelEnterPrime.setFont(font)
        self.labelEnterPrime.setObjectName("labelEnterPrime")
        self.labelP = QtWidgets.QLabel(self.centralwidget)
        self.labelP.setGeometry(QtCore.QRect(320, 90, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelP.setFont(font)
        self.labelP.setObjectName("labelP")
        self.labelQ = QtWidgets.QLabel(self.centralwidget)
        self.labelQ.setGeometry(QtCore.QRect(550, 90, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelQ.setFont(font)
        self.labelQ.setObjectName("labelQ")
        self.buttonCustom = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCustom.setGeometry(QtCore.QRect(40, 220, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.buttonCustom.setFont(font)
        self.buttonCustom.setObjectName("buttonCustom")
        self.buttonCustom.clicked.connect(self.retrievePrimes)
        self.buttonDefault = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDefault.setGeometry(QtCore.QRect(450, 220, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.buttonDefault.setFont(font)
        self.buttonDefault.setObjectName("buttonDefault")
        self.labelOR = QtWidgets.QLabel(self.centralwidget)
        self.labelOR.setGeometry(QtCore.QRect(390, 220, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelOR.setFont(font)
        self.labelOR.setObjectName("labelOR")
        self.labelN = QtWidgets.QLabel(self.centralwidget)
        self.labelN.setGeometry(QtCore.QRect(180, 360, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelN.setFont(font)
        self.labelN.setObjectName("labelN")
        self.labelE = QtWidgets.QLabel(self.centralwidget)
        self.labelE.setGeometry(QtCore.QRect(300, 420, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelE.setFont(font)
        self.labelE.setObjectName("labelE")
        self.labelD = QtWidgets.QLabel(self.centralwidget)
        self.labelD.setGeometry(QtCore.QRect(300, 480, 31, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelD.setFont(font)
        self.labelD.setObjectName("labelD")
        self.inputP = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputP.setGeometry(QtCore.QRect(350, 90, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.inputP.setFont(font)
        self.inputP.setObjectName("inputP")
        self.inputQ = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputQ.setGeometry(QtCore.QRect(580, 90, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.inputQ.setFont(font)
        self.inputQ.setObjectName("inputQ")
        self.outputN = QtWidgets.QTextEdit(self.centralwidget)
        self.outputN.setGeometry(QtCore.QRect(210, 360, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.outputN.setFont(font)
        self.outputN.setObjectName("outputN")
        self.outputE = QtWidgets.QTextEdit(self.centralwidget)
        self.outputE.setGeometry(QtCore.QRect(330, 420, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.outputE.setFont(font)
        self.outputE.setObjectName("outputE")
        self.outputD = QtWidgets.QTextEdit(self.centralwidget)
        self.outputD.setGeometry(QtCore.QRect(330, 480, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.outputD.setFont(font)
        self.outputD.setObjectName("outputD")
        windowKeyGenerator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(windowKeyGenerator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        windowKeyGenerator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(windowKeyGenerator)
        self.statusbar.setObjectName("statusbar")
        windowKeyGenerator.setStatusBar(self.statusbar)

        self.retranslateUi(windowKeyGenerator)
        QtCore.QMetaObject.connectSlotsByName(windowKeyGenerator)

    def retranslateUi(self, windowKeyGenerator):
        _translate = QtCore.QCoreApplication.translate
        windowKeyGenerator.setWindowTitle(_translate("windowKeyGenerator", "Key Generator"))
        self.labelEnterPrime.setText(_translate("windowKeyGenerator", "Enter two prime numbers"))
        self.labelP.setText(_translate("windowKeyGenerator", "P :"))
        self.labelQ.setText(_translate("windowKeyGenerator", "Q :"))
        self.buttonCustom.setText(_translate("windowKeyGenerator", "Generate using primes"))
        self.buttonDefault.setText(_translate("windowKeyGenerator", "Generate 132 bit safe key"))
        self.labelOR.setText(_translate("windowKeyGenerator", "OR"))
        self.labelN.setText(_translate("windowKeyGenerator", "N :"))
        self.labelE.setText(_translate("windowKeyGenerator", "E :"))
        self.labelD.setText(_translate("windowKeyGenerator", "D :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    windowKeyGenerator = QtWidgets.QMainWindow()
    ui = Ui_windowKeyGenerator()
    ui.setupUi(windowKeyGenerator)
    windowKeyGenerator.show()
    sys.exit(app.exec_())
