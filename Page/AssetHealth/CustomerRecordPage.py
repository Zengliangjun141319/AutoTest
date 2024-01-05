# coding: utf-8

from operater import Operater
from Page.comms import *


class CustomerRecordPage(Operater):

    # 左侧菜单列表中的assethealth菜单
    assethealth_loc = ('xpath', ".//*[@id='divLeftTitle']/div[8]/div")

    # Customer Record菜单
    customerrecord_loc = ('id', "nav_customerrecord" )

    # Customer Record列表所在iframe

    iframe_loc = ('xpath', ".//*[@id='set_right']/iframe")

    # 页面查询功能元素
    searchinput_loc = ('id', "searchinputtxt")  # 查询输入框
    searchbutton_loc = ('xpath', './/*[@id="content1"]/div/div[2]/input[@value="Search"]')  # 查询按钮
    searchresult_loc = ('xpath', ".//*[@id='customerlist']/div/div[1]/div/table/tbody/tr/td[1]/span")  # record列表第一行的companyname
    deletecustomer_loc = ('xpath', ".//*[@id='customerlist']/div/div[1]/div/table/tbody/tr/td/a[@title='Delete']")  # 第一行的删除按钮
    deletecustomeryes_loc = ('xpath', yes_btn)  # 删除Customer确认按钮

    # 页面新增、编辑、刷新、导出功能元素
    addbutton_loc = ('xpath', ".//*[@id='content1']/div/div[3]/span[1]")  # 新增按钮
    editbutton_loc = ('xpath', ".//*[@id='content1']/div/div[3]/span[2]")  # 编辑按钮
    refreshbutton_loc = ('xpath', ".//*[@id='content1']/div/div[3]/span[3]")  # 刷新按钮
    exportbutton_loc = ('xpath', ".//*[@id='content1']/div/div[3]/span[4]")  # 导出到Excel按钮

    # 新增Customer窗口元素
    iframecustomer_loc = ('id', "iframeuser")  # 新增customer窗口iframe
    codeinput_loc = ('id', "dialog_code")  # Code文本输入框
    companyname_loc = ('id', "dialog_name")  # companyname 文本输入框
    addressinput_loc = ('id', "dialog_custaddress")  # address文本输入框
    notesinput_loc = ('id', "dialog_notes")  # notes文本输入框
    contactaddbutton_loc = ('xpath', ".//*[@id='tab_custinfo']/div/span[2]")  # contact 新增按钮

    # Customer分配机器
    assignedasset_loc = ('xpath', ".//*[@id='customerlist']/div/div[1]/div/table/tbody/tr[1]/td/a[@title='Assets Assignment']")  # 分配机器按钮
    addassetbutton_loc = ('xpath', ".//*[@id='dialog_managemahchine']/div[4]/span[1]")  # 添加机器按钮
    searchassetinput_loc = ('xpath', ".//*[@id='dialog_machines']/div[2]/div[1]/input")  # 查询机器条件输入框
    searchassetbutton_loc = ('xpath', ".//*[@id='dialog_machines']/div[2]/div[1]/div")  # 查询机器按钮
    assetcheckbutton_loc = ('xpath', '//*[@id="dialog_machines"]/div[2]/div[5]/div/div[1]/div/table/tbody/tr[1]/td[1]/%s' % grid_ck)  # 第一台机器选择CheckBox
    assetokbutton_loc = ('xpath', ".//*[@id='dialog_machines']/div[3]/input[2]")  # 添加机器OK按钮
    closebutton_loc = ('xpath', ".//*[@id='dialog_managemahchine']/div[6]/input")  # 关闭机器分配窗口按钮
    deletebutton_loc = ('xpath', ".//*[@id='dialog_managemahchine']/div[4]/span[2]")  # 删除机器按钮
    deleteyesbutton_loc = ('xpath', "html/body/div[@class='dialog popupmsg']/div[@class='dialog-func']/input[2]")  # 确认删除机器按钮
    firstasset_loc = ('xpath', ".//*[@id='selectedmachinelist']/div/div[1]/div/table/tbody/tr/td[2]/span")

    # 新增Contact窗口元素
    contactname_loc = ('id', "dialog_contactname")  # contact name文本输入框
    preference_loc = ('id', "dialog_contactpreference")  # contact preference下拉选择框
    emailaddress_loc = ('id', "dialog_emailaddress")  # contact Email地址文本输入框
    mobile_loc = ('id', "dialog_mobile")  # mobile文本输入框
    contactaddress_loc = ('id', "dialog_address")  # contact address文本输入框
    activecheckbox_loc = ('id', "dialog_active")  # active复选框
    contactnotes_loc = ('id', "dialog_contactnotes")  # contact notes文本输入框
    contactokbutton_loc = ('xpath', ".//*[@id='dialog_contact']/div[3]/input[2]")  # contact OK 按钮
    contactcancelbutton_loc = ('xpath', ".//*[@id='dialog_contact']/div[3]/input[1]")  # contact Cancel 按钮

    # Customer保存功能元素
    savebutton_loc = ('xpath', './/*[@id="content1"]/div/div[@class="function_title"]/span[1]')  # customer保存按钮
    saveexitbutton_loc = ('xpath', ".//*[@id='content1']/div/div[@class='function_title']/span[2]")  # 保存退出按钮
    withoutsaveexit_loc = ('xpath', './/*[@id="content1"]/div/div[@class="function_title"]/span[3]')  # 不保存退出按钮

    # 保存后信息元素
    savemsg_loc = ('xpath', msg_content)  # 保存后提示信息
    # /html/body/div[4]/div[3]/input
    savemsgok_loc = ('xpath', ok_btn)  # 提示信息OK 按钮