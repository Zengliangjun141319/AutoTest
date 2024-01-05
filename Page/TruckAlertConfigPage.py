# coding:utf-8

from operater import Operater
from Page.comms import *


class TruckAlertPage(Operater):
    # 左侧主菜单列表中Full Menu菜单
    fullmenu_loc = ('id', "button_sites")

    # Over/Under Trucking alerts菜单
    truckalertmenu_loc = ('xpath', ".//*[@id='sites_panel']/div[1]/div[2]/ul/li[9]/a/span")

    # 查询条件元素
    searchinput_loc = ('id', "searchinputtxt")   # 查询条件输入框
    searchbutton_loc = ('xpath', ".//*[@id='content']/div/div[2]/input[2]") # 查询按钮

    # 新增按钮
    addbutton_loc = ('xpath', ".//*[@id='content']/div/div[3]/span[1]")

    # 刷新按钮
    refreshbutton_loc = ('xpath', ".//*[@id='content']/div/div[3]/span[2]")

    # 新增窗口iframe
    iframe_loc = ('id', "iframejobsitelimit")

    # 新增窗口中元素
    jobsiteselect_loc = ('id', "dialog_jobsite")  # jobsite下拉选择列表
    activecheckbox_loc = ('id', "dialog_active")  # active复选框
    starthour_loc = ('id', "dialog_starttimehour")  # 开始时间小时下拉选择列表
    startminute_loc = ('id', "dialog_starttimeminute")  # 开始时间分钟下拉选择列表
    endhour_loc = ('id', "dialog_endtimehour")  # 结束时间小时下拉选择列表
    endminute_loc = ('id', "dialog_endtimeminute")  # 结束时间分钟下拉选择列表
    mintrucks_loc = ('id', "dialog_mintrucks")  # Acceptable minimum trucks文本输入框
    maxtrucks_loc = ('id', "dialog_maxtrucks")  # Acceptable maxnum trucks文本输入框
    assettype_loc = ('xpath', '//*[@id="dialog_assettype"]/div/div[1]/label[2]')  # Acceptable asset type选择框
    # typeselect_loc = ('xpath', '//*[@id="dialog_assettype"]/div/div[2]/ul/li[5]/input')  # 下拉选择列表第5个选项
    notes_loc = ('id', "dialog_notes")  # Notes文本输入框

    savebutton_loc = ('xpath', ".//*[@id='content1']/div[2]/div[1]/span[1]")  # Save按钮
    saveexitbutton_loc = ('xpath', ".//*[@id='content1']/div[2]/div[1]/span[2]")  # Save and Exit按钮
    withoutsavebutton_loc = ('xpath', ".//*[@id='content1']/div[2]/div[1]/span[3]")  # Exit without saving按钮

    savemsg_loc = ('xpath', msg_content)  # 保存成功提示信息
    savemsgok_loc = ('xpath', ok_btn)  # 保存提示信息OK按钮

    searchresult_loc = ('xpath', '//*[@id="jobsitelimitlist"]/div/div[1]/div/table/tbody/tr')
    subscribeBt_loc = ('xpath', '//*[@id="jobsitelimitlist"]/div/div[1]/div/table/tbody/tr/td[10]/a')
    selectallBt_loc = ('xpath', '//*[@id="dialog_subscribecontacts"]/div[@class="div_machines"]/table/tbody/tr/td[@class="td_controller"]/input[2]')
    subscribeOK_loc = ('xpath', '//*[@id="dialog_subscribecontacts"]/div[@class="dialog-func"]/input[2]')

    # //*[@id="jobsitelimitlist"]/div/div[1]/div/table/tbody/tr/td[12]
    delsearch_loc = ('xpath', '//*[@id="jobsitelimitlist"]/div/div[1]/div/table/tbody/tr/td[12]')
    delOk_loc = ('xpath', yes_btn)