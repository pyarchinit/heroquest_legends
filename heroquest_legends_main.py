# -*- coding: utf-8 -*-

"""
/***************************************************************************
        Heroquest's Legends Solo by Mandor the Druid
                             -------------------
    begin                : 2021-01-02
    copyright            : (C) 2021 by Luca Mandolesi
    email                : mandoluca at gmail.com
    version              : 0.6 BETA
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
import sys, os
import random

from PyQt5 import QtWidgets, uic

#codeadded
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush

#codeadde d/
from heroquest_solo_function import Heroquest_solo


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
        self.acceptDrops()
        uic.loadUi(os.path.join(os.path.dirname(__file__),'heroquest_legends.ui'), self)

        self.HQ_SOLO = Heroquest_solo(self.CONFIG_DICT)

        #add backgroundimage
        #dir_path = os.path.dirname(__file__)

        bg_img_path = './mappa.png'#os.path.join(os.path.dirname(__file__),'mappa.png')
        print(bg_img_path)

        oImage = QImage(bg_img_path)
        sImage = oImage.scaled(QSize(800, 768))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.charge_list()

        #self.label_image = QLabel(self)
        #self.label_image.move(50,50)

        self.show()

    def charge_list(self):

        monsters_category = ['goblin',
                             'orc',
                             'fimir',
                             'skeletor',
                             'zombie',
                             'mummie',
                             'chaos_warrior',
                             'gargoyle'
                             ]
        self.comboBox_monster_attack.clear()
        self.comboBox_monster_attack.addItems(monsters_category)

    def on_pushButton_the_mission_pressed(self):
        print('gg0g')
        rng_base = random.SystemRandom()
        mission_number_rand = rng_base.randint(1, 2)

        the_mission_dict = self.CONFIG_DICT['missions_dict']

        rng_base = random.SystemRandom()
        wanderer_monster_number_rand = rng_base.randint(1, 7)
        wanderer_monster = self.CONFIG_DICT['monsters_dict'][wanderer_monster_number_rand]
        wanderer_monster_text = self.CONFIG_DICT['monsters_msg_3']
        the_mission_text = '{}\n{}{}'.format(the_mission_dict[mission_number_rand],wanderer_monster_text,wanderer_monster)
        self.textEdit_the_mission.setText(the_mission_text)

    def on_pushButton_round_pressed(self):
        self.textEdit_aisles.setText("")
        self.textEdit_monsters.setText("")
        self.textEdit_room_description.setText("")
        self.textEdit_treasures_finder.setText("")
        self.textEdit_treasures_description.setText("")
        self.textEdit_traps.setText("")
        self.textEdit_secret_doors.setText("")
        self.textEdit_treasure_cards_description.setText("")

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

    def on_pushButton_treasure_card_pressed(self):
        msg = self.HQ_SOLO.treasure_card(self.HQ_SOLO.random_numbers())
        self.textEdit_treasure_cards_description.setText("")
        self.textEdit_treasure_cards_description.setText(str(msg))

    def on_pushButton_treasures_random_pressed(self):
        msg = self.HQ_SOLO.treasure_random(self.HQ_SOLO.random_numbers())

        self.textEdit_treasures_description.setText("")
        self.textEdit_treasures_description.setText(str(msg))

    def on_pushButton_traps_and_secret_doors_finder_pressed(self):
        msg_traps = self.HQ_SOLO.traps(self.HQ_SOLO.random_numbers())
        msg_secret_door = self.HQ_SOLO.secret_doors(self.HQ_SOLO.random_numbers())
        self.textEdit_traps.setText(str(msg_traps))
        self.textEdit_secret_doors.setText(str(msg_secret_door))

    def on_pushButton_rooms_pressed(self):
        self.textEdit_room_description.setText('')
        self.textEdit_monsters.setText('')

        if self.radioButton_not_explored.isChecked() == True:
            room_explored = 0
        else:
            room_explored = 1

        current_turn = int(self.lineEdit_round.text())
        msg_temp = self.HQ_SOLO.room_generator(self.lineEdit_room_dimension.text(), current_turn,room_explored)
        print(str(msg_temp))
        if current_turn == 1 or current_turn == 2:
            msg_room = self.HQ_SOLO.CONFIG_DICT['aux_msg_1'].format(msg_temp[0])
        else:
            if msg_temp[2] != '':
                msg_room = msg_temp[2]
            elif msg_temp[0] == '' and  msg_temp[2] == '' and room_explored == 1 :
                msg_room = self.HQ_SOLO.CONFIG_DICT['aux_msg_7']
            elif msg_temp[0] == '' and  msg_temp[2] == '' and room_explored == 0 :
                msg_room = self.HQ_SOLO.CONFIG_DICT['aux_msg_6']
            else:
                msg_room = msg_temp[0]

        self.textEdit_room_description.setText(str(msg_room))

        self.textEdit_monsters.setText(str(msg_temp[1]))


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

    def on_pushButton_monster_attack_pressed(self):
        self.textEdit_combat_text.setText("")
        monster_category = self.comboBox_monster_attack.currentText()

        mode_result = self.HQ_SOLO.fighting_system(monster_category) #1 attack - 0 escape

        if mode_result == 1:
            msg_attack = self.CONFIG_DICT['attack_messages'][1]

            rng_base = random.SystemRandom()
            msg_attack = msg_attack[rng_base.randint(0, 1)]

            rng_base = random.SystemRandom()
            msg_attack_choice = msg_attack.format(self.CONFIG_DICT['choice_dict'][rng_base.randint(1, 5)])

            rng_base = random.SystemRandom()
            msg_attack_choice_direction = msg_attack_choice.format(self.CONFIG_DICT['monster_direction_dict'][rng_base.randint(1, 4)])

            self.textEdit_combat_text.setText(str(msg_attack_choice_direction))
        else:
            msg_escape = self.CONFIG_DICT['attack_messages'][2]
            self.textEdit_combat_text.setText(msg_escape)


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()

