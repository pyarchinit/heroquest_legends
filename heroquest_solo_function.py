# -*- coding: utf-8 -*-

"""
/***************************************************************************
        Heroquest's Legends Solo by Mandor the Druid
                             -------------------
    begin                : 2021-01-02
    copyright            : (C) 2021 by Luca Mandolesi
    email                : mandoluca at gmail.com
    version              : 0.83 ALPHA
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

#TODO se il mostro può attaccare subito perchè vicino all'eroe, segnalare se poi si allontana o resta lì
#TODO E' nella linea di vista del mostro l'eroe?
#TODO I MOSTRI SONO IN GRUPPO SE SI VEDONO RECIPROCAMENTE
#TODO inserire sequenza di movimento mostri se quello con più punti attacco, quello che si muove di più

class Heroquest_solo:
    """main class for variables management"""
    rng = random.SystemRandom()
    TOTAL_NUMBER_OF_TURNS = rng.randint(6, 15)

    rng = random.SystemRandom()
    MAX_ROOM_COUNTER = rng.randint(6, 12)

    CURRENT_ROOM_COUNTER = 0

    ESCAPE_FOUND = 0

    FIRST_ROOM = 0

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
                         8:db_monsters_charged[7][2],
                         9:db_monsters_charged[8][2]}

    MONSTERS_COMBAT_VALUES_DICT = {1:db_monsters_charged[0][4],
                                   2:db_monsters_charged[1][4],
                                   3:db_monsters_charged[2][4],
                                   4:db_monsters_charged[3][4],
                                   5:db_monsters_charged[4][4],
                                   6:db_monsters_charged[5][4],
                                   7:db_monsters_charged[6][4],
                                   8:db_monsters_charged[8][4],
                                   9:db_monsters_charged[7][4]}

    MONSTERS_CATEGORY = {1:db_monsters_charged[0][1],
                         2:db_monsters_charged[1][1],
                         3:db_monsters_charged[2][1],
                         4:db_monsters_charged[3][1],
                         5:db_monsters_charged[4][1],
                         6:db_monsters_charged[5][1],
                         7:db_monsters_charged[6][1],
                         8:db_monsters_charged[7][1],
                         9:db_monsters_charged[8][1]
                         }

    THE_MISSION = ''

    SPECIAL_ROOM_CHARGED = ''

    MONSTER_CLASS = ''

    def __init__(self, cd):
        self.CONFIG_DICT = cd
        self.r_num = random

        #position dict
        self.position_dict = self.CONFIG_DICT['position_dict']

        #fornitures dict
        self.forniture_dict = self.CONFIG_DICT['fornitures_dict']

        #treasures dict that you can find inside a cest or in other forniture
        self.treasures_card_dict =  self.CONFIG_DICT['treasures_card_dict']

        #monsters dict that you can find inside a Room or in a aisle
        self.monsters_dict = self.CONFIG_DICT['monsters_dict']

    def special_data_mission_charged(self, mn):
        self.THE_MISSION = int(mn)
        self.SPECIAL_ROOM_CHARGED = self.CONFIG_DICT['specials_rooms'][self.THE_MISSION]
        self.MONSTER_CLASS = self.CONFIG_DICT['monster_class'][self.THE_MISSION]

        #remove_forniture_for_special_room
        id_forniture_special_room_list = self.SPECIAL_ROOM_CHARGED[0] #charge id list
        for i in id_forniture_special_room_list:
            tot_forniture = self.FORNITURES_QTY_DICT[i]
            new_tot_forniture = tot_forniture-1
            self.FORNITURES_QTY_DICT[i] = new_tot_forniture

    def random_numbers(self):
        """ a random number generator based on four D6.
        A simple statistic to understand the probability of success
        >= X == y%
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
        #print("entrata in room generato")
        #turn controller INPUT
        self.current_turn = ct

        #room controller INPUT
        self.room_explored = int(re)
        self.room_dimension = int(room_dimension)/2 #total of room's tiles

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

        if self.room_explored == 0:
            #print("entrata in room generato 2")
            if self.CURRENT_ROOM_COUNTER < self.MAX_ROOM_COUNTER:
                self.CURRENT_ROOM_COUNTER += 1

        #print("entrata in room generato 3")
        if self.current_turn >= self.TOTAL_NUMBER_OF_TURNS : #and self.ESCAPE_FOUND==0 and self.room_explored == 0 and self.CURRENT_ROOM_COUNTER >= self.MAX_ROOM_COUNTER
            #print("entrata in room generato 4")
            #print("special room charged: {}".format(str(self.SPECIAL_ROOM_CHARGED)))
            msg_end = self.SPECIAL_ROOM_CHARGED[1] #Replace the number with THE_MISSION = RAND_NUM
            self.ESCAPE_FOUND = 1
        else:
            #print("entrata in room generato 5")
            if self.room_explored == 0: #if the room is not explored
                count = 0 #counter
                for i in range(forniture_numbers):
                    rng_1 = random.SystemRandom()
                    id_forniture_rand_1 = rng_1.randint(0, 6)

                    rng_2 = random.SystemRandom()
                    id_forniture_rand_2 = rng_2.randint(1, 7)  #create a random ID for fornitures between 1 and 13

                    id_forniture_rand = id_forniture_rand_1+id_forniture_rand_2

                    #verify if the fornitures is still present
                    forniture_residue = self.FORNITURES_QTY_DICT[id_forniture_rand]
                    if forniture_residue > 0:
                        #print("entrata in room generato 6")
                        # charge from DB the selected fornitures
                        res = self.CURSOR.execute(
                            "SELECT * FROM fornitures WHERE id_forniture = %d" % id_forniture_rand)
                        forniture_selected = res.fetchone()
                        #print("entrata in room generato 7")
                        #print("format forniture selected {}".format(str(forniture_selected[4])))
                        square_taken_temp = forniture_selected[4]
                        tot_square_taken += square_taken_temp
                        #if there is residue space in rooms
                        if tot_square_taken < self.room_dimension:
                            #print("entrata in room generato 8")
                            if count == 0:
                                #print("entrata in room generato 9")
                                if id_forniture_rand == 11 or id_forniture_rand == 12:
                                    msg_forniture = '{} {} {};'.format(msg_forniture, self.forniture_dict[id_forniture_rand],self.position_dict[self.r_num.randint(1, 3)])
                                else:
                                    msg_forniture = '{} {} {};'.format(msg_forniture, self.forniture_dict[id_forniture_rand],self.position_dict[self.r_num.randint(1, 5)])
                                new_forniture_residue = forniture_residue - 1
                                self.FORNITURES_QTY_DICT[id_forniture_rand] = new_forniture_residue
                                count = 1
                            else:
                                msg_forniture = '{} {} {};'.format(msg_forniture, self.forniture_dict[id_forniture_rand],
                                                                 self.position_dict[self.r_num.randint(1, 5)])
                                new_forniture_residue = forniture_residue - 1
                                self.FORNITURES_QTY_DICT[id_forniture_rand] = new_forniture_residue
                        else: #no forniture is added and the temporary squares is re added
                            #print("entrata in room generato 10")
                            tot_square_taken -= square_taken_temp
                    else: #if the forniture is not present
                        msg_forniture = msg_forniture
                if msg_forniture != '':
                    msg_rand = rng.randint(0, 3)
                    aux_message = ['aux_msg_2', 'aux_msg_3', 'aux_msg_4', 'aux_msg_5']
                    msg_forniture = '{} {}.'.format(self.CONFIG_DICT[aux_message[msg_rand]], msg_forniture)
            else:
                #print("entrata in room generato 10 B")
                msg_forniture = self.CONFIG_DICT['aux_msg_7']

        #generate the room
        if self.FIRST_ROOM == 1:
            #print("entrata in room generato 11")
            msg_monsters = self.monsters_generator_2(self.random_numbers(),tot_square_taken, self.current_turn)
        else:
            #print("entrata in room generato 12")
            msg_monsters = self.CONFIG_DICT['monsters_msg_first_room']
            self.FIRST_ROOM = 1

        #print("entrata in room generato 13")
        msg_list.append(msg_forniture)
        msg_list.append(msg_monsters)
        msg_list.append(msg_end)

        return msg_list

    def monsters_generator_2(self, rv, square_taken, ct):
        """create random group of monsters based on squares taken by fornitures"""
        #print("monster_generator_2")
        self.rv = rv #the random values to know to create the percentage of possibilities to find monsters

        self.residual_tiles = int(square_taken) #total of room's tiles residue
        self.current_turn = ct

        msg_monsters = ''
        monsters_msg_partial = ''

        if self.rv >= 20:
            #print("monster_generator_2 2")
            return '{} {}'.format(msg_monsters, self.CONFIG_DICT['monsters_msg_2'])
        else:
            if self.residual_tiles <= 3:
                monsters_number = 1
            elif self.residual_tiles > 3 and self.residual_tiles <= 6:
                rng_base = random.SystemRandom()
                monsters_number = rng_base.randint(2, 3)
            elif self.residual_tiles > 6 and self.residual_tiles <= 12:
                rng_base = random.SystemRandom()
                monsters_number = rng_base.randint(2,4)
            elif self.residual_tiles > 12 and self.residual_tiles <= 20:
                rng_base = random.SystemRandom()
                monsters_number = rng_base.randint(4,6)
            else:
                rng_base = random.SystemRandom()
                monsters_number = rng_base.randint(3, 6)

            #print("monster_generator_2 3")
            for i in range(monsters_number):
                #choose id based on monster class
                query_string = "Select id_monster from monsters where monster_class = '{}' or monster_class LIKE '%{}' or monster_class LIKE '{}%' or monster_class LIKE '%{}%'".format(self.MONSTER_CLASS, self.MONSTER_CLASS, self.MONSTER_CLASS, self.MONSTER_CLASS)
                db_monsters_class_query = self.CURSOR.execute(query_string)
                db_monsters_class_charged = db_monsters_class_query.fetchall()
                db_monsters_class_charged_list = []
                #print("monster_generator_2 4")
                for i in db_monsters_class_charged:
                    db_monsters_class_charged_list.append(i[0])

                #print("monster_generator_2 5")
                db_monsters_class_charged_lenght = len(db_monsters_class_charged_list)-1
                rng = random.SystemRandom()
                id_monster_rand = db_monsters_class_charged_list[rng.randint(0, db_monsters_class_charged_lenght)]
                #print("monster_generator_2 6")
                #print("id_monster_rand {}".format(id_monster_rand))
                #print("MONSTERS_QTY_DICT: {}".format(self.MONSTERS_QTY_DICT[id_monster_rand]))
                monsters_residue = int(self.MONSTERS_QTY_DICT[id_monster_rand])
                #print("monster_generator_2 7")
                if monsters_residue > 0:
                    #print("monster_generator_2 8")
                    monsters_msg_partial = '{} {} {};'.format(monsters_msg_partial,
                                                              self.monsters_dict[id_monster_rand],
                                                              self.position_dict[self.r_num.randint(1, 5)])

                    new_monster_residue = int(monsters_residue) - 1

                    self.MONSTERS_QTY_DICT[id_monster_rand] = new_monster_residue

            if monsters_msg_partial != '':
                #print("monster_generator_2 4")
                msg_monsters = '{} {} {}'.format(self.CONFIG_DICT['monsters_msg_intro'], monsters_msg_partial, self.CONFIG_DICT['monsters_msg_close'])
            else:
                #print("monster_generator_2 5")
                msg_monsters = '{} {}'.format(self.CONFIG_DICT['monsters_msg_intro'],self.CONFIG_DICT['monsters_msg_2'])
        return msg_monsters

    def random_monsters_on_aisles(self, n):
        turn = n

        rn = self.random_numbers()
        comparison_value = 0


        if turn >= 1 and turn <= 15:
            comparison_value = 23
        elif turn > 15 and turn <= 20:
            comparison_value = 22
        else:
            comparison_value = 18
        if rn >= comparison_value:
            query_string = "Select id_monster from monsters where monster_class = '{}' or monster_class LIKE '%{}' or monster_class LIKE '{}%' or monster_class LIKE '%{}%'".format(
                self.MONSTER_CLASS, self.MONSTER_CLASS, self.MONSTER_CLASS, self.MONSTER_CLASS)
            db_monsters_class_query = self.CURSOR.execute(query_string)
            db_monsters_class_charged = db_monsters_class_query.fetchall()
            db_monsters_class_charged_list = []
            for i in db_monsters_class_charged:
                db_monsters_class_charged_list.append(i[0])

            db_monsters_class_charged_lenght = len(db_monsters_class_charged_list) - 1
            rng = random.SystemRandom()
            id_monster_rand = db_monsters_class_charged_list[rng.randint(0, db_monsters_class_charged_lenght)]
            monsters_residue = self.MONSTERS_QTY_DICT[id_monster_rand]

            if monsters_residue > 0:
                msg_monsters = self.CONFIG_DICT['aux_msg_9'].format(self.monsters_dict[id_monster_rand])
                new_monster_residue = monsters_residue - 1
                self.MONSTERS_QTY_DICT[id_monster_rand] = new_monster_residue
                return msg_monsters
        else:
            return self.CONFIG_DICT['aux_msg_10']


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
            rocks_msg = self.CONFIG_DICT['aisles_msg_3'].format(self.monsters_dict[self.r_num.randint(1, 7)])

        #aisles generators with doors
        if self.rv > 19 and self.rv <= 22 and self.FORNITURES_QTY_DICT[11] >= 3:  # three doors
            msg_1 = self.CONFIG_DICT['aisles_msg_6'].format(self.position_dict[self.r_num.randint(1, 2)], self.position_dict[self.r_num.randint(1, 2)], self.position_dict[self.r_num.randint(1, 2)], rocks_msg)
            new_doors_residue = self.FORNITURES_QTY_DICT[11] - 3
            self.FORNITURES_QTY_DICT[11] = new_doors_residue

            return '{} {}'.format(msg_1, self.CONFIG_DICT['aisles_msg_8'])

        elif self.rv > 12 and self.rv <= 19 and self.FORNITURES_QTY_DICT[11] >= 2: #two doors
            msg_1 = self.CONFIG_DICT['aisles_msg_5'].format(self.position_dict[self.r_num.randint(1, 2)], self.position_dict[self.r_num.randint(1, 2)], rocks_msg)
            new_doors_residue = self.FORNITURES_QTY_DICT[11] - 2
            self.FORNITURES_QTY_DICT[11] = new_doors_residue

            return '{} {}'.format(msg_1, self.CONFIG_DICT['aisles_msg_8'])

        elif self.rv > 1 and self.rv <= 12 and self.FORNITURES_QTY_DICT[11] >= 1: #one door
            msg_1 = self.CONFIG_DICT['aisles_msg_4'].format(self.position_dict[self.LR_n], rocks_msg)
            new_doors_residue = self.FORNITURES_QTY_DICT[11] - 1
            self.FORNITURES_QTY_DICT[11] = new_doors_residue

            return '{} {}'.format(msg_1, self.CONFIG_DICT['aisles_msg_8'])

        elif self.rv > 22 and self.rv <= 24 or self.FORNITURES_QTY_DICT[11] == 0:
            return self.CONFIG_DICT['aisles_msg_7']

        else:
            return self.CONFIG_DICT['aisles_msg_7']

    def treasures(self, rv):
        self.rv = rv
        if self.rv > 1 and self.rv <= 15:
            return (self.CONFIG_DICT['treasures_msg_1'], 0) #you find nothing. Draw a treasure card.
        elif self.rv > 15 and self.rv <= 22 :
            return (self.CONFIG_DICT['treasures_msg_2'], 1) #you find a random treasure
        elif self.rv > 22:
            return (self.CONFIG_DICT['treasures_msg_3'], 0) #You find a trap!
        else:
            return (self.CONFIG_DICT['treasures_msg_4'], 1) #you find nothing. Draw a treasure card.

    def treasure_random(self, rv, forniture):
        """"create a random treasures inside chest"""
        self.forniture = forniture

        self.rv = rv
        if self.rv > 1 and self.rv <= 13 and self.forniture != '-': #a special treasure
            forniture_id_txt = self.CONFIG_DICT['forniture_name_reconversion_dict'][self.forniture]
            treasure_list = self.CONFIG_DICT['treasures_random_type'][forniture_id_txt]
            max_rand_value = len(treasure_list)-1
            rng = random.SystemRandom()
            value_for_selection = rng.randint(0, max_rand_value)
            msg_random_treasure = treasure_list[value_for_selection]
            return msg_random_treasure

        elif self.rv > 13 and self.rv <= 20: #you'll find gold coins
            msg = self.CONFIG_DICT['chest_msg_2'].format(self.r_num.randrange(50, 150, 5))
            return msg

        elif self.rv > 20 and self.rv <= 22:  #you'll find a trap!
            return self.CONFIG_DICT['chest_msg_3']

        else:
            rng_1 = random.SystemRandom() #you'll find a weapon
            weapon_rand_num = rng_1.randint(1, 9)
            msg = self.CONFIG_DICT['chest_msg_4'].format(self.CONFIG_DICT['weapons_dict'][weapon_rand_num])

            return msg

    def treasure_card(self, rv):
        """"create a random treasures inside chest"""
        self.rv = rv
        if self.rv >= 1 and self.rv <= 12: #you'll find a wanderer monster
            treasure_description = self.treasures_card_dict[19]
            return treasure_description
        elif self.rv > 12 and self.rv <= 16: #you'll find a healing potion

            treasure_description = self.treasures_card_dict[5]
            return treasure_description
        else:
            rng_1 = random.SystemRandom()
            treasure_description = self.treasures_card_dict[rng_1.randint(1, 20)]
            return treasure_description

    def secret_doors(self, rv):
        """Create random doors for aisles"""
        self.rv = rv

        if self.rv >= 1 and self.rv <= 15:
            return self.CONFIG_DICT['secret_doors_msg_1'] #no secret doors
        elif self.rv > 15 and self.rv <= 20 :
            value_LR = self.r_num.randint(1, 3)
            return self.CONFIG_DICT['secret_doors_msg_2'].format(self.position_dict[value_LR]) #find a secret doot
        else:
            return self.CONFIG_DICT['secret_doors_msg_3'] #find a trapdoor

    def traps(self, rv):
        """search for traps"""
        self.rv = rv
        if self.rv <= 15:
            return self.CONFIG_DICT['traps_msg_1']
        elif self.rv > 15 and self.rv <= 23:
            return self.CONFIG_DICT['traps_msg_2']
        else:
            return self.CONFIG_DICT['traps_msg_3']

    def fighting_system(self, mc, mg, ms):

        self.monster_category = mc
        self.monster_group = mg
        self.monster_sight = ms

        #COMBAT VALUE FROM DB
        combat_value_dict = self.CONFIG_DICT['combat_value_dict']
        monster_converted = self.CONFIG_DICT['monster_name_reconversion_dict'][self.monster_category]
        combat_value = combat_value_dict[monster_converted]

        #IF GROUPED aggresivity_bonus VALUE RANDOM 1-3 TO ADD
        #RANDO VALUE 4D6
        aggresivity_bonus = 0
        if self.monster_group == 1:
            rng = random.SystemRandom()
            aggresivity_bonus = rng.randint(1, 10)

        if self.monster_sight == 1:
            rng = random.SystemRandom()
            aggresivity_bonus += rng.randint(1, 5)

        aggr_rand_num = self.random_numbers()

        aggression_value = combat_value+aggr_rand_num

        final_aggression_value = aggression_value+aggresivity_bonus

        if final_aggression_value > 30:
            #heroe mode
            return 1
        else:
            #villan mode
            return 2

    def random_trap(self, n):
        self.turn = int(n)
        comparison_value = 0
        rn = self.random_numbers()

        if self.turn >= 1 or turn <= 15:
            comparison_value = 23

        elif self.turn > 15 or turn <= 20:
            comparison_value = 22

        elif self.turn > 20 or turn <= 26:
            comparison_value = 18
        else:
            comparison_value = 20

        if rn <= comparison_value:
            msg = ''
            return msg
        else:
            return self.CONFIG_DICT['aux_msg_8']




#TODO FIGTHTING SYSTEM
