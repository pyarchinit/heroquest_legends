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
#from PySide2.QtWidgets import *
#import PySimpleGUIQt as sg
HQ_SOLO = Heroquest_solo() #app CLASS to call method
#default theme
sg.theme('DefaultNoMoreNagging')
# ------ Menu Definition ------ #
menu_def = [['&File', ['&Open', '&Save', 'E&xit', 'Properties']],
            ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Help', '&About...'], ]
#layout

left_column = [[sg.Text('', size=(20, 2), justification='center',font=("Helvetica", 12), relief=sg.RELIEF_RIDGE)],
             [sg.Text(HQ_SOLO.CONFIG_DICT['TXT_4']), sg.Text("1", key = "-TEXT_4-", )],
             [sg.Button(HQ_SOLO.CONFIG_DICT['btn_7'], key = "-RESET_ALL-")],
             [sg.Frame(layout=[
              [sg.Button(HQ_SOLO.CONFIG_DICT['btn_1'], key = "-AISLES-"),
               sg.Multiline('', key = "-AISLES_TEXT-", size=(60,6))]],
               title=HQ_SOLO.CONFIG_DICT['FIELD_BOX_1'])]]

layout = [
    [sg.Menu(menu_def, tearoff=True)],
             [sg.Column(left_column,element_justification='c')],

             [sg.Frame(layout=[
               [sg.Button(HQ_SOLO.CONFIG_DICT['btn_2'], key="-ROOM_GENERATOR-"),
                sg.Text(HQ_SOLO.CONFIG_DICT['TXT_1']),
                sg.Input('6', key="-ROOM_GENERATOR_NUMBER-", size=(5, 3))],
               [sg.Multiline('', key="-ROOM_GENERATOR_TEXT-", size=(60, 3))]],

                 title=HQ_SOLO.CONFIG_DICT['TXT_1'])],#frame title

             [sg.Frame(layout=[
              [sg.Button(HQ_SOLO.CONFIG_DICT['btn_3'],
                         key="-TREASURES-"), sg.Multiline('', key = "-TREASURES_TEXT-", size=(60,3))],
              [sg.Button(HQ_SOLO.CONFIG_DICT['btn_4'], key="-CHEST-"),
               sg.Multiline('', key="-CHEST_TEXT-", size=(60, 6))]], title=HQ_SOLO.CONFIG_DICT['TXT_3'])],

              [sg.Button(HQ_SOLO.CONFIG_DICT['btn_5'], key="-MONSTERS_GENERATOR-"),sg.Multiline('', key="-MONSTERS_GENERATOR_TEXT-", size=(60, 3))],
              [sg.Button(HQ_SOLO.CONFIG_DICT['btn_6'], key="-TRAPS_SECRET-")],
              [sg.Multiline('', key="-TRAPS_TEXT-", size=(60, 3))],
              [sg.Multiline('', key="-SECRET_DOOR_TEXT-", size=(60, 3))],
              #sg.Image(r'.\\images\\orco.png', key='-IMAGE-')
                ]




def main():
# Create the window
    window = sg.Window("Heroquest solo assistant - by Mandor The Druid-version 0.004 beta", layout) #margins=(10, 10)
    # Create an event loop
    while True:
        event, values = window.read()

        if event == "-RESET_ALL-":
            window["-CHEST_TEXT-"].update("")
            window["-TRAPS_TEXT-"].update("")
            window["-SECRET_DOOR_TEXT-"].update("")
            window["-AISLES_TEXT-"].update("")
            window["-ROOM_GENERATOR_TEXT-"].update("")
            window["-MONSTERS_GENERATOR_TEXT-"].update("")
            window["-TREASURES_TEXT-"].update(str(''))
            current_turn = int(window["-TEXT_4-"].get())
            netx_turn = current_turn+1
            window["-TEXT_4-"].update(str(netx_turn))

        if event == "-AISLES-":
            current_turn = int(window["-TEXT_4-"].get())

            if current_turn == 1 or current_turn == 2:
                msg_num = HQ_SOLO.random_numbers()
                while(msg_num) >= 21:
                    msg_num = HQ_SOLO.random_numbers() #return always door at first and second turn
                msg = HQ_SOLO.aisles(msg_num)
            else:
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
            current_turn = int(window["-TEXT_4-"].get())

            if current_turn == 1 or current_turn == 2:
                msg_num = HQ_SOLO.random_numbers()
                while(msg_num) >= 14:
                    msg_num = HQ_SOLO.random_numbers() #return always door at first and second turn
                msg = HQ_SOLO.room_generator(msg_num, window["-ROOM_GENERATOR_NUMBER-"].get())
                if not msg.__contains__('port'):
                    msg = '{} Colloca anche una porta chiusa verso un corridio inesplorato.'.format(msg)

            elif current_turn == 3:
                msg_num = HQ_SOLO.random_numbers()
                msg_temp = HQ_SOLO.room_generator(msg_num, window["-ROOM_GENERATOR_NUMBER-"].get())
                msg = '{} Colloca anche una porta chiusa verso il corridio.'.format(msg_temp)
            else:
                msg = HQ_SOLO.room_generator(HQ_SOLO.random_numbers(), window["-ROOM_GENERATOR_NUMBER-"].get())
            window["-ROOM_GENERATOR_TEXT-"].update(str(msg))

        if event == "-MONSTERS_GENERATOR-":
            msg = HQ_SOLO.monsters_generator(HQ_SOLO.random_numbers(), window["-ROOM_GENERATOR_NUMBER-"].get())
            window["-MONSTERS_GENERATOR_TEXT-"].update(str(msg))
            # window["-IMAGE-"].update(r'.\\images\\goblin.png')


        if event == "OK" or event == sg.WIN_CLOSED:
            break


if __name__ == '__main__':
    main()