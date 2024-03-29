# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     InspectionLayoutPage.py
   Description :
   Author :        曾良均
   QQ:             277099728
   Date：          1/26/2022 9:49 AM
-------------------------------------------------
   Change Activity:
                   1/26/2022:
-------------------------------------------------
"""
__author__ = 'ljzeng'

from operater import Operater
from Page.comms import *


class InspectionLayoutPage(Operater):
    # Layouts页面元素
    # 左侧滑块大图标
    inspection_loc = ('xpath', '//*[@id="divLeftTitle"]/div[@title="Inspection"]/div')

    # Inspection页面左侧菜单
    exButton_loc = ('xpath', '//*[@id="nav_arrow"]')  # 左边菜单收折按钮
    layoutsMu_loc = ('xpath', '//*[@id="set_left"]/ul/li[@title="Layouts"]/a/span')

    # 右侧页面
    searchInbox_loc = ('xpath', '//*[@id="set_right"]/div/div[1]/div[2]/input[@type="text"]')
    searchBt_loc = ('xpath', '//*[@id="set_right"]/div/div[1]/div[2]/input[@value="Search"]')

    addBtn_loc = ('xpath', '//*[@id="set_right"]/div/div[1]/div[@class="function_title"]/span[@class="sbutton iconadd"]')
    editBtn_loc = ('xpath', '//*[@id="set_right"]/div/div[1]/div[@class="function_title"]/span[@class="sbutton iconedit"]')
    refreshBtn_loc = ('xpath', '//*[@id="set_right"]/div/div[1]/div[@class="function_title"]/span[@class="sbutton iconrefresh"]')

    # 列表第一行的元素
    firstLayoutName_loc = ('xpath', '//*[@id="set_right"]/div/div[2]/div/div[1]/div/table/tbody/tr[1]/td[1]')
    firstLayoutEdit_loc = ('xpath', '//*[@id="set_right"]/div/div[2]/div/div[1]/div/table/tbody/tr[1]/td/a[@title="Edit"]')
    firstLayoutDel_loc = ('xpath', '//*[@id="set_right"]/div/div[2]/div/div[1]/div/table/tbody/tr[1]/td/a[@title="Delete"]')

    # 确认删除
    layoutDelOk_loc = ('xpath', yes_btn)

    # Layout编辑页面
    saveBtn_loc = ('xpath', '//*[@id="right_popup"]/div/div[@class="function_title"]/span[@class="sbutton iconsave button-save"]')
    saveExit_loc = ('xpath', '//*[@id="right_popup"]/div/div[@class="function_title"]/span[@class="sbutton iconsave button-save-exit"]')
    exitBtn_loc = ('xpath', '//*[@id="right_popup"]/div/div[@class="function_title"]/span[@class="sbutton iconexit button-exit"]')

    # 保存弹出界面
    saveLayoutmess_loc = ('xpath', msg_content)
    saveLyoutOk_loc = ('xpath', ok_btn)

    funcs = '//*[@id="right_popup"]/div/div[@class="subcontent"]/div[@class="settings-line"]/'

    # 页面元素
    # layoutNameinbox_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div[2]/span[1]/input')
    layoutNameinbox_loc = ('class name', 'text-layout-name')
    includelogoCh_loc = ('id', 'layout-include-logo')

    # icon上传及删除按钮
    logoUpload_loc = ('xpath', '//*[@id="right_popup"]/div/div[3]/div[1]/span[@class="icon-file"]/span[@class="svg-button button-icon-upload"]')
    logodel_loc = ('xpath', '//*[@id="right_popup"]/div/div[3]/div[1]/span[@class="icon-file"]/span[@class="svg-button button-icon-delete"]')

    # notesInbox_loc = ('xpath', '//*[@id="right_popup"]/div/div[3]/span[3]/textarea')
    notesInbox_loc = ('class name', 'text-layout-notes')

    # Headers
    leftHeaderInbox_loc = ('xpath', funcs + 'div[@class="layout-headers-left"]/textarea')
    midHeaderInbox_loc = ('xpath', funcs + 'div[@class="layout-headers-middle"]/textarea')
    rightHeaderInbox_loc = ('xpath', funcs + 'div[@class="layout-headers-right"]/textarea')

    # Footers
    leftFooterInbox_loc = ('xpath', funcs + 'div[@class="layout-footers-left"]/textarea')
    midFooterInbox_loc = ('xpath', funcs + 'div[@class="layout-footers-middle"]/textarea')
    rightFooterInbox_loc = ('xpath', funcs + 'div[@class="layout-footers-right"]/textarea')