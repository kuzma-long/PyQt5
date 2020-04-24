import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QDial,QSlider, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        lcd = QLCDNumber(self)
        lcd2=QLCDNumber(self)
        dial = QDial(self)
        slider=QSlider(self)
        self.setGeometry(300, 300, 700, 250)
        self.setWindowTitle('学点编程吧')
        lcd.setGeometry(100, 50, 150, 60)
        lcd2.setGeometry(400,50,150,60)
        dial.setGeometry(120, 120, 100, 100)
        slider.setGeometry(420,120,100,100)
        dial.valueChanged.connect(lcd.display)
        slider.valueChanged.connect(lcd2.display)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
