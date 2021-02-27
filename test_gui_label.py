import sys

from PyQt5 import QtGui

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton

from PyQt5.QtGui import QPixmap

import random


class Label(QLabel):

    def __init__(self):
        super(Label, self).__init__()

        self.letters = ['q','w','e','r','t','y']

        self.h_layout = QHBoxLayout()
        self.setLayout(self.h_layout)

        self.label = QLabel('Random letters: _')

        self.pic = QtGui.QPixmap()
        self.pic.setPixmap(QtGui.QPixmap('C:\\Users\\Luca\\Programmazione\\heroquest_solo\\images\\Fimir.png'))

        self.btn = QPushButton("Roll")
        self.btn.clicked.connect(self.change_label)

        self.h_layout.addWidget(self.label)

        self.h_layout.addWidget(self.btn)
        self.h_layout.addWidget(self.pic)

    def change_label(self):
        if len(self.letters)>0:
            self.label.setText(self.letters.pop(0))

if __name__=="__main__":
    app = QApplication(sys.argv)
    main_label = Label()
    main_label.show()
    sys.exit(app.exec_())