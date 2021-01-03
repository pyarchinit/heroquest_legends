# -*- coding: utf-8 -*-
"""
/***************************************************************************
        Heroquest Solo by Mandor the Druid
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

from heroquest_solo_main import Heroquest_solo
import PySimpleGUI as sg
HQ_SOLO = Heroquest_solo() #app CLASS to call method
#default theme
sg.theme('DefaultNoMoreNagging')
# ------ Menu Definition ------ #
menu_def = [['&File', ['&Open', '&Save', 'E&xit', 'Properties']],
            ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Help', '&About...'], ]
#layout
layout = [[sg.Menu(menu_def, tearoff=True)],
          [sg.Frame(layout=[
              [sg.Button("Come è fatto il corridoio", key = "_AISLES_"),
               sg.Multiline('', key = "_AISLES_TEXT_", size=(60,6))]],
               title='Esplora un nuovo corridoio')],

          [sg.Frame(layout=[
               [sg.Button("Scopri come è fatta la stanza", key="_ROOM_GENERATOR_"),
                sg.Text('Inserisci il numero di caselle della stanza (minimo 6)'),
                sg.Input('6', key="_ROOM_GENERATOR_NUMBER_", size=(5, 3))],
               [sg.Multiline('', key="_ROOM_GENERATOR_TEXT_", size=(60, 3))]],
               title='Esplora una nuova Stanza')],

          [sg.Frame(layout=[
              [sg.Button("Ci sono tesori?", key="_TREASURES_"), sg.Multiline('', key = "_TREASURES_TEXT_", size=(60,3))],
              [sg.Button("Cosa contiene?", key="_CHEST_"), sg.Multiline('', key="_CHEST_TEXT_", size=(60, 6))]],
                title='Esplora la stanza e i suoi mobili')],

              [sg.Button("Ci sono mostri nella stanza?", key="_MONSTERS_GENERATOR_"),sg.Multiline('', key="_MONSTERS_GENERATOR_TEXT_", size=(60, 3)), sg.Image(r'.\\images\\orco.png', key='-IMAGE-')],
              [sg.Button("Ci sono trabocchetti o porte segrete?", key="_TRAPS_SECRET_")],
              [sg.Multiline('', key="_TRAPS_TEXT_", size=(60, 3)), sg.Multiline('', key="_SECRET_DOOR_TEXT_", size=(60, 3))],

    ]
# Create the window
window = sg.Window("Heroquest solo assistant - by Mandor The Druid-version 0.01 beta", layout,  margins=(10, 10))
# Create an event loop
while True:
    event, values = window.read()

    if event == "_AISLES_":
        msg = HQ_SOLO.aisles(HQ_SOLO.random_numbers())
        window["_AISLES_TEXT_"].update(str(msg))

    if event == "_TREASURES_":
        msg = HQ_SOLO.treasures(HQ_SOLO.random_numbers())
        window["_TREASURES_TEXT_"].update(str(''))
        window["_TREASURES_TEXT_"].update(str(msg))

    if event == "_CHEST_":
        msg = HQ_SOLO.chest(HQ_SOLO.random_numbers())
        window["_CHEST_TEXT_"].update("")
        window["_CHEST_TEXT_"].update(str(msg))

    if event == "_TRAPS_SECRET_":
        msg_traps = HQ_SOLO.traps(HQ_SOLO.random_numbers())
        msg_secret_door = HQ_SOLO.secret_doors(HQ_SOLO.random_numbers())
        window["_TRAPS_TEXT_"].update(str(msg_traps))
        window["_SECRET_DOOR_TEXT_"].update(str(msg_secret_door))


    if event == "_ROOM_GENERATOR_":
        msg = HQ_SOLO.room_generator(HQ_SOLO.random_numbers(), window["_ROOM_GENERATOR_NUMBER_"].get())
        window["_ROOM_GENERATOR_TEXT_"].update(str(msg))


    if event == "_MONSTERS_GENERATOR_":
        msg = HQ_SOLO.monsters_generator(HQ_SOLO.random_numbers(), window["_ROOM_GENERATOR_NUMBER_"].get())
        window["_MONSTERS_GENERATOR_TEXT_"].update(str(msg))
        window["-IMAGE-"].update(r'.\\images\\goblin.png')


    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()