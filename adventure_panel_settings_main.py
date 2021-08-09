#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
/***************************************************************************
        Heroquest's Legends Solo by Mandor the Druid
                             -------------------
    begin                : 2021-01-02
    copyright            : (C) 2021 by Luca Mandolesi
    email                : mandoluca at gmail.com
    version              : 0.92 ALPHA
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
from __future__ import absolute_import


from builtins import range
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QTableWidgetItem
from PyQt5.uic import loadUiType
from delegateComboBox import ComboBoxDelegate
import os
import sqlite3


MAIN_DIALOG_CLASS, _ = loadUiType(os.path.join(os.path.dirname(__file__), 'adventures_panel_settings.ui'))


class AdventurePanelSettings(QDialog, MAIN_DIALOG_CLASS):
    TYPE_ORDER = ""
    DICT = ""
    CONNECTION = sqlite3.connect('./db_heroquest_legends.sqlite')
    CURSOR = CONNECTION.cursor()

    def __init__(self, parent=None, db=None):
        QDialog.__init__(self, parent)

        self.setupUi(self)


    def closeEvent(self, event):
        QDialog.closeEvent(self, event)

    def insertItems(self):
        the_missions_dict = self.DICT['missions_dict']
        key_list = []
        for k in the_missions_dict.keys():
            key_list.append(str(k))

        self.comboBox_id.addItems(key_list)


    def customize_gui(self):
        the_fornitures_list = []
        print(str('gigio'))

        res = self.CURSOR.execute("SELECT DISTINCT(tipe_forniture) FROM fornitures")
        fornitures_values = res.fetchall()
        for i in fornitures_values:
            the_fornitures_list.append(i[0])
        print(str(the_fornitures_list))

        self.delegateFornitures = ComboBoxDelegate()
        self.delegateFornitures.def_values(the_fornitures_list)
        self.delegateFornitures.def_editable('False')
        self.tableWidget_fornitures.setItemDelegateForColumn(1, self.delegateFornitures)

        the_monster_types_list = self.DICT['monster_types']

        self.delegateMT = ComboBoxDelegate()
        values_monsters_types = the_monster_types_list
        self.delegateMT.def_values(values_monsters_types)
        self.delegateMT.def_editable('False')
        self.tableWidget_monsters_type.setItemDelegateForColumn(0, self.delegateMT)


    def on_pushButton_charge_adventure_pressed(self):
        mission_number = int(self.comboBox_id.currentText())
        the_missions = self.DICT['missions_dict'][mission_number]
        the_title = the_missions[0]
        description = the_missions[1]

        special_room = self.DICT['specials_rooms'][mission_number]
        room_description = special_room[1]
        room_fornitures_list = special_room[0]

        print("puccia")
        #GUI
        self.lineEdit_adventure_title.setText(str(the_title))
        self.textEdit_the_mission.setText(str(description))
        self.textEdit_the_final_room.setText(str(room_description))


        class_monsters_list = self.from_list_to_listoflist(self.DICT['monster_class'][mission_number])

        #print(str(class_monsters_list))
        self.tableInsertData("self.tableWidget_monsters_type", class_monsters_list)

        #type_special_room_fornitures_list = self.from_list_to_listoflist(self.DICT['specials_rooms'][mission_number][0])

        special_room_fornitures_list = self.DICT['specials_rooms'][mission_number][0]
        special_room_fornitures_list_charge = []

        # charge the total of forniture linked to ID

        #FORNITURES_QTY_DICT = {1: db_fornitures_charged[0][2],
        for i in special_room_fornitures_list:
            res = self.CURSOR.execute("SELECT * FROM fornitures WHERE id_forniture = '{}'".format(str(i)))
            #print(str(paolo))
            res_charged = res.fetchone()
            forniture = [str(i), res_charged[1]]

            special_room_fornitures_list_charge.append(forniture)

        self.tableInsertData("self.tableWidget_fornitures", special_room_fornitures_list_charge)


        self.customize_gui()

    def from_list_to_listoflist(self,l):
        self.list = l
        list_of_lists = []

        for i in  self.list:
            list_of_lists.append([i])

        return list_of_lists


    def tableInsertData(self, t, d):
        """Set the value into alls Grid"""
        self.table_name = t

        self.data_list = d
        self.data_list.sort()
        # column table count
        table_col_count_cmd = "{}.columnCount()".format(self.table_name)
        table_col_count = eval(table_col_count_cmd)
        # clear table
        table_clear_cmd = "{}.clearContents()".format(self.table_name)
        eval(table_clear_cmd)
        for i in range(table_col_count):
            table_rem_row_cmd = "{}.removeRow(int({}))".format(self.table_name, i)
            eval(table_rem_row_cmd)
        for row in range(len(self.data_list)):
            cmd = '{}.insertRow(int({}))'.format(self.table_name, row)
            eval(cmd)
            for col in range(len(self.data_list[row])):
                exec_str = '{}.setItem(int({}),int({}),QTableWidgetItem(self.data_list[row][col]))'.format(self.table_name, row, col)
                eval(exec_str)
        max_row_num = len(self.data_list)
        value = eval(self.table_name+".item(max_row_num,1)")
        if value == '':
            cmd = ("%s.removeRow(%d)") % (self.table_name, max_row_num)
            eval(cmd)



if __name__ == '__main__':
    import sys

    a = QApplication(sys.argv)
    dlg = AdventurePanelSettings()
    dlg.show()
    sys.exit(a.exec_())
