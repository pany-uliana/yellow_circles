import sys

from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.should_paint_circle = False
        self.Button.clicked.connect(self.run)

    def run(self):
        self.should_paint_circle = True
        self.update()

    def paintEvent(self, event):
        if self.should_paint_circle:
            self.size = random.uniform(1, 100)
            painter = QPainter(self)
            painter.setPen(QPen(Qt.yellow, 8, Qt.SolidLine))
            painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
            painter.drawEllipse(random.uniform(1, 500), random.uniform(1, 500),
                                self.size, self.size)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
