import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from halamanUser import Ui_Dialog1
import pymysql


class Login(QDialog):

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


    def __init__(self):
        self.koneksi()
        super(Login, self).__init__()
        loadUi('loginUser.ui', self)
        self.loginButton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createButton.clicked.connect(self.gotosignup)


    def loginfunction(self):
        username = self.username.text()
        password = self.password.text()
        con = pymysql.connect(db='db_klinikum',
                             user='root', passwd='', host='localhost',
                             port=3306, autocommit=True)
        cur = con.cursor()
        query = "SELECT * From pasien where usernamePasien=%s AND passwordPasien=%s"
        data = cur.execute(query, (username, password))
        if (len(cur.fetchall()) > 0):

            self.messagebox("Berhasil", "Anda Berhasil Login")
            self.openHalamanUser()
        else:
            self.messagebox("Gagal", "Username atau Password anda salah")
            self.username.clear()
            self.password.clear()
            return



    def gotosignup(self):
        signup = Signup()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex()+1)


    def openHalamanUser(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog1()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()


class Signup(QDialog):
    def __init__(self):
        super(Signup, self).__init__()
        loadUi('signupUser.ui', self)
        self.signupButton.clicked.connect(self.signupfunction)
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Password)

    def signupfunction(self):
        Nik        = self.lineEdit.text()
        nama       = self.lineEdit_2.text()
        if self.radioButton.isChecked():
            jenisK = 'Laki-laki'
        else:
            jenisK = 'Perempuan'
        ttl        = self.lineEdit_3.text()
        noTelp     = self.lineEdit_4.text()
        alamat     = self.lineEdit_5.text()
        username   = self.lineEdit_6.text()
        password   = self.lineEdit_7.text()

        insert = (Nik, nama, jenisK, ttl, noTelp, alamat, username, password)
        print(insert)
        if self.lineEdit.text() and self.lineEdit_2.text() and self.radioButton.isChecked and self.lineEdit_3.text() and self.lineEdit_4.text() and self.lineEdit_5.text() and self.lineEdit_6.text() and self.lineEdit_7.text():
            con = pymysql.connect(db='db_klinikum',
                                  user='root', passwd='', host='localhost',
                                  port=3306, autocommit=True)
            cur = con.cursor()
            query = "INSERT INTO pasien (nik, namaPasien, jenisKelamin, TTL, noTelp, alamat, usernamePasien, passwordPasien)" + "VALUES" + str(insert)
            data = cur.execute(query)
            login = Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            QMessageBox.information(self, "Berhasil", "Akun anda berhasil dibuat, silahkan login")

        else:
            QMessageBox.information(self, "Gagal", "Silahkan di cek kembali")
            return

        #self.openHalamanUser()

    def openHalamanUser(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog1()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()




app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(585)
widget.setFixedHeight(780)
widget.show()
app.exec_()