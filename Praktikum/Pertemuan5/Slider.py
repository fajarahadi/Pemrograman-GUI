

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        self.resize(400, 100)
        self.move(300, 300)
        self.setWindowTitle('Slider dan LCDNumber')
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(-1)
        self.slider.setMaximum(201)
        self.slider.setValue(21)
        self.lcd = QLCDNumber()
        self.lcd.setDigitCount(3)
        self.lcd.display(21)
        layout = QVBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(self.lcd)
        self.setLayout(layout)
        self.slider.sliderMoved.connect(self.sliderMoved)
    def sliderMoved(self):
        self.lcd.display(str(self.slider.value()))
if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()