# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIUTS.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from EditDataMHS import *

class Ui_Form(object):




    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(779, 694)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(310, 65, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(190, 490, 431, 111))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nimEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.nimEdit.setObjectName("nimEdit")
        self.verticalLayout.addWidget(self.nimEdit)
        self.namaEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.namaEdit.setObjectName("namaEdit")
        self.verticalLayout.addWidget(self.namaEdit)
        self.jurusanEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.jurusanEdit.setObjectName("jurusanEdit")
        self.verticalLayout.addWidget(self.jurusanEdit)
        self.notelpEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.notelpEdit.setObjectName("notelpEdit")
        self.verticalLayout.addWidget(self.notelpEdit)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(130, 490, 53, 111))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.layoutWidget1.setFont(font)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(230, 610, 395, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.layoutWidget2.setFont(font)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tambah = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tambah.setFont(font)
        self.tambah.setObjectName("tambah")
        self.tambah.clicked.connect(self.tambahData)
        self.horizontalLayout.addWidget(self.tambah)
        self.edit = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.edit.setFont(font)
        self.edit.setObjectName("edit")
        self.edit.clicked.connect(self.editData)
        self.horizontalLayout.addWidget(self.edit)
        self.clear = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.clear.clicked.connect(self.nimEdit.clear)
        self.clear.clicked.connect(self.namaEdit.clear)
        self.clear.clicked.connect(self.jurusanEdit.clear)
        self.clear.clicked.connect(self.notelpEdit.clear)
        self.horizontalLayout.addWidget(self.clear)
        self.hapus = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.hapus.setFont(font)
        self.hapus.setObjectName("hapus")
        self.hapus.clicked.connect(self.hapusData)
        self.horizontalLayout.addWidget(self.hapus)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(130, 140, 491, 341))
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def tambahData(self):
        self.listWidget.addItem(
            self.nimEdit.text() + ' , ' +
            self.namaEdit.text() + ' , ' +
            self.jurusanEdit.text() + ' , ' +
            self.notelpEdit.text())

    def editData(self):
        if self.listWidget.currentRow() < 0: return
        self.editDataMhs = EditDataMahasiswa ()
        q = str(self.listWidget.currentItem().text())
        idx = q.index(',')
        self.editDataMhs.nim.setText(q[:(idx - 1)])
        self.editDataMhs.nama.setText(q[(idx - 2):])
        self.editDataMhs.jurusan.setText(q[(idx - 3):])
        self.editDataMhs.telp.setText(q[(idx - 4):])

        if self.editDataMhs.exec_() == QDialog.Accepted:
            self.listWidget.currentItem().setText(
                self.editDataMhs.nim.text() + ' , ' +
                self.editDataMhs.nama.text() + ' , ' +
                self.editDataMhs.jurusan.text() + ' , ' +
                self.editDataMhs.telp.text())

    def hapusData(self):
        row = self.listWidget.currentRow()
        if row >= 0:
            self.listWidget.takeItem(row)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Data Mahasiswa"))
        self.label_2.setText(_translate("Form", "NIM"))
        self.label_3.setText(_translate("Form", "Nama"))
        self.label_4.setText(_translate("Form", "Jurusan"))
        self.label_5.setText(_translate("Form", "No.Telp"))
        self.tambah.setText(_translate("Form", "TAMBAH"))
        self.edit.setText(_translate("Form", "EDIT"))
        self.clear.setText(_translate("Form", "CLEAR"))
        self.hapus.setText(_translate("Form", "HAPUS"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

