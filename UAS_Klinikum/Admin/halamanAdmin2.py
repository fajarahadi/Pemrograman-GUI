# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'halamanAdmin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from tambahPasien import Ui_Dialog
from ubahPasien import Ui_Dialog3

class Ui_Dialog2(object):

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

    def loadData(self):
        con = pymysql.connect(db='db_klinikum',
                              user='root', passwd='', host='localhost',
                              port=3306, autocommit=True)
        cur = con.cursor()
        result ="SELECT noAntrian, namaPas, tanggalPeriksa, jamPeriksa, keluhan From periksa WHERE noAntrian >32"
        data = cur.execute(result)
        hasil = cur.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(hasil):
            # print(row_data)
            self.tableWidget.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))




    #def ubahData(self):


    def hapusData(self):

        row = self.tableWidget.currentIndex().row()
        column = self.tableWidget.currentIndex().column()
        print(row, column)




    def carifunction(self):
        cari = self.lineCari.text()
        filter = self.comboFilter.currentText()

        con = pymysql.connect(db='db_klinikum',
                              user='root', passwd='', host='localhost',
                              port=3306, autocommit=True)
        cur = con.cursor()

        if (filter == 'Nama Pasien'):
            query = "SELECT noAntrian, namaPas, tanggalPeriksa, jamPeriksa, keluhan FROM periksa WHERE namaPas=%s"
            data = cur.execute(query,(cari))
            hasil = cur.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(hasil):
                # print(row_data)
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        else:
            query = "SELECT noAntrian, namaPas, tanggalPeriksa, jamPeriksa, keluhan FROM periksa WHERE tanggalPeriksa=%s"
            data = cur.execute(query, (cari))
            hasil = cur.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(hasil):
                # print(row_data)
                self.tableWidget.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


    def openTambahPasien(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()

    def openUbahPasien(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog3()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(721, 549)
        Dialog.setStyleSheet("background-color: rgb(209, 236, 206);\n"
"\n"
"")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(107, 107, 107);\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 120, 52, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboFilter = QtWidgets.QComboBox(Dialog)
        self.comboFilter.setGeometry(QtCore.QRect(110, 120, 151, 31))
        self.comboFilter.setStyleSheet("background-color: rgb(107, 107, 107);\n"
"font: 12pt \"MS Shell Dlg 2\"; color:rgb(255, 255, 255)")
        self.comboFilter.setObjectName("comboFilter")
        self.comboFilter.addItem("")
        self.comboFilter.addItem("")
        self.lineCari = QtWidgets.QLineEdit(Dialog)
        self.lineCari.setGeometry(QtCore.QRect(330, 120, 241, 31))
        self.lineCari.setObjectName("lineCari")
        self.buttonCari = QtWidgets.QPushButton(Dialog)
        self.buttonCari.setGeometry(QtCore.QRect(610, 120, 51, 31))
        self.buttonCari.setStyleSheet("background-color: rgb(107, 107, 107);\n"
"font: 12pt \"MS Shell Dlg 2\"; color:rgb(255, 255, 255)")
        self.buttonCari.setObjectName("buttonCari")

        self.buttonCari.clicked.connect(self.carifunction)

        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(50, 200, 621, 192))
        self.tableWidget.setStyleSheet("background-color: rgb(107, 107, 107);\n"
"font: 10pt \"MS Shell Dlg 2\"; color:rgb(0, 0, 0)")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(270, 450, 395, 35))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonRefresh = QtWidgets.QPushButton(self.layoutWidget)
        self.buttonRefresh.setStyleSheet("background-color: rgb(107, 107, 107);\n"
"font: 12pt \"MS Shell Dlg 2\"; color:rgb(255, 255, 255)")
        self.buttonRefresh.setObjectName("buttonRefresh")
        self.horizontalLayout.addWidget(self.buttonRefresh)

        self.buttonRefresh.clicked.connect(self.loadData)


        self.buttonTambah = QtWidgets.QPushButton(self.layoutWidget)
        self.buttonTambah.setStyleSheet("background-color: rgb(107, 107, 107);\n"
"font: 12pt \"MS Shell Dlg 2\"; color:rgb(255, 255, 255)")
        self.buttonTambah.setObjectName("buttonTambah")
        self.horizontalLayout.addWidget(self.buttonTambah)

        self.buttonTambah.clicked.connect(self.openTambahPasien)

        self.buttonUbah = QtWidgets.QPushButton(self.layoutWidget)
        self.buttonUbah.setStyleSheet("background-color: rgb(107, 107, 107);\n"
"font: 12pt \"MS Shell Dlg 2\"; color:rgb(255, 255, 255)")
        self.buttonUbah.setObjectName("buttonUbah")
        self.horizontalLayout.addWidget(self.buttonUbah)

        self.buttonUbah.clicked.connect(self.openUbahPasien)

        self.buttonHapus = QtWidgets.QPushButton(self.layoutWidget)
        self.buttonHapus.setStyleSheet("background-color: rgb(107, 107, 107);\n"
"font: 12pt \"MS Shell Dlg 2\"; color:rgb(255, 255, 255)")
        self.buttonHapus.setObjectName("buttonHapus")
        self.horizontalLayout.addWidget(self.buttonHapus)

        self.buttonHapus.clicked.connect(self.hapusData)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Data Pasien"))
        self.label_2.setText(_translate("Dialog", "Filter:"))
        self.comboFilter.setItemText(0, _translate("Dialog", "Nama Pasien"))
        self.comboFilter.setItemText(1, _translate("Dialog", "Tanggal Periksa"))
        self.buttonCari.setText(_translate("Dialog", "Cari"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "No. Antrian"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Nama Pasien"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Tanggal Periksa"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Jam Periksa"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Keluhan"))
        self.buttonRefresh.setText(_translate("Dialog", "Refresh"))
        self.buttonTambah.setText(_translate("Dialog", "Tambah"))
        self.buttonUbah.setText(_translate("Dialog", "Ubah"))
        self.buttonHapus.setText(_translate("Dialog", "Hapus"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

