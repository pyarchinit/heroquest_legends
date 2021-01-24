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

import random, locale
import sqlite3

class Heroquest_solo:
    """main class for variables management"""
    TOTAL_NUMBER_OF_TURNS = 1
    CONFIG_DICT = ''
    CONNECTION = sqlite3.connect('./db_heroquest_legends.sqlite')
    CURSOR = CONNECTION.cursor()

    def __init__(self, cd):
        self.CONFIG_DICT = cd
        self.r_num = random

        #position dict
        self.position_dict = self.CONFIG_DICT['position_dict']

        #{1: 'sinistra',2: 'destra',3: 'sul fondo',4: 'al centro',5: 'davanti a te'}
        #fornitures dict
        self.forniture_dict = self.CONFIG_DICT['fornitures_dict']

        #treasures dict that you can find inside a cest or in other forniture
        self.treasures_dict =  self.CONFIG_DICT['treasures_dict']

        #monsters dict that you can find inside a Room or in a aisle
        self.monsters_dict = self.CONFIG_DICT['monsters_dict']

        rng = random.SystemRandom()
        self.TOTAL_NUMBER_OF_TURNS = rng.randint(4, 12)

    def random_numbers(self):
        """ a random number generator based on four D6.
        A simple statistic to understand the probability of success
        >= X = y%
        4 = 100%
        5 = 99.92%
        6 = 99.61%
        7 = 98.84%
        8 = 97.30%
        9 = 94.60%
        10 = 90.28%
        11 = 84.10%
        12 = 76.08%
        13 = 66.44%
        14 = 55.63%
        15 = 44.37%
        16 = 33.50%
        17 = 23.92%
        18 = 15.90%
        19 = 9.72%
        20 = 5.40%
        21 = 2.70%
        22 = 1.16%
        23 = 0.39%
        24 = 0.08% """

        rng = random.SystemRandom()
        value_1 = rng.randint(1, 6)

        rng = random.SystemRandom()
        value_2 = rng.randint(1, 6)

        rng = random.SystemRandom()
        value_3 = rng.randint(1, 6)

        rng = random.SystemRandom()
        value_4 = rng.randint(1, 6)

        rn_list = [value_1, value_2, value_3, value_4]

        rn_sum = sum(rn_list)

        return rn_sum

    def aisles(self, rv):
        #sistem for discover aisles

        self.rv = rv #recive a random number beetween 4 and 24 for number of doors
        self.LR_n = self.r_num.randint(1, 2) #select beetween left ora right

        rock_msg_value = self.random_numbers()

        #generate a rock message and sometis with a monster
        if rock_msg_value > 0 and rock_msg_value <= 15:
            rocks_msg = self.CONFIG_DICT['aisles_msg_1']

        elif rock_msg_value > 15 and rock_msg_value <= 18:
            rocks_msg = self.CONFIG_DICT['aisles_msg_2']
        else:
            wander_monster_list = [1, 2, 3, 7, 8, 9, 13]
            rocks_msg = self.CONFIG_DICT['aisles_msg_3'].format(
                self.monsters_dict[wander_monster_list[self.r_num.randint(0, len(wander_monster_list)-1)]])

        if self.rv > 1 and self.rv <= 10:
            return self.CONFIG_DICT['aisles_msg_4'].format(self.position_dict[self.LR_n], rocks_msg)

        elif self.rv > 10 and self.rv <= 15:

            return self.CONFIG_DICT['aisles_msg_5'].format(self.position_dict[self.r_num.randint(1, 2)], self.position_dict[self.r_num.randint(1, 2)], rocks_msg)

        elif self.rv > 15 and self.rv <= 20:
            return self.CONFIG_DICT['aisles_msg_6'].format(self.position_dict[self.r_num.randint(1, 2)], self.position_dict[self.r_num.randint(1, 2)], self.position_dict[self.r_num.randint(1, 2)],rocks_msg)
        else:
            return self.CONFIG_DICT['aisles_msg_7']

    def treasures(self, rv):
        self.rv = rv

        if self.rv > 14 and self.rv <= 15:
            return self.CONFIG_DICT['treasures_msg_1']

        elif self.rv > 15 and self.rv <= 22 :
            return self.CONFIG_DICT['treasures_msg_2']

        elif self.rv > 22:
            return self.CONFIG_DICT['treasures_msg_3']
        else:
            return self.CONFIG_DICT['treasures_msg_4']

    def chest(self, rv):
        """"create a random treasures inside chest"""
        self.rv = rv
        #print(rv)
        if self.rv > 1 and self.rv <= 15: #you'll find potions and items
            items_list = []
            nr_items_random = self.random_numbers()
            if nr_items_random >0 and nr_items_random  <= 18:
                items_numbers = 1
            elif nr_items_random >18 and nr_items_random <= 20:
                items_numbers = 2
            else:
                items_numbers = 3
            #items_numbers = self.r_num.randint(1, 3)
            for i in range(items_numbers):
                items_list.append(self.treasures_dict[self.r_num.randint(1, 20)])

            items_list_str = self.CONFIG_DICT['chest_msg_1'].format('\n'.join(items_list))

            return items_list_str

        elif self.rv > 15 and self.rv <= 21: #you'll find gold coins
            msg = self.CONFIG_DICT['chest_msg_2'].format(self.r_num.randrange(1, 500, 25)-1)
            return msg
        elif self.rv > 22:
            return self.CONFIG_DICT['chest_msg_3']

    def secret_doors(self, rv):
        """Create random doors for aisles"""
        self.rv = rv
        self.LR_n = self.r_num.randint(1, 2)

        if self.rv <= 13:
            return self.CONFIG_DICT['secret_doors_msg_1']
        elif self.rv > 13 and self.rv <= 24:
            value_LR = self.r_num.randint(1, 2)
            return self.CONFIG_DICT['secret_doors_msg_2'].format(self.position_dict[self.r_num.randint(1, 2)], self.position_dict[self.r_num.randint(1, 2)])
        else:
            return self.CONFIG_DICT['secret_doors_msg_1']

    def traps(self, rv):
        """search for traps"""

        self.rv = rv

        if self.rv <= 15:
            return self.CONFIG_DICT['traps_msg_1']
        elif self.rv > 15 and self.rv <= 23:
            return self.CONFIG_DICT['traps_msg_2']
        else:
            return self.CONFIG_DICT['traps_msg_3']

    def room_generator(self, rv, room_dimension, ct):
        """create random rooms with fornitures"""
        self.rv = rv #the values recives a number from 4D6
        self.room_dimension = int(room_dimension) #total of room's tiles
        self.current_turn = ct
        forniture_number = 0
        random_id_selected = ''
        select_forniture_list = []
        select_forniture_list_temp = []

        if self.current_turn >= 3 and self.current_turn >= self.TOTAL_NUMBER_OF_TURNS:
            return self.CONFIG_DICT['end_msg_1']
        else:
            if self.rv <=14: #if the random values is minus-equal 14 (between 55% and 100% of cases), the system returns no fornitures
                return self.CONFIG_DICT['fornitures_msg_2']
            else:
                if self.room_dimension <= 6: #for rooms minus-equal to 6 the number of forniture is 1,2 or 3
                    forniture_number = self.r_num.randint(1, 3) #for rooms still can add between 1 or 3 forniture

                    if forniture_number == 1: #if the is selected only on forniture it can take 1, 2 or 3 square
                        square_taken = self.r_num.randint(1, 3)

                        for row in self.CURSOR.execute("SELECT * FROM fornitures WHERE square_taken <= '%s'" % square_taken):
                            select_forniture_list_temp.append(row[0])
                        random_id_selected = select_forniture_list_temp[self.r_num.randint(1,len(select_forniture_list_temp)-1)]
                        res = self.CURSOR.execute("SELECT * FROM fornitures WHERE id_forniture = '%s'" % random_id_selected)
                        forniture_selected = res.fetchone()

                        select_forniture_list.append(

                            '{} {}'.format(self.forniture_dict[forniture_selected[0]],
                                           self.position_dict[self.r_num.randint(1, 3)])) #this command decide the position of the forniture

                        msg_forniture = self.CONFIG_DICT['fornitures_msg_1'].format(", ".join(select_forniture_list))

                    elif forniture_number >= 2: #if fornture number is beetween 2 and 3
                        square_taken = self.r_num.randint(1, 3) #take randomly a fornitures beetween 1 and 3 square taken

                        for row in self.CURSOR.execute("SELECT * FROM fornitures WHERE square_taken <= '%s'" % square_taken):
                            select_forniture_list_temp.append(row[0])
                        random_id_selected = select_forniture_list_temp[self.r_num.randint(1,len(select_forniture_list_temp)-1)]
                        res = self.CURSOR.execute("SELECT * FROM fornitures WHERE id_forniture = '%s'" % random_id_selected)
                        forniture_selected = res.fetchone()
                        select_forniture_list.append(

                            '{} {}'.format(self.forniture_dict[forniture_selected[0]],
                                           self.position_dict[self.r_num.randint(1, 3)])) #this command decide the position of the forniture

                        if square_taken <= 2: #if square taken value is minus-equal 2
                            for row in self.CURSOR.execute("SELECT * FROM fornitures WHERE square_taken <= '%s'" % square_taken):
                                select_forniture_list_temp.append(row[0])
                            random_id_selected = select_forniture_list_temp[
                                self.r_num.randint(1, len(select_forniture_list_temp) - 1)]
                            res = self.CURSOR.execute(
                                "SELECT * FROM fornitures WHERE id_forniture = '%s'" % random_id_selected)
                            forniture_selected = res.fetchone()
                            select_forniture_list.append(

                            '{} {}'.format(self.forniture_dict[forniture_selected[0]],
                                           self.position_dict[self.r_num.randint(1, 3)]))

                            msg_forniture = self.CONFIG_DICT['fornitures_msg_1'].format(", ".join(select_forniture_list))


                        else: #if square taken is more than 2 then
                            for row in self.CURSOR.execute(
                                    "SELECT * FROM fornitures WHERE square_taken = '1'"):
                                select_forniture_list_temp.append(row[0])
                            random_id_selected = select_forniture_list_temp[
                                self.r_num.randint(1, len(select_forniture_list_temp) - 1)]
                            res = self.CURSOR.execute(
                                "SELECT * FROM fornitures WHERE id_forniture = '%s'" % random_id_selected)
                            forniture_selected = res.fetchone()
                            select_forniture_list.append(

                            '{} {}'.format(self.forniture_dict[forniture_selected[0]],
                                           self.position_dict[self.r_num.randint(1, 3)]))

                            msg_forniture = self.CONFIG_DICT['fornitures_msg_1'].format(", ".join(select_forniture_list))


                    elif self.room_dimension > 6 and self.room_dimension <= 16: #if room is beetween 6 and 16 squares
                        square_taken = self.r_num.randint(1, 6)  # take randomly a fornitures beetween 1 and 6 square taken

                        forniture_number = self.r_num.randint(1, 3) #for rooms beetwee 6 and 16 squares ad between 1 and 3 forniture
                        for row in self.CURSOR.execute("SELECT * FROM fornitures WHERE square_taken <= '%s'" % square_taken):
                            select_forniture_list_temp.append(row[0])
                        random_id_selected = select_forniture_list_temp[
                            self.r_num.randint(1, len(select_forniture_list_temp) - 1)]
                        res = self.CURSOR.execute(
                            "SELECT * FROM fornitures WHERE id_forniture = '%s'" % random_id_selected)
                        forniture_selected = res.fetchone()
                        select_forniture_list.append(

                            '{} {}'.format(self.forniture_dict[forniture_selected[0]],
                                           self.position_dict[self.r_num.randint(1, 3)]))

                        msg_forniture = self.CONFIG_DICT['fornitures_msg_1'].format(", ".join(select_forniture_list))

                    """
                    for i in range(forniture_number):
                        select_forniture_list.append('{} {}'.format(self.forniture_dict[self.r_num.randint(1, 12)], self.position_dict[self.r_num.randint(1, 3)]))
                        msg_forniture = self.CONFIG_DICT['fornitures_msg_1'].format(", ".join(select_forniture_list))
                    """

                elif self.room_dimension > 16:

                    square_taken = self.r_num.randint(1, 6)  # take randomly a fornitures beetween 1 and 6 square taken

                    forniture_number = self.r_num.randint(1,
                                                          3)  # for rooms beetwee 6 and 16 squares ad between 1 and 3 forniture
                    for row in self.CURSOR.execute("SELECT * FROM fornitures WHERE square_taken <= '%s'" % square_taken):
                        select_forniture_list_temp.append(row[0])
                    random_id_selected = select_forniture_list_temp[
                        self.r_num.randint(1, len(select_forniture_list_temp) - 1)]
                    res = self.CURSOR.execute(
                        "SELECT * FROM fornitures WHERE id_forniture = '%s'" % random_id_selected)
                    forniture_selected = res.fetchone()
                    select_forniture_list.append(

                        '{} {}'.format(self.forniture_dict[forniture_selected[0]],
                                       self.position_dict[self.r_num.randint(1, 3)]))

                    msg_forniture = self.CONFIG_DICT['fornitures_msg_1'].format(", ".join(select_forniture_list))

                    """
                    forniture_number = self.r_num.randint(1, 4) #for rooms still 6 squares add between 1 and 4 forniture
                    for i in range(forniture_number):
                        select_forniture_list.append('{} {}'.format(self.forniture_dict[self.r_num.randint(1, 12)], self.position_dict[self.r_num.randint(1, 3)]))
    
    
                        msg_forniture = self.CONFIG_DICT['fornitures_msg_1'].format(", ".join(select_forniture_list))
                    """
            return msg_forniture

    def monsters_generator(self, rv, room_dimension):
        """create random monsters for rooms based on room dimension"""
        self.rv = rv
        self.room_dimension = int(room_dimension)
        self.LR_n = self.position_dict[self.r_num.randint(1, 5)]
        monsters_number = 0
        if self.rv > 13:
            if self.room_dimension <= 6:
                monsters_number = 1
            elif self.room_dimension > 9 and self.room_dimension <= 16:
                monsters_number = self.r_num.randint(1, 3)
            elif self.room_dimension > 16:
                monsters_number = self.r_num.randint(1, 4)
            select_monsters_list = []

            for i in range(monsters_number):
                monster_dict_length = len(self.monsters_dict)
                select_monsters_list.append('{} {}'.format(self.monsters_dict[self.r_num.randint(1, monster_dict_length)], self.position_dict[self.r_num.randint(1, 5)]))

            msg_monsters = self.CONFIG_DICT['monsters_msg_1'].format(", ".join(select_monsters_list))
            return msg_monsters

        else:
            return self.CONFIG_DICT['monsters_msg_2']

#TODO FIGTHTING SYSTEM