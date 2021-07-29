# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginAdmin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from halamanAdmin2 import Ui_Dialog2
import pymysql

class Ui_Dialog(object):

    def koneksi (self):
        con = pymysql.connect(db='db_klinikum',
        user='root', passwd='', host='localhost',
        port=3306, autocommit=True)
        cur = con.cursor()
        if(cur):
                self.messagebox ("Koneksi", "Koneksi Berhasil")
        else:
                self.messagebox ("Koneksi", "Koneksi Gagal")

    def messagebox (self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)

        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def loginAdminfunction(self):
        username = self.usernameA.text()
        password = self.passwordA.text()
        con = pymysql.connect(db='db_klinikum',
                              user='root', passwd='', host='localhost',
                              port=3306, autocommit=True)
        cur = con.cursor()
        query = "SELECT * From admin where usernameAdmin=%s AND passwordAdmin=%s"
        data = cur.execute(query, (username, password))
        if (len(cur.fetchall()) > 0):
            self.messagebox("Berhasil", "Anda Berhasil Login")
            self.openHalamanAdmin()
        else:
            self.messagebox("Gagal", "Username atau Password anda salah")
            self.usernameA.clear()
            self.passwordA.clear()
            return




    def openHalamanAdmin(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()



    def setupUi(self, Dialog):
        self.koneksi()
        Dialog.setObjectName("Dialog")
        Dialog.resize(536, 490)
        Dialog.setStyleSheet("background-color: rgb(209, 236, 206);")
        self.passwordA = QtWidgets.QLineEdit(Dialog)
        self.passwordA.setGeometry(QtCore.QRect(60, 290, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passwordA.setFont(font)
        self.passwordA.setText("")
        self.passwordA.setObjectName("passwordA")
        self.passwordA.setEchoMode(QtWidgets.QLineEdit.Password)
        self.usernameA = QtWidgets.QLineEdit(Dialog)
        self.usernameA.setGeometry(QtCore.QRect(60, 200, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.usernameA.setFont(font)
        self.usernameA.setObjectName("usernameA")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 260, 81, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 20, 351, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.loginButtonA = QtWidgets.QPushButton(Dialog)
        self.loginButtonA.setGeometry(QtCore.QRect(190, 390, 121, 41))
        self.loginButtonA.setStyleSheet("background-color: rgb(107, 107, 107);\n"
"font: 12pt \"MS Shell Dlg 2\"; color:rgb(255, 255, 255)")
        self.loginButtonA.setObjectName("loginButtonA")

        self.loginButtonA.clicked.connect(self.loginAdminfunction)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 170, 81, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(150, 70, 221, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.label_2.setText(_translate("Dialog", "Selamat Datang di Klinik"))
        self.loginButtonA.setText(_translate("Dialog", "Login"))
        self.label.setText(_translate("Dialog", "Username"))
        self.label_5.setText(_translate("Dialog", "Bunda Bahagia"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

