# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        # Central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Title label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 20, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        # Labels for sections
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 120, 80, 20))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 220, 80, 20))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(440, 120, 100, 20))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(460, 220, 100, 20))
        self.label_5.setObjectName("label_5")

        # Text fields
        self.txtvanban = QtWidgets.QTextEdit(self.centralwidget)
        self.txtvanban.setGeometry(QtCore.QRect(190, 110, 160, 80))
        self.txtvanban.setObjectName("txtvanban")

        self.txtmahoa = QtWidgets.QTextEdit(self.centralwidget)
        self.txtmahoa.setGeometry(QtCore.QRect(190, 210, 160, 80))
        self.txtmahoa.setObjectName("txtmahoa")

        self.txtthongtin = QtWidgets.QTextEdit(self.centralwidget)
        self.txtthongtin.setGeometry(QtCore.QRect(550, 110, 160, 80))
        self.txtthongtin.setObjectName("txtthongtin")

        self.txtsign = QtWidgets.QTextEdit(self.centralwidget)
        self.txtsign.setGeometry(QtCore.QRect(550, 210, 160, 80))
        self.txtsign.setObjectName("txtsign")

        # Buttons
        self.btngenerate = QtWidgets.QPushButton(self.centralwidget)
        self.btngenerate.setGeometry(QtCore.QRect(350, 70, 120, 30))
        self.btngenerate.setObjectName("btngenerate")

        self.btnencrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnencrypt.setGeometry(QtCore.QRect(130, 320, 100, 30))
        self.btnencrypt.setObjectName("btnencrypt")

        self.btndecrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btndecrypt.setGeometry(QtCore.QRect(260, 320, 100, 30))
        self.btndecrypt.setObjectName("btndecrypt")

        self.btnsign = QtWidgets.QPushButton(self.centralwidget)
        self.btnsign.setGeometry(QtCore.QRect(450, 320, 100, 30))
        self.btnsign.setObjectName("btnsign")

        self.btnverify = QtWidgets.QPushButton(self.centralwidget)
        self.btnverify.setGeometry(QtCore.QRect(580, 320, 100, 30))
        self.btnverify.setObjectName("btnverify")

        MainWindow.setCentralWidget(self.centralwidget)

        # Menu bar & status bar (default)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Set text content
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RSA Cipher"))
        self.label.setText(_translate("MainWindow", "RSA CIPHER"))
        self.label_2.setText(_translate("MainWindow", "Plaintext"))
        self.label_3.setText(_translate("MainWindow", "CipherText"))
        self.label_4.setText(_translate("MainWindow", "Information"))
        self.label_5.setText(_translate("MainWindow", "Signature"))
        self.btngenerate.setText(_translate("MainWindow", "Generate Keys"))
        self.btnencrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btndecrypt.setText(_translate("MainWindow", "Decrypt"))
        self.btnsign.setText(_translate("MainWindow", "Sign"))
        self.btnverify.setText(_translate("MainWindow", "Verify"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
