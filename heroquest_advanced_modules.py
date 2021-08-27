#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
/***************************************************************************
        Heroquest's Legends Solo by Mandor the Druid
                             -------------------
    begin                : 2021-01-02
    copyright            : (C) 2021 by Luca Mandolesi
    email                : mandoluca at gmail.com
    version              : 0.91 ALPHA
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

class Heroquest_Advanced_Modules:


    def random_numbers(self, c):

        self.choice_dice = c

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


#PASSAGES

        if self.choice_dice == "D12":
            rng = random.SystemRandom()
            value_1 = rng.randint(1, 6)

            rng = random.SystemRandom()
            value_2 = rng.randint(1, 6)

            rn_list = [value_1, value_2]

        elif self.choice_dice == "2D12":
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

    def passages_lenght_table(self, n):
        """receive one D12 value"""
        self.number = n
        if  self.number >= 1 and self.number <= 2:
            return "1 section"
        elif  self.number >2 and self.number <= 8:
            return "2 sections"
        else:
            return "3 sections"

    def passages_features_table(self, n):
        """receive 2D12 value"""
        self.number = n
        if  self.number >= 2 and self.number <= 4:
            return "Wandering Monster"
        elif  self.number >4 and self.number <= 15:
            return "Nothing"
        elif  self.number >15 and self.number <= 19:
            return "1 Door"
        elif  self.number >19 and self.number <= 21:
            return "2 Doors"
        elif  self.number >21 and self.number <= 24:
            return "Wandering Monster"

    def passages_end_table(self, n):
        """receive 2D12 value"""
        self.number = n
        if  self.number >= 2 and self.number <= 3:
            return "T-Junction"
        elif  self.number >3 and self.number <= 8:
            return "Dead end"
        elif  self.number >8 and self.number <= 11:
            return "Right turn"
        elif  self.number >11 and self.number <= 14:
            return "T-Junction"
        elif  self.number >14 and self.number <= 17:
            return "Left turn"
        elif  self.number >17 and self.number <= 19:
            return "Stairs down"
        elif  self.number >19 and self.number <= 22:
            return "Stairs out"
        elif  self.number >22 and self.number <= 24:
            return "T-Junction"

    def room_type_table(self, n):
        """receive one D12 value"""
        self.number = n
        if  self.number >= 1 and self.number <= 6:
            return "Normal - small"
        elif  self.number >6 and self.number <= 8:
            return "Hazard - small"
        elif  self.number >8 and self.number <= 10:
            return "Liar - large"
        elif  self.number >10 and self.number <= 12:
            return "Quest - large"

    def room_doors_table(self, n):
        """receive one D12 value"""
        self.number = n
        if  self.number >= 1 and self.number <= 4:
            return "None"
        elif  self.number >6 and self.number <= 8:
            return "1 Door"
        elif  self.number >8 and self.number <= 10:
            return "2 Door"

    def hazard_table(self, n):
        """receive one D12 value"""
        self.number = n
        if self.number == 1:
            return "Wandering monster"
        elif self.number == 2:
            return "Non-player Character"
        elif self.number == 3:
            return "Chasm"
        elif self.number == 4:
            return "Statue"
        elif self.number == 5:
            return "Rats or Bats"
        elif self.number == 6:
            return "Mould"
        elif self.number == 7:
            return "Mushrooms"
        elif self.number == 8:
            return "Grate"
        elif self.number == 9:
            return "Pool"
        elif self.number == 10:
            return "Magic Cirle"
        elif self.number == 11:
            return "Trapdoor"
        elif self.number == 12:
            return "Throne"

#SECRET DOORS AND HIDDEN TREASURES

    def secret_doors_table(self, n):
        #receive one D12 value

        self.number = n
        if self.number == 1:
            return "The GM may draw 1 doungen counter (see the Gamemaster section)"
        elif self.number >1 and self.number <=6:
            return "There is no secret door in this wall section"
        elif self.number > 6 and self.number <=12:
            return "The Hero finds a secret door and may place it wherever he likes in the section of wall he was searching."

    def hidden_treasure_table(self, n):
        """receive one 2D12 value"""
        self.number = n
        if self.number >= 2 and self.number <= 6:
            return "The GM may draw 1 doungen counter (see the Gamemaster section)"
        elif self.number >6 and self.number <=16:
            return "There is no hidden treasure door in this room"
        elif self.number > 17 and self.number <=23:
            return "The Hero finds a cache of hidden treasure - roll a dice and multiply the score by five to find the value of the treasure in gold crown."
        elif self.number == 24:
            return "The Hero finds a cache of hidden treasure - roll two dice and consut the Magic Treasure Table in the Treasure Section"


#TRAPS AND TREASURES





HQA = Heroquest_Advanced_Modules()
HQA.random_numbers("2D12")
print(HQA.passages_lenght_table(HQA.random_numbers('D12')))
print(HQA.passages_features_table(HQA.random_numbers('2D12')))
print(HQA.passages_end_table(HQA.random_numbers('2D12')))
print(HQA.room_type_table(HQA.random_numbers('D12')))
print(HQA.hazard_table(HQA.random_numbers('D12')))
print(HQA.secret_doors_table(HQA.random_numbers('D12')))
print(HQA.hidden_treasure_table(HQA.random_numbers('2D12')))



