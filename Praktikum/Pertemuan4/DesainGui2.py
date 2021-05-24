# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DesainGui2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(827, 479)
        self.namaEdit = QtWidgets.QLineEdit(Form)
        self.namaEdit.setGeometry(QtCore.QRect(220, 120, 371, 21))
        self.namaEdit.setObjectName("namaEdit")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(220, 180, 371, 65))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.hallo = QtWidgets.QPushButton(self.widget)
        self.hallo.setObjectName("hallo")
        self.gridLayout.addWidget(self.hallo, 0, 0, 1, 1)
        self.clear = QtWidgets.QPushButton(self.widget)
        self.clear.setObjectName("clear")
        self.clear.clicked.connect(self.namaEdit.clear)
        self.gridLayout.addWidget(self.clear, 0, 1, 1, 1)
        self.keluar = QtWidgets.QPushButton(self.widget)
        self.keluar.setObjectName("keluar")
        self.keluar.clicked.connect(Form.close)
        self.gridLayout.addWidget(self.keluar, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(310, 80, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.hallo.setText(_translate("Form", "Hallo"))
        self.clear.setText(_translate("Form", "Clear"))
        self.keluar.setText(_translate("Form", "Keluar"))
        self.label.setText(_translate("Form", "Masukan Nama Anda"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

