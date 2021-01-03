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

import os
#import traceback
#import sys
from builtins import object
#from qgis.PyQt.QtWidgets import *
#from qgis.core import QgsMessageLog, Qgis, QgsSettings
#from .pyarchinit_OS_utility import Pyarchinit_OS_Utility


class Settings(object):

    #MESSAGES DICT
    AISLES_MESSAGES = ""

    #OTHER MESSAGES DICT
    
    conf = open('config.cfg', "rb+")

    data = conf.read()

    conf.close()

    def __init__(self, s):

        self.configuration = eval(s)

    def set_configuration(self):

        self.AISLES_MESSAGES = self.configuration['AISLES']
        """
        self.HOST = self.configuration['HOST']
        self.DATABASE = self.configuration['DATABASE']
        self.PASSWORD = self.configuration['PASSWORD']
        self.PORT = self.configuration['PORT']
        self.USER = self.configuration['USER']
        self.THUMB_PATH = self.configuration['THUMB_PATH']
        self.THUMB_RESIZE = self.configuration['THUMB_RESIZE']
        self.SITE_SET = self.configuration['SITE_SET']
        PLUGIN_PATH = path = os.path.dirname(__file__)
        """
