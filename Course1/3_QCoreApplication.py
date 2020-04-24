import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Ico(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('学点编程吧出品')
        self.setWindowIcon(QIcon('2.jpg'))
        qbtn = QPushButton('退出', self)
        qbtn.clicked.connect(
            QCoreApplication.instance().quit)  # QCoreApplication包含主事件循环; 它处理和调度所有事件。 instance()方法给我们当前的实例。
        qbtn.resize(70, 30)
        qbtn.move(50, 50)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ico()
    sys.exit(app.exec_())
