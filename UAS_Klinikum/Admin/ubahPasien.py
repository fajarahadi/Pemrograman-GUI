# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ubahPasien.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import pymysql

class Ui_Dialog3(object):

    def koneksi(self):
        con = pymysql.connect(db='db_klinikum',
                              user='root', passwd='', host='localhost',
                              port=3306, autocommit=True)
        cur = con.cursor()
        if (cur):
            self.messagebox("Koneksi", "Koneksi Berhasil")
        else:
            self.messagebox("Koneksi", "Koneksi Gagal")

    def messagebox(self, title, message):
            mess = QtWidgets.QMessageBox()
            mess.setWindowTitle(title)
            mess.setText(message)

            mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
            mess.exec_()

    def ubahfunction(self):
        namapasien  = self.lineNamapasien.text()
        tanggalPeriksa = self.datePeriksa.text()
        jamPeriksa = self.cbJamperiksa.currentText()
        keluhan = self.teksKeluhan.toPlainText()





    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 640)
        Dialog.setStyleSheet("background-color: rgb(209, 236, 206);\n"
"\n"
"")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 180, 121, 21))
        self.label.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.datePeriksa = QtWidgets.QDateEdit(Dialog)
        self.datePeriksa.setGeometry(QtCore.QRect(180, 180, 161, 31))
        self.datePeriksa.setCalendarPopup(True)
        self.datePeriksa.setDate(QtCore.QDate(2021, 7, 30))
        self.datePeriksa.setObjectName("datePeriksa")
        self.cbJamperiksa = QtWidgets.QComboBox(Dialog)
        self.cbJamperiksa.setGeometry(QtCore.QRect(180, 240, 141, 31))
        self.cbJamperiksa.setEditable(False)
        self.cbJamperiksa.setObjectName("cbJamperiksa")
        self.cbJamperiksa.addItem("")
        self.cbJamperiksa.addItem("")
        self.cbJamperiksa.addItem("")
        self.cbJamperiksa.addItem("")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 310, 61, 21))
        self.label_2.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 240, 121, 21))
        self.label_3.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_21 = QtWidgets.QLabel(Dialog)
        self.label_21.setGeometry(QtCore.QRect(40, 10, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(107, 107, 107);\n"
"")
        self.label_21.setObjectName("label_21")
        self.teksKeluhan = QtWidgets.QTextEdit(Dialog)
        self.teksKeluhan.setGeometry(QtCore.QRect(50, 340, 391, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.teksKeluhan.setFont(font)
        self.teksKeluhan.setObjectName("teksKeluhan")
        self.btnUbah = QtWidgets.QPushButton(Dialog)
        self.btnUbah.setGeometry(QtCore.QRect(160, 480, 121, 41))
        self.btnUbah.setStyleSheet("background-color: rgb(107, 107, 107);\n"
"font: 12pt \"MS Shell Dlg 2\"; color:rgb(255, 255, 255)")
        self.btnUbah.setObjectName("btnUbah")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 120, 121, 21))
        self.label_4.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.lineNamapasien = QtWidgets.QLineEdit(Dialog)
        self.lineNamapasien.setGeometry(QtCore.QRect(180, 120, 261, 31))
        self.lineNamapasien.setObjectName("lineNamapasien")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Tanggal Periksa"))
        self.cbJamperiksa.setItemText(0, _translate("Dialog", "09:00"))
        self.cbJamperiksa.setItemText(1, _translate("Dialog", "11:00"))
        self.cbJamperiksa.setItemText(2, _translate("Dialog", "13:00"))
        self.cbJamperiksa.setItemText(3, _translate("Dialog", "15:00"))
        self.label_2.setText(_translate("Dialog", "Keluhan"))
        self.label_3.setText(_translate("Dialog", "Jam Periksa"))
        self.label_21.setText(_translate("Dialog", "Ubah"))
        self.btnUbah.setText(_translate("Dialog", "Ubah"))
        self.label_4.setText(_translate("Dialog", "Nama Pasien"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog3()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

