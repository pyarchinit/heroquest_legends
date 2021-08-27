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
        #print(str('gigio'))

        res = self.CURSOR.execute("SELECT DISTINCT(tipe_forniture) FROM fornitures")
        fornitures_values = res.fetchall()
        for i in fornitures_values:
            forniture_converted = self.DICT['forniture_name_conversion_dict']
            the_fornitures_list.append(forniture_converted[i[0]])


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

        #print("puccia")
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
            print(str(self.DICT['forniture_name_conversion_dict']))
            forniture_converted = self.DICT['forniture_name_conversion_dict'][res_charged[1]]

            forniture = [str(i), forniture_converted]

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

    def insert_new_row(self, table_name):
        """insert new row into a table based on table_name"""
        cmd = table_name + ".insertRow(0)"
        eval(cmd)

    def remove_row(self, table_name):
        try:
            """insert new row into a table based on table_name"""
            table_row_count_cmd = ("%s.rowCount()") % (table_name)
            table_row_count = eval(table_row_count_cmd)
            rowSelected_cmd = ("%s.selectedIndexes()") % (table_name)
            rowSelected = eval(rowSelected_cmd)
            rowIndex = (rowSelected[0].row())
            cmd = ("%s.removeRow(%d)") % (table_name, rowIndex)
            eval(cmd)
        except:
            pass

    def empty_fields(self):
        fornitures_row_count = self.tableWidget_fornitures.rowCount()
        monsters_row_count = self.tableWidget_monsters_type.rowCount()

        self.lineEdit_adventure_title.clear()
        self.textEdit_the_mission.clear()
        self.textEdit_the_final_room.clear()

        #self.comboBox_sito.setEditText("")  # 1 - Sito

        for i in range(fornitures_row_count):
            self.tableWidget_fornitures.removeRow(0)
        self.insert_new_row("self.tableWidget_fornitures")

        for i in range(monsters_row_count):
            self.tableWidget_monsters_type.removeRow(0)
        self.insert_new_row("self.tableWidget_monsters_type")

    def on_pushButton_insert_row_fornitures_pressed(self):
        self.insert_new_row('self.tableWidget_fornitures')


    def on_pushButton_remove_row_fornitures_pressed(self):
        self.remove_row('self.tableWidget_fornitures')


    def on_pushButton_insert_row_monster_pressed(self):
        self.insert_new_row('self.tableWidget_monsters_type')


    def on_pushButton_remove_row_monster_pressed(self):
        self.remove_row('self.tableWidget_monsters_type')



    def on_pushButton_create_pressed(self):
        self.empty_fields()



if __name__ == '__main__':
    import sys

    a = QApplication(sys.argv)
    dlg = AdventurePanelSettings()
    dlg.show()
    sys.exit(a.exec_())
