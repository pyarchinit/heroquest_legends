import random


class Heroquest_solo:
    """main class for variables management"""
    def __init__(self):
        self.r_num = random

        #position dict
        self.LR_dict = {1: 'a sinistra',
                        2: 'a destra',
                        3: 'al centro',
                        4: 'sul fondo',
                        5: 'davanti a te'}

        #fornutures dict
        self.forniture_dict = {1: "armadio",
                               2: "porta chiusa",
                               3: "libreria",
                               4: "porta chiusa",
                               5: "porta chiusa",
                               6: "porta aperta",
                               7: "porta aperta",
                               8: "scrigno",
                               9: "tesoro",
                               10: "caminetto",
                               11: "trono",
                               12: "rastrelliera",
                               13: "tomba",
                               14: "porta chiusa",
                               15: "porta aperta",
                               16: "porta aperta",
                               17: "bancone del mago",
                               18: "tavolo di tortura",
                               19: "tavolo",
                               20: "tavolo",
                               21: "tavolo",
                               22: "porta aperta",
                               23: "porta chiusa",
                               24: "porta aperta",
                               25: "libreria",
                               26: "porta aperta",
                               27: "bancone del mago",
                               28: "tavolo di tortura",
                               29: "scrigno",
                               30: "tavolo",
                               31: "scrigno",
                               32: "porta aperta",
                               33: "porta chiusa",
                               34: "porta aperta",
                               35: "libreria"}

        #items dict that you can find inside a cest or in other forniture
        self.tresures_dict = {1: "Pozione di cura",
                              2: "Pozione di velocità",
                              3: "Pozione di attacco",
                              4: "Pozione di difesa",
                              5: "Spada",
                              6: "Pozione di cura",
                              7: "Lancia",
                              8: "Pozione di difesa",
                              9: "Scudo",
                              10 : "balestra",
                              11: "Pozione di attacco",
                              12: "Pozione di difesa",
                              13: "Spada",
                              14: "Spadino",
                              15: "Lancia",
                              16: "Pozione di difesa",
                              17: "Pozione di attacco",
                              18: "Balestra",
                              19: "Pozione di difesa",
                              20: "Pozione di attacco"}

        self.monsters_dict = {1: "un Goblin",
                              2: "un Orco",
                              3: "un Fimir",
                              4: "due Goblin",
                              5: "due Orchi",
                              6: "due Fimir",
                              7: "tre Goblin",
                              8: "tre Orchi",
                              9: "tre Fimir",
                              10: "uno Scheletro",
                              11:  "uno Zombie",
                              12:  "una Mummia",
                              13: "due Scheletri",
                              14: "due Zombie",
                              15: "tre Scheletri",
                              16: "tre Mummie",
                              17: "tre Zombie",
                              18: "un Guerriero del Caos",
                              19: "due Guerrieri del Caos",
                              20: "tre Guerrieri del Caos",
                              21: "Un Gargoyle"}





    def random_numbers(self):
        """ a random number generator based on four D6.
        A simple statistic to understand the probability of success
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
        value_1 = self.r_num.randrange(1, 6)
        value_2 = self.r_num.randrange(1, 6)
        value_3 = self.r_num.randrange(1, 6)
        value_4 = self.r_num.randrange(1, 6)

        rn_list = [value_1, value_2, value_3, value_4]

        rn_sum = sum(rn_list)
        return rn_sum #return values between 4 and 24

    def aisles(self, rv):
        #sistem for discover aisles

        self.rv = rv #recive a random number beetween 4 and 24 for number of doors
        self.LR_n = self.r_num.randrange(1, 2) #select beetween

        rock_msg_value = self.random_numbers()
        print(rock_msg_value)
        if rock_msg_value > 0 and rock_msg_value <= 13:
            rocks_msg = "Dal fondo del corridoio arriva una luce fioca, forse troverai altre stanze?"
        elif rock_msg_value > 13 and rock_msg_value <= 16:
            rocks_msg = "Il soffitto è crollato e il corridoio è bloccato dopo la porta. O tornare indietro o entrare. Che cosa ti dice di fare l'istinto?"
        else:
            wander_monster_list = [1, 2, 3, 7, 8, 9, 13]
            rocks_msg = "Il soffitto è crollato e il corridoio è bloccato dopo la porta. Dul buio del corridoio arriva un rumore sinistro: sulla tua strada trovi {}".format(
                self.monsters_dict[ wander_monster_list[self.r_num.randrange(1, len(wander_monster_list))]])

        if self.rv > 1 and self.rv <= 10:

            return "Hai trovato una porta a " + self.LR_dict[self.LR_n] + ". Colloca una porta nella prima stanza. " + rocks_msg

        elif self.rv > 10 and self.rv <= 15:

            return "Hai trovato due porte. Una prima porta a {} e una seconda porta a {}. Ognuna ti conduce ad una stanza diversa. ".format(self.LR_dict[self.r_num.randrange(1, 2)], self.LR_dict[self.r_num.randrange(1, 2)]) + rocks_msg

        elif self.rv > 15 and self.rv <= 20:
            return "Hai trovato tre porte. Colloca una prima porta a {}, una seconda porta a {} e una terza porta a {}. Ognuna ti conduce ad una stanza diversa. ".format(self.LR_dict[self.r_num.randrange(1, 2)], self.LR_dict[self.r_num.randrange(1, 2)], self.LR_dict[self.r_num.randrange(1, 2)]) + rocks_msg
        else:
            return ": Non hai trovato nessuna porta"

    def thresures(self, rv):
        self.rv = rv

        if self.rv > 1 and self.rv <= 11:
            return "Non hai trovato nulla. Pesca una carta dal mazzo dei Tesori"

        elif self.rv > 11 and self.rv <= 17:
            return "Finalmente un tesoro. Scopri cosa contiene"

        elif self.rv > 17:
            return """Mentre cerchi tra vecchi stracci e ossa di sorcio, senti uno scatto: un dardo di colpisce e perdi 1 punto corpo"""
        else:
            return "Non hai trovato nulla. Pesca una carta dal mazzo dei Tesori"

    def chest(self, rv):
        """"create a random threasures inside chest"""
        self.rv = rv

        if self.rv > 1 and self.rv <= 15:
            items_list = []
            items_numbers = self.r_num.randrange(1, 3)
            for i in range(items_numbers):
                items_list.append(self.tresures_dict[self.r_num.randrange(1, 8)])

            items_list_str = "Hai trovato un tesoro con dentro:\n{}".format('\n'.join(items_list))

            return items_list_str

        elif self.rv > 15 and self.rv <= 20:
            msg = "Hai trovato {} monete d'oro".format(self.r_num.randrange(1, 500, 25)-1)
            return msg
        else:
            return """Putroppo hai fatto scattare un trabocchetto. Se provare a disinnescarlo tirando un dado da combattimento: 
            Con 1 scudo bianco non ti succede nulla e puoi ritentare la sorte;
            Con 1 scudo nero non ti succede nulla;
            Con 1 teschio perdi 1 punto corpo."""

    def secret_doors(self, rv):
        """Create random doors for aisles"""
        self.rv = rv
        self.LR_n = self.r_num.randrange(1, 2)

        if self.rv <= 13:
            return "Non hai trovato nessuna porta segreta."
        elif self.rv > 14 and self.rv <= 24:
            value_LR = self.r_num.randrange(1, 2)
            return "Hai trovato una porta segreta " + self.LR_dict[
                self.r_num.randrange(1, 2)] + ". Colloca una porta segreta nel muro a {}".format(self.LR_dict[self.r_num.randrange(1, 2)])
        else:
            return "Non hai trovato nessuna porta segreta."

    def traps(self, rv):
        """search for traps"""

        self.rv = rv

        if self.rv <= 13:
            return "Per fortuna non ci sono trabocchetti."
        elif self.rv > 14 and self.rv <= 24:
            return """Hai scovato un trabocchetto proprio davanti a te. Se vuoi sorpassarlo tira un dado da combattimento:
                        Con 1 scudo bianco passi indenne.
                        Con 1 scudo nero non riesci a passare.
                        Con 1 teschio cadi e perdi 1 punto corpo. Se sei caduto difendi con un dado in meno e uscirai solo facendo un valore superiore a 2"""
        else:
            return "Non ci sono trabocchetti."

    def room_generator(self, rv, room_dimension):
        """create random rooms with fornitures"""
        self.rv = rv #the values recives a number from 4D6
        self.room_dimension = int(room_dimension) #total of room's tiles
        forniture_number = 0

        if self.rv > 10:

            if self.room_dimension <= 6:
                forniture_number = 1
            elif self.room_dimension > 9 and self.room_dimension <= 16:
                forniture_number = self.r_num.randrange(1, 3)
            elif self.room_dimension > 16:
                forniture_number = self.r_num.randrange(1, 4)
            select_forniture_list = []

            for i in range(forniture_number):
                select_forniture_list.append(self.forniture_dict[self.r_num.randrange(1, 35)])

            msg_forniture = "La stanza contiene {}".format(", ".join(select_forniture_list))
            return msg_forniture

        else:
            return "Non c'è mobilio ma attento agli incantesimi!!!"


    def monsters_generator(self, rv, room_dimension):
        """create random monsters for rooms based on room dimension"""
        self.rv = rv
        self.room_dimension = int(room_dimension)
        self.LR_n = self.LR_dict[self.r_num.randrange(1, 5)]
        monsters_number = 0
        if self.rv > 10:
            if self.room_dimension <= 6:
                monsters_number = 1
            elif self.room_dimension > 9 and self.room_dimension <= 16:
                monsters_number = self.r_num.randrange(1, 3)
            elif self.room_dimension > 16:
                monsters_number = self.r_num.randrange(1, 4)
            select_monsters_list = []

            for i in range(monsters_number):
                select_monsters_list.append('{} {}'.format(self.monsters_dict[self.r_num.randrange(1, 21)], self.LR_dict[self.r_num.randrange(1, 5)]))

            msg_monsters = "Colloca {}".format(", ".join(select_monsters_list))
            return msg_monsters

        else:
            return "FIUUU... meno male. Nessun Mostro in vista!!!"





