# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ManageRegions.py
   Description :    Region管理功能测试
        1、 新建Region
        2、 编辑Region
        3、 删除Region
   Author :        曾良均
   QQ:             277099728
   Date：          1/13/2022 2:42 PM
-------------------------------------------------
   Change Activity:
                   1/13/2022:
-------------------------------------------------
"""
__author__ = 'ljzeng'

from Common.operater import Operater

class ManageRegions(Operater):
    # 定义元素位置
    # 左侧菜单
    settingsMenu_loc = ('id', 'button_menu')
    systemsettings_loc = ('id', 'lisyssetting')

    # 系统设置菜单项
    manageregion_loc = ('id', 'nav_regions')

    # 右边内容
    iframe_loc = ('xpath', '//*[@id="set_right"]/iframe')

    #  顶层功能按钮
    addBtn_loc = ('xpath', '//*[@id="recordcontent"]/div[@class="function_title"]/span[@class="sbutton iconadd"]')
    refresh_loc = ('xpath', '//*[@id="recordcontent"]/div[@class="function_title"]/span[@class="sbutton iconrefresh"]')

    # 添加界面
    regionname_loc = ('id', 'dialog_name')
    startdate_loc = ('id', 'dialog_startdate')
    projectdate_loc = ('id', 'dialog_projectenddate')
    enddate_loc = ('id', 'dialog_enddate')
    notes_loc = ('id', 'dialog_notes')

    okBtn = ('xpath', '//*[@id="dialog_region"]/div[@class="dialog-func"]/input[@value="OK"]')
    cancelBtn = ('xpath', '//*[@id="dialog_region"]/div[@class="dialog-func"]/input[@value="Cancel"]')

    # 添加不符合时弹出窗口
    tipmessage_loc = ('xpath', '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-content"]/div')
    tipOK_loc = ('xpath', '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input')


    # 列表功能按钮
    result1Edit_loc = ('xpath', '//*[@id="regionlist"]/div/div[1]/div/table/tbody/tr/td[6]/a')
    result1Del_loc = ('xpath', '//*[@id="regionlist"]/div/div[1]/div/table/tbody/tr/td[7]/a')

    # 删除提示
    delOK_loc = ('xpath', '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input[@value="Yes"]')