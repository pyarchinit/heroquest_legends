from random import randint
from sys import exit as sysExit

from PIL import Image

from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLabel


# Okay I was not sure what this was or why but it did not
# seem to me to be part of adding a human to the form and
# since I could not use it anyway I removed it to here
img = Image.open('C:\\Users\\Luca\\Programmazione\\heroquest_solo\\images\mappa.png')
img.resize((20, 20), Image.ANTIALIAS)


class HumanLabel(QLabel):
    def __init__(self, parent):
        QLabel.__init__(self, parent)

        self.HumanLocale = parent

    @property
    def HumanLocale(self):
        # On what Form is the Human located
        return self.__parent

    @HumanLocale.setter
    def HumanLocale(self, value):
        self.__parent = value

    @property
    def xCor(self):
        # Human's current X-Coordinate
        return self.__xCoordinate

    @xCor.setter
    def xCor(self, value):
        self.__xCoordinate = value

    @property
    def yCor(self):
        # Human's current Y-Coordinate
        return self.__yCoordinate

    @yCor.setter
    def yCor(self, value):
        self.__yCoordinate = value

    @property
    def HumanImage(self):
        # Human's current Image
        return self.__HumanImage

    @HumanImage.setter
    def HumanImage(self, value):
        self.__HumanImage.setPixmap(QPixmap(value))

    def placeHuman(self):
        self.move(self.xCor, self.yCor)
        # I do not have access to your Image so did this instead
        value = str(self.xCor) + '-' + str(self.yCor)
        self.setText(value)
        self.Humans[humanId].HumanImage = 'C:\\Users\\Luca\\Programmazione\\heroquest_solo\\images\mappa.png'
        self.show()

    def addHumanRandomly(self):
        # Note because you do not currently check to see if
        # the current humanId is not already in your list
        # you may end up just moving them instead of creating
        # them as such I would suggest such a check here and
        # creating another method called moveHuman
        self.xCor = randint(1, 450)
        self.yCor = randint(1, 350)
        self.placeHuman()


class MyMainWindow(QWidget):
    def __init__(self):
        super(MyMainWindow, self).__init__()

        self.Humans = {}

        self.setupUi()

        humanId = randint(1, 10000)
        self.Humans[humanId] = HumanLabel(self)
        self.Humans[humanId].addHumanRandomly()

    def setupUi(self):
        self.setWindowTitle('Form')
        self.resize(500, 375)

        humanId = 1
        self.Humans[humanId] = HumanLabel(self)
        self.Humans[humanId].xCor = 0
        self.Humans[humanId].yCor = 0
        self.Humans[humanId].HumanImage = 'C:\\Users\\Luca\\Programmazione\\heroquest_solo\\images\mappa.png'
        self.Humans[humanId].placeHuman()

    def mouseDoubleClickEvent(self, event):
        humanId = randint(1, 10000)
        # Create the object within the Dictionary
        self.Humans[humanId] = HumanLabel(self)
        # Then using that object stored in our Dictionary
        # we set its coordinates and show it
        self.Humans[humanId].addHumanRandomly()


if __name__ == '__main__':
    MainThred = QApplication([])

    MainGui = MyMainWindow()
    MainGui.show()

    sysExit(MainThred.exec_())