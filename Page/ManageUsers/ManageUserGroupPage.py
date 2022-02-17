# -*- coding: utf-8 -*-

from Common.operater import Operater

class ManageUserGroupPage(Operater):

    settings_loc = ('id', "button_menu")    # 左侧滑块列表中的Settings按钮
    usersetup_loc = ('xpath', ".//*[@id='menu_panel']/ul/li[1]/a/span")     # Settings面板中的User Setup按钮
    usergroup_loc = ('xpath', ".//*[@id='nav_user_group']/a/span")  # User Group菜单按钮

    iframe_loc = ('xpath', ".//*[@id='set_right']/iframe")  # User Groups页面嵌套的iframe

    addgroupbutton_loc = ('xpath', ".//*[@id='content1']/div/div[2]/span[1]")  # add 按钮
    refreshbutton_loc = ('xpath', ".//*[@id='content1']/div/div[2]/span[2]")  # refresh 按钮

    groupname_loc = ('id', "dialog_group_name")  # 新增窗口中 user group name文本输入框
    description_loc = ('id', "dialog_group_description")  # 新增窗口中 description文本输入框

    allselect_loc = ('xpath', ".//*[@id='tab_groupinfo']/table[2]/tbody/tr/td[2]/input[2]")  # 分配用户全选按钮

    okbuttong_loc = ('xpath', ".//*[@id='dialog_user_group']/div[3]/input[2]")  # 新增窗口OK按钮
