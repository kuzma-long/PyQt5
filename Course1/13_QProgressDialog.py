import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QProgressDialog)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 150)
        self.setWindowTitle("微信公众号：学点编程吧--进度对话框")
        self.lb = QLabel("文件数量", self)
        self.lb.move(20, 40)
        self.bt1 = QPushButton('开始', self)
        self.bt1.move(20, 80)
        self.edit = QLineEdit('100000', self)
        self.edit.move(100, 40)
        self.show()
        self.bt1.clicked.connect(self.showDialog)

    def showDialog(self):
        num = int(self.edit.text())
        progress = QProgressDialog(self)
        progress.setWindowTitle("请稍等")
        progress.setLabelText("正在操作...")
        progress.setCancelButtonText("取消")
        progress.setMinimumDuration(5)  # 此属性保留对话框出现之前必须通过的时间。默认值为4000毫秒,即4秒。
        progress.setWindowModality(Qt.WindowModal)  # 阻塞同一应用程序中其它可视窗口的输入的对话框，用户必须完成这个对话框中的交互操作并且关闭了它之后才能访问应用程序中的其它窗口。
        progress.setRange(0, num)
        for i in range(num):
            progress.setValue(i)    # 该属性持有当前的进度
            if progress.wasCanceled():
                QMessageBox.warning(self, "提示", "操作失败")
                break
        else:
            progress.setValue(num)
            QMessageBox.information(self, "提示", "操作成功")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
