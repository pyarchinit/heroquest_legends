# -*- coding: utf-8 -*-

"""
/***************************************************************************
        Heroquest's Legends Solo by Mandor the Druid
                             -------------------
    begin                : 2021-01-02
    copyright            : (C) 2021 by Luca Mandolesi
    email                : mandoluca at gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import locale
import sys
import os
from PyQt5 import QtWidgets, uic
from PyQt5.uic import loadUiType
#codeadded
import sys
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QFileDialog

#codeadde d/
from heroquest_solo_main import Heroquest_solo


class Ui(QtWidgets.QMainWindow):
    CONFIG = ""
    local_language = locale.getdefaultlocale()
    file_name = 'it_IT.txt'
    if local_language[0] == 'it_IT':
        CONFIG = open(file_name, "rb+")
    elif local_language[0] == 'en_EN':
        CONFIG = open('en_EN.txt', "rb+")
    data_config = CONFIG.read()
    CONFIG.close()
    CONFIG_DICT = eval(data_config)

    HQ_SOLO = ""

    CURRENT_ROUND = ''

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('C:\\Users\\Luca\\Programmazione\\heroquest_solo\\heroquest_legends.ui', self)
        self.acceptDrops()
        self.HQ_SOLO = Heroquest_solo(self.CONFIG_DICT)

        #add backgroundimage
        oImage = QImage("C:\\Users\\Luca\\Programmazione\\heroquest_solo\\images\mappa.bmp")
        sImage = oImage.scaled(QSize(1024, 768))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.label_image = QLabel(self)
        self.label_image.move(50,50)



        self.show()

    def on_pushButton_round_pressed(self):
        self.textEdit_aisles.setText("")
        self.textEdit_monsters.setText("")
        self.textEdit_room_description.setText("")
        self.textEdit_treasures_finder.setText("")
        self.textEdit_treasures_description.setText("")
        self.textEdit_traps.setText("")
        self.textEdit_secret_doors.setText("")

        current_turn = int(self.lineEdit_round.text())
        next_turn = current_turn+1
        self.lineEdit_round.setText(str(next_turn))

    def on_pushButton_aisles_pressed(self):
        current_turn = int(self.lineEdit_round.text())
        self.textEdit_aisles.setText("")


        if current_turn == 1 or current_turn == 2:
            msg_num = self.HQ_SOLO.random_numbers()
            while (msg_num) >= 21:
                msg_num = self.HQ_SOLO.random_numbers()  # return always door at first and second turn
            msg = self.HQ_SOLO.aisles(msg_num)
        else:
            msg = self.HQ_SOLO.aisles(self.HQ_SOLO.random_numbers())

        self.textEdit_aisles.setText("")
        self.textEdit_aisles.setText(str(msg))

    def on_pushButton_treasures_finds_pressed(self):
        msg = self.HQ_SOLO.treasures(self.HQ_SOLO.random_numbers())
        self.textEdit_treasures_finder.setText("")
        self.textEdit_treasures_finder.setText(str(msg))

    def on_pushButton_treasures_description_pressed(self):
        msg = self.HQ_SOLO.chest(self.HQ_SOLO.random_numbers())
        self.textEdit_treasures_description.setText("")
        self.textEdit_treasures_description.setText(str(msg))

    def on_pushButton_traps_and_secret_doors_finder_pressed(self):
        msg_traps = self.HQ_SOLO.traps(self.HQ_SOLO.random_numbers())
        msg_secret_door = self.HQ_SOLO.secret_doors(self.HQ_SOLO.random_numbers())
        self.textEdit_traps.setText(str(msg_traps))
        self.textEdit_secret_doors.setText(str(msg_secret_door))

    def on_pushButton_rooms_pressed(self):
        current_turn = int(self.lineEdit_round.text())
        msg_temp = self.HQ_SOLO.room_generator(self.lineEdit_room_dimension.text(), current_turn)

        if current_turn == 1 or current_turn == 2:
            msg_room = self.HQ_SOLO.CONFIG_DICT['aux_msg_1'].format(msg_temp[0])
            #print("mesg war 7")
        else:
            if msg_temp[0] == '':
                msg_room = self.HQ_SOLO.CONFIG_DICT['aux_msg_6']
            else:
                msg_room = msg_temp[0]


        self.textEdit_room_description.setText(str(msg_temp[1]))

        self.textEdit_monsters.setText(str(msg_room))
        #TODO test area to add images
        """
        #test area to add images
        #image = QFileDialog.getOpenFileName(None, 'OpenFile', '', "Image file(*.jpg)")
        #imagePath = image[0]
        #pixmap = QPixmap(imagePath)

        #if int(self.lineEdit_round.text()) == 1:
            pixmap = QPixmap('C:\\Users\\Luca\\Programmazione\\heroquest_solo\\images\\goblin.png')

            self.label_image.setPixmap(pixmap)
            self.label_image.setGeometry(500, 500, 500, 700)

            self.label_image.adjustSize()  # <---

            ## print(ocr.resimden_yaziya(imagePath))
            # print(imagePath)
        else:
            pixmap = QPixmap('C:\\Users\\Luca\\Programmazione\\heroquest_solo\\images\\fimir.png')

            self.label_image.setPixmap(pixmap)
            self.label_image.setGeometry(400, 400, 250, 250)

            self.label_image.adjustSize()  # <---
        """


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()


