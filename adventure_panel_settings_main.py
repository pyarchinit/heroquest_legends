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

MAIN_DIALOG_CLASS, _ = loadUiType(os.path.join(os.path.dirname(__file__), 'adventures_panel_settings.ui'))


class AdventurePanelSettings(QDialog, MAIN_DIALOG_CLASS):
    TYPE_ORDER = ""
    DICT = ""

    def __init__(self, parent=None, db=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        #self.ITEMS = []
        #self.insertItems()


    def closeEvent(self, event):
        QDialog.closeEvent(self, event)


    def on_pushButtonRight_pressed(self):
        pass
        """
        all_items = []

        for index in range(self.FieldsList.count()):
            all_items.append(self.FieldsList.item(index).text())

        item_selected = self.FieldsList.selectedItems()

        all_items.remove(item_selected[0].text())
        try:
            all_items.remove('')
        except:
            pass
        self.FieldListsort.addItem(item_selected[0].text())

        self.FieldsList.clear()

        for item in all_items:
            self.FieldsList.addItem(item)
        """

    def on_pushButtonLeft_pressed(self):
        pass
        """
        all_items = []

        for index in range(self.FieldListsort.count()):
            all_items.append(self.FieldListsort.item(index).text())

        item_selected = self.FieldListsort.selectedItems()
        try:
            all_items.remove(item_selected[0].text())
        except:
            pass
        self.FieldsList.addItem(item_selected[0].text())

        self.FieldListsort.clear()

        if len(all_items) > 0:
            for item in all_items:
                self.FieldListsort.addItem(item)
        """

    def insertItems(self):
        the_missions_dict = self.DICT['missions_dict']
        key_list = []
        for k in the_missions_dict.keys():
            key_list.append(str(k))

        self.comboBox_id.addItems(key_list)



        """"
        self.delegate_fornitures = ComboBoxDelegate()
        self.delegate_fornitures.def_values(values_fornitures)
        self.delegate_fornitures.def_editable('False')
        self.tableWidget_fornitures.setItemDelegateForColumn(1,self.delegate_fornitures)
        self.tableWidget_fornitures.insertRow(0)
        #self.FieldsList.insertItems(0, lv)
        """

    def on_pushButton_charge_adventure_pressed(self):
        mission_number = int(self.comboBox_id.currentText())
        the_missions = self.DICT['missions_dict'][mission_number]
        the_title = the_missions[0]
        description = the_missions[1]
        the_fornitures_list = []
        the_fornitures_dict = self.DICT['forniture_name_conversion_dict'].keys()

        for i in self.DICT['forniture_name_conversion_dict'].keys():
            the_fornitures_list.append(i)

        print(str(the_fornitures_list))

        special_room = self.DICT['specials_rooms'][mission_number]
        print(str(special_room))
        room_description = special_room[1]
        room_fornitures_list = special_room[0]

        self.lineEdit_adventure_title.setText(str(the_title))
        self.textEdit_lamissione.setText(str(description))
        self.textEdit_the_final_room.setText(str(room_description))

        self.delegateRS = ComboBoxDelegate()
        values_fornitures = ["tavolo", "sedia", "cesso"]
        self.delegateRS.def_values(values_fornitures)
        self.delegateRS.def_editable('False')
        self.tableWidget_fornitures.setItemDelegateForColumn(1, self.delegateRS)

        elenco = [["1","tavolo"], ["2","sedia"], ["3","cesso"]]

        self.tableInsertData("self.tableWidget_fornitures",the_fornitures_list)

    def tableInsertData(self, t, d):
        """Set the value into alls Grid"""
        self.table_name = t
        print("table_insert 0")
        self.data_list = d
        self.data_list.sort()
        print("table_insert 1")
        # column table count
        table_col_count_cmd = "{}.columnCount()".format(self.table_name)
        table_col_count = eval(table_col_count_cmd)
        print("table_insert 2")
        # clear table
        table_clear_cmd = "{}.clearContents()".format(self.table_name)
        eval(table_clear_cmd)
        for i in range(table_col_count):
            print("table_insert 3")
            table_rem_row_cmd = "{}.removeRow(int({}))".format(self.table_name, i)
            print("table_insert 4")
            eval(table_rem_row_cmd)
        for row in range(len(self.data_list)):
            cmd = '{}.insertRow(int({}))'.format(self.table_name, row)
            eval(cmd)
            for col in range(len(self.data_list[row])):
                print("table_insert 4.3")
                exec_str = '{}.setItem(int({}),int({}),QTableWidgetItem(self.data_list[row][col]))'.format(self.table_name, row, col)
                print("table_insert 4.4")
                eval(exec_str)
                print("table_insert 4.5")
        max_row_num = len(self.data_list)
        print("table_insert 5")
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
