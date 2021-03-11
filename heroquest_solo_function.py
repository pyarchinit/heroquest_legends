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

import random
import sqlite3

class Heroquest_solo:
    """main class for variables management"""
    rng = random.SystemRandom()
    TOTAL_NUMBER_OF_TURNS = rng.randint(4, 12)

    ESCAPE_FOUND = 0

    CONFIG_DICT = ''

    CONNECTION = sqlite3.connect('./db_heroquest_legends.sqlite')
    CURSOR = CONNECTION.cursor()

    #charge the total of forniture linked to ID
    db_fornitures_query = CURSOR.execute("Select * from fornitures")
    db_fornitures_charged = db_fornitures_query.fetchall()

    #charge the total of monsters linked to ID
    db_monsters_query = CURSOR.execute("Select * from monsters")
    db_monsters_charged = db_monsters_query.fetchall()


    FORNITURES_QTY_DICT = {1:db_fornitures_charged[0][2],
                           2:db_fornitures_charged[1][2],
                           3:db_fornitures_charged[2][2],
                           4:db_fornitures_charged[3][2],
                           5:db_fornitures_charged[4][2],
                           6:db_fornitures_charged[5][2],
                           7:db_fornitures_charged[6][2],
                           8:db_fornitures_charged[7][2],
                           9:db_fornitures_charged[8][2],
                           10:db_fornitures_charged[9][2],
                           11:db_fornitures_charged[10][2],
                           12:db_fornitures_charged[11][2],
                           13:db_fornitures_charged[12][2]}

    MONSTERS_QTY_DICT = {1:db_monsters_charged[0][2],
                           2:db_monsters_charged[1][2],
                           3:db_monsters_charged[2][2],
                           4:db_monsters_charged[3][2],
                           5:db_monsters_charged[4][2],
                           6:db_monsters_charged[5][2],
                           7:db_monsters_charged[6][2],
                           8:db_monsters_charged[7][2]}


    def __init__(self, cd):
        self.CONFIG_DICT = cd
        self.r_num = random

        #position dict
        self.position_dict = self.CONFIG_DICT['position_dict']

        #fornitures dict
        self.forniture_dict = self.CONFIG_DICT['fornitures_dict']

        #treasures dict that you can find inside a cest or in other forniture
        self.treasures_dict =  self.CONFIG_DICT['treasures_dict']

        #monsters dict that you can find inside a Room or in a aisle
        self.monsters_dict = self.CONFIG_DICT['monsters_dict']


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


    def room_generator(self, room_dimension, ct, re):
        """create random rooms with fornitures"""

        #turn controller INPUT
        self.current_turn = ct

        #room controller INPUT
        self.room_explored = int(re)
        self.room_dimension = int(room_dimension) #total of room's tiles

        #forniture_square_taken
        tot_square_taken = 0

        #messages controller
        msg_forniture = ''
        msg_monsters = ''
        msg_end = ''
        msg_list = []

        #roll the dice and select a random number of fornitures between 1 and 4
        rng = random.SystemRandom()
        forniture_numbers = rng.randint(1, 4)
        count = 0
        #if the current turn is max or equal and the escape is founded
        if self.current_turn >= self.TOTAL_NUMBER_OF_TURNS and self.ESCAPE_FOUND==0:
            msg_end = self.CONFIG_DICT['end_msg_1']
            self.ESCAPE_FOUND = 1
        else:
            if self.room_explored == 0: #if the room is not explored
                print("step_1")
                count = 0                           #counter
                for i in range(forniture_numbers):
                    rng_1 = random.SystemRandom()
                    id_forniture_rand_1 = rng_1.randint(0, 6)

                    rng_2 = random.SystemRandom()
                    id_forniture_rand_2 = rng_2.randint(1, 7)  #create a random ID for fornitures between 1 and 13

                    id_forniture_rand = id_forniture_rand_1+id_forniture_rand_2


                    #verify if the fornitures is still present
                    forniture_residue = self.FORNITURES_QTY_DICT[id_forniture_rand]
                    if forniture_residue > 0:
                        print("step_2")
                        # charge from DB the selected fornitures
                        res = self.CURSOR.execute(
                            "SELECT * FROM fornitures WHERE id_forniture = %d" % id_forniture_rand)
                        forniture_selected = res.fetchone()
                        print("step_12")
                        square_taken_temp = forniture_selected[4]
                        tot_square_taken += square_taken_temp
                        print("step_13")
                        if tot_square_taken < self.room_dimension:
                            print("step_15")
                            msg_forniture = '{}{}{}'.format(msg_forniture, self.forniture_dict[id_forniture_rand],self.position_dict[self.r_num.randint(1, 5)])
                            print("step_5")
                            new_forniture_residue = forniture_residue - 1
                            self.FORNITURES_QTY_DICT[id_forniture_rand] = new_forniture_residue
                        else:
                            print("step_6")
                            tot_square_taken -= square_taken_temp
                    else:
                        print("step_7")
                        msg_forniture = msg_forniture

            else:
                msg_forniture = self.CONFIG_DICT['aux_msg_7']

            if msg_forniture != '':
                msg_rand = rng.randint(0, 3)
                aux_message = ['aux_msg_2', 'aux_msg_3', 'aux_msg_4', 'aux_msg_5']
                msg_forniture = '{} {}.'.format(self.CONFIG_DICT[aux_message[msg_rand]], msg_forniture)

        msg_monsters = self.monsters_generator_2(self.random_numbers(),tot_square_taken, self.current_turn)


        msg_list.append(msg_forniture)
        msg_list.append(msg_monsters)
        msg_list.append(msg_end)

        return msg_list

    def monsters_generator_2(self, rv, square_taken, ct):
        """create random group of monsters based on squares taken by fornitures"""
        self.rv = rv #the random values to know to create the percentage of possibilities to find monsters

        self.residual_tiles = int(square_taken) #total of room's tiles residue
        self.current_turn = ct

        msg_monsters = ''
        monsters_msg_partial = ''
        print("monster_value{}".format(str(self.rv)))
        if self.rv >= 18:
            return '{} {}'.format(msg_monsters, self.CONFIG_DICT['monsters_msg_2'])
        else:
            if self.residual_tiles <= 3:
                monsters_number = 1
            elif self.residual_tiles > 3 and self.residual_tiles <= 6:
                rng_base = random.SystemRandom()
                monsters_number = rng_base.randint(1, 2)
            elif self.residual_tiles > 6 and self.residual_tiles <= 12:
                rng_base = random.SystemRandom()
                monsters_number = rng_base.randint(1, 3)
            elif self.residual_tiles > 12 and self.residual_tiles <= 20:
                rng_base = random.SystemRandom()
                monsters_number = rng_base.randint(1,6)
            else:
                rng_base = random.SystemRandom()
                monsters_number = rng_base.randint(1, 6)

            for i in range(monsters_number):
                rng_1 = random.SystemRandom()
                id_monster_rand_1 = rng_1.randint(0, 2)

                rng_2 = random.SystemRandom()
                id_monster_rand_2 = rng_2.randint(1, 6)

                id_monster_rand = id_monster_rand_1 + id_monster_rand_2
                monsters_residue = self.MONSTERS_QTY_DICT[id_monster_rand]

                if monsters_residue > 0:
                    monsters_msg_partial = '{} {} {};'.format(monsters_msg_partial, self.monsters_dict[id_monster_rand],
                                                       self.position_dict[self.r_num.randint(1, 5)])

                    new_monster_residue = monsters_residue - 1

                    self.MONSTERS_QTY_DICT[id_monster_rand] = new_monster_residue

            if monsters_msg_partial != '':
                msg_monsters = '{} {} {}'.format(self.CONFIG_DICT['monsters_msg_intro'], monsters_msg_partial, self.CONFIG_DICT['monsters_msg_close'])
            else:
                msg_monsters = '{} {}'.format(self.CONFIG_DICT['monsters_msg_intro'],self.CONFIG_DICT['monsters_msg_2'])
        return msg_monsters


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

    def treasure_random(self, rv):
        """"create a random treasures inside chest"""
        self.rv = rv
        if self.rv >= 4 and self.rv <= 12: #you'll find potions and items
            items_list = []
            nr_items_random = self.random_numbers()
            if nr_items_random >=4 and nr_items_random  <= 18: #probability to find one treasure
                items_numbers = 1
            elif nr_items_random >18 and nr_items_random <= 20: #probability to find two treasure
                items_numbers = 2
            else:
                items_numbers = 3 #probability to find three treasure

            for i in range(items_numbers):
                items_list.append(self.treasures_dict[self.r_num.randint(1, 20)]) #select randomly
            items_list_str = self.CONFIG_DICT['chest_msg_1'].format('\n'.join(items_list))
            return items_list_str
        elif self.rv > 12 and self.rv <= 20: #you'll find gold coins
            print("tres_rand_2")
            msg = self.CONFIG_DICT['chest_msg_2'].format(self.r_num.randrange(1, 150, 5)-1)
            return msg
        elif self.rv > 20 and self.rv <= 22:  #you'll find a trap!
            print("tres_rand_3")
            return self.CONFIG_DICT['chest_msg_3']
        else:
            rng_1 = random.SystemRandom() #you'll find a weapon
            weapon_rand_num = rng_1.randint(1, 9)
            msg = self.CONFIG_DICT['chest_msg_4'].format(self.CONFIG_DICT['weapons_dict'][weapon_rand_num])
            return msg

    def treasure_card(self, rv):
        """"create a random treasures inside chest"""
        self.rv = rv
        if self.rv > 1 and self.rv <= 12: #you'll find a wanderer monster
            treasure_description = self.CONFIG_DICT["treasures_dict"][19]
            return treasure_description
        elif self.rv > 13 and self.rv <= 16: #you'll find a heoling potion
            treasure_description = self.CONFIG_DICT["treasures_dict"][5]
            return treasure_description
        elif self.rv > 16:
            rng_1 = random.SystemRandom()
            treasure_description = self.CONFIG_DICT["treasures_dict"][rng_1.randint(1, 20)]
            return treasure_description

    def traps_secret_doors(self, rv):
        """Create random doors for aisles"""
        self.rv = rv


        if self.rv <= 13:
            return self.CONFIG_DICT['secret_doors_msg_1']
        elif self.rv > 13 and self.rv <= 24:
            value_LR = self.r_num.randint(1, 3)
            return self.CONFIG_DICT['secret_doors_msg_2'].format(self.position_dict[self.r_num.randint(1, 3)])
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

    def fighting_system(self, mc):
        self.monster_category = mc

        combat_value_dict = self.CONFIG_DICT['combat_value_dict']

        combat_value = combat_value_dict[self.monster_category]

        aggr_rand_num = self.random_numbers()
        aggression_value = aggr_rand_num+combat_value

        if aggression_value >17:
            #heroes mode
            return 1
        else:
            #villan mode
            return 2



#TODO FIGTHTING SYSTEM