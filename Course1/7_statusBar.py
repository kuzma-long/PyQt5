import sys

from PyQt5.QtWidgets import QApplication, QMainWindow  # QMainWindow类提供了一个主应用程序窗口。 这使得能够创建具有状态栏，工具栏和菜单栏的经典应用程序框架。


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.statusBar().showMessage('准备就绪')
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('关注微信公众号：学点编程吧--状态栏')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
