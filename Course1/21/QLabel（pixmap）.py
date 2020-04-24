# coding=utf-8

import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(550, 500)
        self.setWindowTitle('关注微信公众号：学点编程吧--标签:图画（QLabel）')

        pix = QPixmap('sexy.jpg')

        lb1 = QLabel(self)
        lb1.setGeometry(0, 0, 300, 200)
        lb1.setStyleSheet("border: 2px solid red")
        lb1.setPixmap(pix)

        lb2 = QLabel(self)
        lb2.setGeometry(0, 250, 300, 200)
        lb2.setPixmap(pix)
        lb2.setStyleSheet("border: 2px solid red")
        lb2.setScaledContents(True) # 是否将缩放其内容以填充所有可用空间。当启用时，标签显示一个像素图，它将缩放像素图以填充可用空间。该属性的默认值是False。

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
