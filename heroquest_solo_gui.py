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
#import PySimpleGUIWeb as sg#
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
              [sg.Button("Come è fatto il corridoio", key = "-AISLES-"),
               sg.Multiline('', key = "-AISLES_TEXT-", size=(60,6))]],
               title='Esplora un nuovo corridoio')],

          [sg.Frame(layout=[
               [sg.Button("Scopri come è fatta la stanza", key="-ROOM_GENERATOR-"),
                sg.Text('Inserisci il numero di caselle della stanza (minimo 6)'),
                sg.Input('6', key="-ROOM_GENERATOR_NUMBER-", size=(5, 3))],
               [sg.Multiline('', key="-ROOM_GENERATOR_TEXT-", size=(60, 3))]],
               title='Esplora una nuova Stanza')],

          [sg.Frame(layout=[
              [sg.Button("Ci sono tesori?", key="-TREASURES-"), sg.Multiline('', key = "-TREASURES_TEXT-", size=(60,3))],
              [sg.Button("Cosa contiene?", key="-CHEST-"), sg.Multiline('', key="-CHEST_TEXT-", size=(60, 6))]],
                title='Esplora la stanza e i suoi mobili')],

              [sg.Button("Ci sono mostri nella stanza?", key="-MONSTERS_GENERATOR-"),sg.Multiline('', key="-MONSTERS_GENERATOR_TEXT-", size=(60, 3))],
              [sg.Button("Ci sono trabocchetti o porte segrete?", key="-TRAPS_SECRET-")],
              [sg.Multiline('', key="-TRAPS_TEXT-", size=(60, 3)), sg.Multiline('', key="-SECRET_DOOR_TEXT-", size=(60, 3))],
              #sg.Image(r'.\\images\\orco.png', key='-IMAGE-')
    ]



# Create the window
window = sg.Window("Heroquest solo assistant - by Mandor The Druid-version 0.004 beta", layout,  margins=(10, 10))
# Create an event loop
while True:
    event, values = window.read()
    window.back

    if event == "-AISLES-":
        msg = HQ_SOLO.aisles(HQ_SOLO.random_numbers())
        window["-AISLES_TEXT-"].update("")
        window["-AISLES_TEXT-"].update(str(msg))

    if event == "-TREASURES-":
        msg = HQ_SOLO.treasures(HQ_SOLO.random_numbers())
        window["-TREASURES_TEXT-"].update(str(''))
        window["-TREASURES_TEXT-"].update(str(msg))

    if event == "-CHEST-":
        msg = HQ_SOLO.chest(HQ_SOLO.random_numbers())
        window["-CHEST_TEXT-"].update("")
        window["-CHEST_TEXT-"].update(str(msg))

    if event == "-TRAPS_SECRET-":
        msg_traps = HQ_SOLO.traps(HQ_SOLO.random_numbers())
        msg_secret_door = HQ_SOLO.secret_doors(HQ_SOLO.random_numbers())
        window["-TRAPS_TEXT-"].update(str(msg_traps))
        window["-SECRET_DOOR_TEXT-"].update(str(msg_secret_door))


    if event == "-ROOM_GENERATOR-":
        msg = HQ_SOLO.room_generator(HQ_SOLO.random_numbers(), window["-ROOM_GENERATOR_NUMBER-"].get())
        window["-ROOM_GENERATOR_TEXT-"].update(str(msg))


    if event == "-MONSTERS_GENERATOR-":
        msg = HQ_SOLO.monsters_generator(HQ_SOLO.random_numbers(), window["-ROOM_GENERATOR_NUMBER-"].get())
        window["-MONSTERS_GENERATOR_TEXT-"].update(str(msg))
        #window["-IMAGE-"].update(r'.\\images\\goblin.png')


    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()