# coding: utf-8

from Common.operater import  Operater

class MaintenanceRecordPage(Operater):

    # 左侧滑块中AssetHealth按钮
    assethealth_loc = ('xpath', ".//*[@id='divLeftTitle']/div[8]/div")

    # Maintenance Record菜单按钮
    maintenancerecord_loc = ('xpath', ".//*[@id='nav_record']/a/span")

    # Maintenance Record管理页面iframe
    iframe_loc = ('xpath', ".//*[@id='set_right']/iframe")

    # Maintenance Record管理页面查询条件
    begindate_loc = ('id', "startdatetxt")
    enddate_loc = ('id', "enddatetxt")
    typeselect_loc = ('id', "typeselectinput")
    searchinput_loc = ('id', "searchinputtxt")
    searchbotton_loc = ('xpath', ".//*[@id='recordcontent']/div[2]/input[2]")

    # Maintenance Record新增按钮
    addbutton_loc = ('xpath', ".//*[@id='recordcontent']/div[3]/span[@class='sbutton iconadd']")

    # Maintenance Record刷新按钮
    refreshbutton_loc = ('xpath', ".//*[@id='recordcontent']/div[3]/span[@class='sbutton iconrefresh']")

    # 选择机器查询条件元素
    type_loc = ('id', "typeselectinput")  # 页面type过滤条件
    typeselect1_loc =('xpath', ".//*[@id='typeselectinput']/option[2]") # 列表第二个元素


    assetdropdown_loc = ('id', "droptable")  # 机器下拉列表框
    assetlist_loc = ('id', "machines_tbody") # 机器列表
    assetselect_loc = ('xpath', ".//*[@id='machines_tbody']/tr[6]")
    searchinput1_loc = ('id', "searchinputtxt") # 页面过滤条件输入框
    searchbotton1_loc = ('xpath', ".//*[@id='content1']/div[1]/div[3]/input[2]")  # 页面查询按钮


    # 新增按钮
    addrecordbutton_loc = ('xpath', ".//*[@id='content1']/div[1]/div[5]/div[1]/input[1]")

    # 新增Reocrd窗口iframe
    mriframe_loc = ('id', "iframemaintenancerecord")
    # mriframe_loc = ('xpath', ".//*[@id='dialog_maintenancerecord']/iframe")

    # Record详情页面元素
    pmalert_loc = ('id', "dialog_pmalerts")  # pm alert 选择框
    maintenacedate_loc = ('id', "dialog_mdate") # maintenance 日期
    maintenancetype_loc = ('id', "dig_mtype")  # maintenance 类型选择框
    maintenancehour_loc = ('id', "dialog_hours") # maintenance 时间输入框
    cost_loc = ('id', "dialog_cost") # cost 输入框
    invoicenum_loc = ('id', "dialog_invoicenumber") # invoice number输入框
    completedby_loc = ('id', "dig_completedby")  # completed by 输入框
    descrip_loc = ('id', "dialog_notes") # description 输入框
    attachment_loc = ('id', "uploadattfile") # 上传附件按钮

    savebotton_loc = ('xpath', ".//*[@id='content1']/div[2]/div[1]/span[1]")   # save 按钮
    saveexitbotton_loc = ('xpath', ".//*[@id='content1']/div[2]/div[1]/span[2]") # save and exit 按钮
    withoutsave_loc = ('xpath', ".//*[@id='content1']/div[2]/div[1]/span[3]")  # exit without saving 按钮

    savemsg_loc = ('xpath', "html/body/div[5]/div[2]/div")  # save提示信息
    saveok_loc = ('xpath', "html/body/div[5]/div[3]/input") # save提示信息中ok按钮



