import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(400, 300)
    w.move(300, 300)
    w.setWindowTitle('学点编程吧出品')
    w.show()
    sys.exit(app.exec_())
