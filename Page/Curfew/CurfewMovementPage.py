# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     CurfewMovementPage.py
   Author :        曾良均
   QQ:             277099728
   Date：          4/19/2023 10:59 AM   
   Description :
-------------------------------------------------
   Change Activity:
                   
-------------------------------------------------
"""
__author__ = 'ljzeng'
from operater import Operater
from Page.comms import *


class CurfewMovementPage(Operater):
    # 左侧菜单
    settingsBtn_loc = ('id', 'button_menu')
    curfewconmenu_loc = ('xpath', '//*[@id="menu_panel"]/ul/li[4]/a/span[text()="Curfew Configuration"]')

    # 收折按钮
    exBtn_loc = ('id', 'nav_arrow')
    curfewmov_loc = ('id', 'nav_curfewmt')

    # 右侧页面元素
    curfewFrame_loc = ('xpath', '//*[@id="set_right"]/iframe')
    savebtn_loc = ('xpath', '//*[@id="content1"]/div/div[@class="function_title"]/span[@class="sbutton iconsave"]')
    refresh_loc = ('xpath', '//*[@id="content1"]/div/div[@class="function_title"]/span[@class="sbutton iconrefresh"]')
    defaultTol_loc = ('id', 'dialog_defaulttolerance')

    firstcurfewvalue_loc = ('xpath', '//*[@id="tolerancelist"]/div/div/div/div/table/tr[1]/td[2]/content/span[2]')

    saveOK_loc = ('xpath', ok_btn)