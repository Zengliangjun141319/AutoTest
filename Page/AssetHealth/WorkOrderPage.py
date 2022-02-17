# coding: utf-8

from Common.operater import Operater

class WorkOrderPage(Operater):

    # 左侧滑块中AssetHealth按钮
    assethealth_loc = ('xpath', ".//*[@id='divLeftTitle']/div[8]/div")

    # 左侧菜单中work order菜单
    workordermenu_loc = ('id', "nav_workorder")

    # work order管理页面嵌套的iframe
    iframe_loc = ('xpath', ".//*[@id='set_right']/iframe")
    iframeworkorder_loc = ('id', "iframeworkorder")

    # work order页面查询条件部分的元素
    assertgroup_loc = ('id', "div_assetgroup") # assertgroup查询条件下拉选择框
    inputtext_loc = ('id', "searchinputtxt") # workorder查询条件输入框
    searchbutton_loc = ('xpath', ".//*[@id='recordcontent']/div[2]/input[2]") # 查询按钮
    maintenancerecord_loc = ('id', "chkshowmaintenance") # view maintaenance records复选框



    # work order页面列表信息部分的元素
    addbutton_loc = ('xpath', ".//*[@id='recordcontent']/div[@class='function_title']/span[@class='sbutton iconadd']") # 新增按钮
    editbutton_loc = ('xpath', ".//*[@id='recordcontent']/div[@class='function_title']/span[@class='sbutton iconedit']") # 编辑按钮
    refreshbutton_loc = ('xpath', ".//*[@id='recordcontent']/div[@class='function_title']/span[@class='sbutton iconrefresh']") # 刷新按钮
    layout_loc = ('xpath', ".//*[@id='recordcontent']/div[@class='function_title']/span[@class='sbutton iconlayout']") # Layout 按钮
    resetlayout_loc = ('xpath', ".//*[@id='recordcontent']/div[@class='function_title']/span[@class='sbutton iconresetlayout']")  # Reset Layout 按钮
    resetcheck_loc = ('xpath', 'html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input[@value="Yes"]')
    # 增加导出 ------ 2021.12.28
    exportExcel_loc = ('xpath', '//*[@id="recordcontent"]/div[@class="function_title"]/span[@class="sbutton iconexport"]')


    # Tab页标题
    workortab_loc = ('id', "li_workorder") # work order tab标签
    alertstab_loc = ('xpath', ".//*[@id='ul_container']/li[2]") # alerts tab标签
    segmentstab_loc = ('xpath', ".//*[@id='ul_container']/li[3]") # segments tab标签

    # 选择机器 详细信息
    assetselect_loc = ('id', "btnSelectAsset") # 机器选择按钮
    assetlist_loc = ('id', "dialog_machines") # 机器列表框
    assetsearchinput_loc = ('xpath', ".//*[@id='dialog_machines']/div[2]/div[1]/input") # 机器查询条件输入框
    assetsearchbutton_loc = ('xpath', ".//*[@id='dialog_machines']/div[2]/div[1]/div")  # 机器查询按钮
    searchresult_loc = ('xpath', ".//*[@id='dialog_machines']/div[2]/div[4]/div/div/div/table/tbody/tr") # 查询结果
    assetokbutton_loc = ('xpath', ".//*[@id='dialog_machines']/div[3]/input[2]")  # OK按钮

    # 选择Contact 详细信息
    customerselect_loc = ('id', "btnaddcustomer")  # customer选择按钮
    allcustomer_loc = ('id', "chkshowallcust") # show all customer复选框
    customerinfo_loc = ('xpath', ".//*[@id='customerlist']/div/div/div/table/tbody/tr[1]")  # 选择customer信息
    customerok_loc = ('xpath', ".//*[@id='dialog_customer']/div[3]/input[2]") # customer确认按钮

    addcontact_loc = ('xpath', ".//*[@id='traddcontact']/td/span") # 新增Contact按钮
    contactname_loc = ('id', "dialog_contactname") # contact name 文本输入框
    preferences_loc = ('id', "dialog_contactpreference") # contact preferences下拉选择框
    email_loc = ('id', "dialog_emailaddress") # email address 文本输入框
    mobile_loc = ('id', "dialog_mobile") # mobile 文本输入框
    contactnotes_loc = ('id', "dialog_contactnotes") # contact notes文本输入框
    contactok_loc = ('xpath', ".//*[@id='dialog_customercontact']/div[3]/input[2]") # contact OK 按钮

    wotypeicon_loc = ('xpath', ".//*[@id='dialog_wotype']/div/div[1]")
    wotypeselect_loc = ('xpath', ".//*[@id='dropdowndiv']/ul/li[2]") # work order类型下拉列表框
    followupdate_loc = ('id', "dialog_nextfollowupdate") # newt follow up date文本框
    assignedto_loc = ('id', "dialog_assignto")  # assigned to下拉列表框
    duedate_loc = ('id', "dialog_duedate") # due date文本输入框
    status_loc = ('id', "dialog_status") # status下拉列表框
    completeddate_loc = ('id', "dialog_completeddate") # completed date日期输入框
    internalid_loc = ('id', "dialog_internalid") # internal ID文本输入框
    description_loc = ('id', "dialog_description") # description文本输入框
    odometer_loc = ('id', "dialog_odometer")
    odometeruom_loc = ('id', "dig_odometeruom")

    # cost详细信息
    metertype_loc = ('id', "dialog_metertype")  # meter type 下拉选择框
    hourmeter_loc = ('id', "dialog_hourmeter")  # hour meter 文本输入框
    expectedcost_loc = ('id', "dialog_expectedcost") # expected cost 文本显示框
    totalcost_loc = ('id', "dialog_workordercosts")  # work order total cost 文本显示框
    othercost_loc = ('id', "dialog_othercost") # other cost 文本输入框
    partscost_loc = ('id', "dialog_partscost") # parts cost 文本输入框
    traveltimecost_loc = ('id', "dialog_traveltimecost") # travel time cost 文本输入框
    laborcost_loc = ('id', "dialog_laborcost")  # labor cost 文本显示框
    hourlyrate_loc = ('id', "dialog_hourlyrate") # hourly rate 文本显示框
    timetocomplete_loc = ('id', "dialog_timetocomplete") # time to complete 文本输入框
    invoicenum_loc = ('id', "dialog_invoicenumber") # invoice number 文本输入框
    notes_loc = ('id', "dialog_notes") # notes 文本输入框




    emaildetail_loc = ('id', "input_emaildetails") # email details 按钮
    print_loc = ('id', "btnPrint") # print 按钮
    savebotton_loc = ('xpath', ".//*[@id='tab_workorder']/div[1]/span[1]") # 保存按钮
    saveandexitbutton_loc = ('xpath', ".//*[@id='tab_workorder']/div[1]/span[2]") # 保存退出按钮
    withoutsavebutton_lco = ('xpath', ".//*[@id='tab_workorder']/div[1]/span[3]") # 不保存退出按钮

    savedialogmessage_loc = ('xpath', 'html/body/div[@class="dialog popupmsg"]/div[2]/div') # save后提示框信息
    savedialogokbotton_loc = ('xpath', 'html/body/div[@class="dialog popupmsg"]/div[3]/input') # save提示信息框OK按钮

    # Status Setting设置页面
    statussetting_loc = ('xpath', ".//*[@id='recordcontent']/div[1]/span[2]") # status setting 按钮
    iframestatus_loc = ('id', "iframeworkorderstatus")  # work order iframe
    statusaddbutton_loc = ('xpath', ".//*[@id='content1']/div[2]/div[3]/span[1]") # status 新增按钮

    statusnameinput_loc = ('id', "dialog_statusname")  # status name文本输入框
    statuscolorinput_loc = ('id', "dialog_statuscolor") # status color文本输入框
    statusokbutton_loc = ('xpath', ".//*[@id='dialog_status']/div[3]/input[2]") # 新增status OK 按钮
    statusrefresh_loc = ('xpath', ".//*[@id='content1']/div[2]/div[3]/span[2]") # status 刷新按钮
    statusexit_loc = ('xpath', ".//*[@id='content1']/div[2]/div[3]/span[3]") # status 列表退出按钮


    # Layout设置窗口
    allselect_loc = ('class name', "data-column-header-checkbox")
    firstcolumn_loc = ('xpath', ".//*[@id='dialog_layouts']/div[2]/div/div/div/div/table/tr[1]/td[1]/span")
    firstcolumninput_loc = ('xpath', ".//*[@id='dialog_layouts']/div[2]/div/div/div/div/table/tr[1]/td[2]/content/span/input")
    firstcolumnselect_loc = ('xpath', "//*[@id='dialog_layouts']/div[2]/div/div/div/div/table/tr[1]/td[3]/input")
    secondcolumnselect_loc = ('xpath', ".//*[@id='dialog_layouts']/div[2]/div/div/div/div/table/tr[2]/td[3]/input")
    thirdcolumnselect_loc = ('xpath', "//*[@id='dialog_layouts']/div[2]/div/div/div/div/table/tr[3]/td[3]/input")
    fourthcolumnselect_loc = ('xpath', "//*[@id='dialog_layouts']/div[2]/div/div/div/div/table/tr[4]/td[3]/input")
    fifthcolumnselect_loc = ('xpath', "//*[@id='dialog_layouts']/div[2]/div/div/div/div/table/tr[5]/td[3]/input")
    layoutokbutton_loc = ('xpath', ".//*[@id='dialog_layouts']/div[3]/input[2]")
    columnname1_loc = ('xpath', ".//*[@id='workorderlist']/div/div/table/tr[1]/th[1]/div")
    columnname2_loc = ('xpath', ".//*[@id='workorderlist']/div/div/table/tr[1]/th[2]/div")

    # WorkOrder第一条记录的work order number和description
    firstcell_loc = ('xpath', ".//*[@id='workorderlist']/div/div[1]/div/table/tbody/tr[1]/td[1]")
    fifthcell_loc = ('xpath', ".//*[@id='workorderlist']/div/div[1]/div/table/tbody/tr[1]/td[5]/span")

    wonumber_loc = ('xpath', "//*[@id='workorderlist']/div/table/tbody/tr/th[1]/div[1]/span")

    statuscol_loc = ('xpath', "//*[@id='workorderlist']/div/div[1]/div/table/tbody/tr[1]/td[4]/span/div/select")
    statuschangeok_loc = ('id', "btn_save")

    defaultlayout_loc = ('xpath', "//*[@id='recordcontent']/div[2]/span[@class='sbutton iconlayout']")
    resetdefault_loc = ('xpath', "/html/body/div[@class='dialog popupmsg']/div[@class='dialog-func']/input[3]")





    # 查询
    def search(self, text):
        self.send_keys(self.inputtext_loc, text)
        self.click(self.searchbutton_loc)


    def inputTo(self, inboxloc, text):
        self.send_keys(inboxloc, text)

