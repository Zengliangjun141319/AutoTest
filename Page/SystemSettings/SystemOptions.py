# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     SystemOptions.py
   Author :        曾良均
   QQ:             277099728
   Date：          7/18/2022 2:01 PM   
   Description :
-------------------------------------------------
   Change Activity:
                   
-------------------------------------------------
"""
__author__ = 'ljzeng'

from operater import Operater
from Page.comms import *


class SystemOptions(Operater):
    # 系统设置页面元素
    # 左侧菜单
    settingsMenu_loc = ('id', 'button_menu')
    systemsettings_loc = ('id', 'lisyssetting')
    exButton_loc = ('id', 'nav_arrow')

    sysOption_loc = ('xpath', '//*[@id="nav_systemoptions"]/a/span')

    iframe_loc = ('xpath', '//*[@id="set_right"]/iframe')
    unitOdo_loc = ('id', 'txtOdoUnit')

    saveBtn = ('xpath', '//*[@id="content1"]/div[1]/div[@class="function_title"]/span[@class="sbutton iconsave"]')
    SaveOK = ('xpath', ok_btn)