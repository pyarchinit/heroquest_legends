import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFileDialog, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot


# import TurkceOcr as ocr

class App(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Resimden Texte'
        self.left = 50
        self.top = 50
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create widget

        button = QPushButton('Resim Yükle', self)
        button.setToolTip('This is load picture button')
        button.move(10, 10)
        button.clicked.connect(self.on_click)

        self.label = QLabel(self)
        self.label.move(10, 50)

        # self.resize(pixmap.width(), pixmap.height())

        self.show()

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
        image = QFileDialog.getOpenFileName(None, 'OpenFile', '', "Image file(*.jpg)")
        imagePath = image[0]
        #pixmap = QPixmap(imagePath)
        pixmap = QPixmap('C:\\Users\\Luca\\Programmazione\\heroquest_solo\\images\\goblin.png')
        self.label.setPixmap(pixmap)

        self.label.adjustSize()  # <---

        # print(ocr.resimden_yaziya(imagePath))
        print(imagePath)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())