# coding: utf-8
'''
获取同级多个元素中最后一个元素的方法： last()
    如： last_comments_txt = ('xpath', '//*[@id="workorderdetail"]/div/div/div[2]/div[1]/div/div[3]/div[last()]/div[2]/span')
'''
from operater import Operater
from Page.comms import *


class WorkOrderPage(Operater):

    # 左侧滑块中AssetHealth按钮
    assethealth_loc = ('xpath', ".//*[@id='divLeftTitle']/div[8]/div")

    # 左侧菜单中work order菜单
    workordermenu_loc = ('id', "nav_workorder")

    # work order管理页面嵌套的iframe
    iframe_loc = ('xpath', ".//*[@id='set_right']/iframe")
    iframeworkorder_loc = ('id', "iframeworkorder")

    # work order页面查询条件部分的元素
    assertgroup_loc = ('id', "div_assetgroup")  # assertgroup查询条件下拉选择框
    inputtext_loc = ('id', "searchinputtxt")  # workorder查询条件输入框
    searchbutton_loc = ('xpath', './/*[@id="recordcontent"]/div[2]/input[@value="Search"]')  # 查询按钮
    maintenancerecord_loc = ('id', "chkshowmaintenance")  # view maintaenance records复选框
    # displaycompleteChx_loc = ('id', 'chkcompleted')
    displaySelect_loc = ('id', 'selcompleted')

    # work order页面列表信息部分的元素
    addbutton_loc = ('xpath', ".//*[@id='recordcontent']/div[@class='function_title']/span[@class='sbutton iconadd']") # 新增按钮
    editbutton_loc = ('xpath', ".//*[@id='recordcontent']/div[@class='function_title']/span[@class='sbutton iconedit']") # 编辑按钮
    refreshbutton_loc = ('xpath', ".//*[@id='recordcontent']/div[@class='function_title']/span[@class='sbutton iconrefresh']") # 刷新按钮
    layout_loc = ('xpath', '//*[@id="recordcontent"]/div[@class="function_title"]/span[@class="sbutton iconlayout iconmenu"]')
    # ('xpath', ".//*[@id='recordcontent']/div[@class='function_title']/span[@class='sbutton iconlayout iconmenu']") # Layout 按钮
    # 406版本取消Reset Layout功能
    # resetlayout_loc = ('xpath', ".//*[@id='recordcontent']/div[@class='function_title']/span[@class='sbutton iconresetlayout']")  # Reset Layout 按钮
    # resetcheck_loc = ('xpath', 'html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input[@value="Yes"]')
    # 增加导出 ------ 2021.12.28
    exportExcel_loc = ('xpath', '//*[@id="recordcontent"]/div[@class="function_title"]/span[@class="sbutton iconexport"]')

    # 406版本调整Layout设置UI
    layout_panel = '//*[@id="layout_panel_holder"]/div/ul'
    uplayout_loc = ('xpath', '%s/li[text()="Update Layout"]' % layout_panel)  # Update Layout
    savelayout_loc = ('xpath', '%s/li[text()="Save Layout"]' % layout_panel)
    managelayout_loc = ('xpath', '%s/li[text()="Manage Layout"]' % layout_panel)
    my_default_layout_loc = ('xpath', '%s/li[text()="My Default *"]' % layout_panel)
    company_default_layout_loc = ('xpath', '%s/li[text()="Company Default *"]' % layout_panel)

    # layout设置界面元素
    showdefaultlayout = ('id', 'rdoDefaultLayout')   # Show Default Layout单选框
    selectAllChx_loc = ('xpath', '//*[@id="dialog_layouts"]/div[5]/div[1]/table/tr/td[1]/input')
    firstlayoutcolumnChx_loc = ('xpath', '//*[@id="dialog_layouts"]/div[5]/div[2]/table/tr[1]/td[1]/input')
    firstlayoutcolumnCapInbox_loc = ('xpath', '//*[@id="dialog_layouts"]/div[5]/div[2]/table/tr[1]/td[3]/input')
    layoutOK_loc = ('xpath', '//*[@id="dialog_layouts"]/div[@class="dialog-func"]/input[@value="OK"]')

    savelayoutname_loc = ('xpath', '//*[@id="dialog_savelayout"]/div[2]/input')   # layout name input box
    saveAsMyDefChx_loc = ('id', 'chkMyDefault')
    makePubChx_loc = ('id', 'chkPublic')
    saveCompChx_loc = ('id', 'chkCompanyDefault')
    savelayoutBtn_loc = ('xpath', '//*[@id="dialog_savelayout"]/div[@class="dialog-func"]/input[@value="Save Layout"]')
    savelayoutCancel_loc = ('xpath', '//*[@id="dialog_savelayout"]/div[@class="dialog-func"]/input[@value="Cancel"]')
    savemessage_loc = ('xpath', msg_content)
    saveOKBtn_loc = ('xpath', ok_btn)
    saveoverwriteYes_loc = ('xpath', yes_btn)
    saveoverwriteNo_loc = ('xpath', no_btn)

    # manage layout
    dellayoutYesBtn_loc = ('xpath', yes_btn)
    managelayoutOKBtn_loc = ('xpath', '//*[@id="dialog_managelayout"]/div[@class="dialog-func"]/input[@value="OK"]')

    # Tab页标题
    workortab_loc = ('id', "li_workorder")  # work order tab标签
    alertstab_loc = ('xpath', ".//*[@id='ul_container']/li[@data-href='tab_alerts']")  # alerts tab标签
    segmentstab_loc = ('id', "li_segments")  # segments tab标签
    attachmentstab_loc = ('id', 'li_attachments')  # Attachments
    inspectionstab_loc = ('id', 'li_inspections')   # Inspections
    estimatestab_loc = ('id', 'li_estimates')   # Estimates
    invoicestab_loc = ('id', 'li_invoices')   # Invoices

    # 选择机器 详细信息
    assetselect_loc = ('id', "btnSelectAsset")  # 机器选择按钮
    assetlist_loc = ('id', "dialog_machines")  # 机器列表框
    assetsearchinput_loc = ('xpath', ".//*[@id='dialog_machines']/div[2]/div[1]/input")  # 机器查询条件输入框
    assetsearchbutton_loc = ('xpath', ".//*[@id='dialog_machines']/div[2]/div[1]/div")  # 机器查询按钮
    # 位置变更　//*[@id="dialog_machines"]/div[2]/div[5]/div/div[1]/div/table/tbody/tr[1]/td[1]
    searchresult_loc = ('xpath', ".//*[@id='dialog_machines']/div[2]/div[5]/div/div/div/table/tbody/tr") # 查询结果
    assetokbutton_loc = ('xpath', ".//*[@id='dialog_machines']/div[3]/input[2]")  # OK按钮

    desc_window_ok_loc = ('xpath', '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input')

    # 选择Contact 详细信息
    customerselect_loc = ('id', "btnaddcustomer")  # customer选择按钮
    allcustomer_loc = ('id', "chkshowallcust")  # show all customer复选框
    customerinfo_loc = ('xpath', ".//*[@id='customerlist']/div/div/div/table/tbody/tr[1]")  # 选择customer信息
    customerok_loc = ('xpath', ".//*[@id='dialog_customer']/div[3]/input[2]")  # customer确认按钮

    addcontact_loc = ('xpath', ".//*[@id='traddcontact']/td/span")  # 新增Contact按钮
    contactname_loc = ('id', "dialog_contactname")  # contact name 文本输入框
    preferences_loc = ('id', "dialog_contactpreference")  # contact preferences下拉选择框
    preferencesE_loc = ('xpath', '//*[@id="dialog_contactpreference"]/div/div[2]/ul/li[2]')
    email_loc = ('id', "dialog_emailaddress")  # email address 文本输入框
    mobile_loc = ('id', "dialog_mobile")  # mobile 文本输入框
    contactnotes_loc = ('id', "dialog_contactnotes")  # contact notes文本输入框
    contactok_loc = ('xpath', ".//*[@id='dialog_customercontact']/div[3]/input[2]")  # contact OK 按钮

    # Contact Infomation
    companyCode = ('id', 'dialog_custcustomercode')
    companyName = ('id', 'dialog_custcustomername')

    wotypeicon_loc = ('xpath', ".//*[@id='dialog_wotype']/div/div[1]")
    wotype_loc = ('id', 'dialog_wotype')
    wotypeselect_loc = ('xpath', ".//*[@id='dropdowndiv']/ul/li[2]")  # work order类型下拉列表框
    wotypesel = ('xpath', '//*[@id="dialog_wotype"]/div/div[1]/input')
    followupdate_loc = ('id', "dialog_nextfollowupdate")  # newt follow up date文本框
    assignedto_loc = ('id', "dialog_assignto")  # assigned to下拉列表框
    duedate_loc = ('id', "dialog_duedate")  # due date文本输入框
    status_loc = ('id', "dialog_status")  # status下拉列表框
    completeddate_loc = ('id', "dialog_completeddate")  # completed date日期输入框
    internalid_loc = ('id', "dialog_internalid")  # internal ID文本输入框
    ponumber_loc = ('id', 'dialog_ponumber')   # PO Number
    description_loc = ('id', "dialog_description")  # description文本输入框
    odometer_loc = ('id', "dialog_odometer")
    odometeruom_loc = ('id', "dig_odometeruom")
    actrequireChx_loc = ('id', 'dialog_inspectionrequired')

    partsnmumberinbox = ('id', 'dialog_partsordernumber')
    partstatus = ('id', 'dialog_partsstatus')
    partsstatussel = ('xpath', '//*[@id="dialog_partsstatus"]/div/div[2]/ul/li[@title="Pending"]')
    location_loc = ('xpath', '//*[@id="dialog_location"]/div/div[1]/label[1]')
    locationsel = ('xpath', '//*[@id="dialog_location"]/div/div[2]/ul/li[3]')
    component = ('xpath', '//*[@id="dialog_wocomponent"]/div/div[1]/input')
    department_loc = ('xpath', '//*[@id="dialog_department"]/div/div[1]/label[1]')
    departmentsel = ('xpath', '//*[@id="dialog_department"]/div/div[2]/ul/li[2]')
    advisor_loc = ('xpath', '//*[@id="dialog_advisor"]/div/div[1]/label[1]')
    advisorsel = ('xpath', '//*[@id="dialog_advisor"]/div/div[2]/ul/li[2]')
    salesperson_loc = ('xpath', '//*[@id="dialog_salesperson"]/div/div[1]/label[1]')
    salespersonsel = ('xpath', '//*[@id="dialog_salesperson"]/div/div[2]/ul/li[3]')
    alternatestatus = ('id', 'dialog_alternatestatus')
    partsexpecteddate_inbox = ('id', 'dialog_partsexpecteddate')
    nextfollowup_inbox = ('id', 'dialog_nextfollowupdate')

    # Following
    exFollowing_loc = ('id', 'spanfollower')
    addFollowerBtn_loc = ('xpath', '//*[@id="traddfollower"]/td/span[@class="sbutton iconadd"]')
    firstFollowingChx_loc = ('xpath', '//*[@id="allfollowerlist"]/div/div[1]/div/table/tbody/tr[1]/td[4]/label/layer')
    addFollowerOk_loc = ('xpath', '//*[@id="addfollowerpopupdialog"]/div[@class="dialog-func"]/input[@value="OK"]')

    # cost详细信息
    metertype_loc = ('id', "dialog_metertype")  # meter type 下拉选择框
    metertype = ('xpath', '//*[@id="dialog_metertype"]/div/div[2]/ul/li[@value="Both"]')
    hourmeter_loc = ('id', "dialog_hourmeter")  # hour meter 文本输入框
    expectedcost_loc = ('id', "dialog_expectedcost")  # expected cost 文本显示框
    totalcost_loc = ('id', "dialog_workordercosts")  # work order total cost 文本显示框
    othercost_loc = ('id', "dialog_othercost")  # other cost 文本输入框
    partscost_loc = ('id', "dialog_partscost")  # parts cost 文本输入框
    traveltimecost_loc = ('id', "dialog_traveltimecost")  # travel time cost 文本输入框
    laborcost_loc = ('id', "dialog_laborcost")  # labor cost 文本显示框
    hourlyrate_loc = ('id', "dialog_hourlyrate")  # hourly rate 文本显示框
    timetocomplete_loc = ('id', "dialog_timetocomplete")  # time to complete 文本输入框
    invoicenum_loc = ('id', "dialog_invoicenumber")  # invoice number 文本输入框
    billablechx = ('id', 'dialog_billable')  # Billable 复选框
    billtojobDg = ('id', 'dialog_billtojob')  # Bill to job下拉框
    billjobsel = ('xpath', '//*[@id="dialog_billtojob"]/div/div[1]/label[1]')
    notes_loc = ('id', "dialog_notes")  # notes 文本输入框

    emaildetail_loc = ('id', "input_emaildetails")  # email details 按钮
    print_loc = ('id', "btnPrint")  # print 按钮
    savebotton_loc = ('xpath', './/*[@id="content1"]/div[1]/span[@class="sbutton iconsave"]')  # 保存按钮
    saveandexitbutton_loc = ('xpath', ".//*[@id='content1']/div[1]/span[2]")  # 保存退出按钮
    withoutsavebutton_lco = ('xpath', ".//*[@id='content1']/div[1]/span[3]")  # 不保存退出按钮

    # 729版本增加提示
    saveStatusChange_loc = ('id', 'btn_savestatuschange')
    saveStatusNo_loc = ('xpath', '//*[@id="dialog_statuschange"]/div[@class="dialog-func"]/input[@value="Cancel"]')

    savedialogmessage_loc = ('xpath', 'html/body/div[@class="dialog popupmsg"]/div[2]/div')  # save后提示框信息
    savedialogokbotton_loc = ('xpath', 'html/body/div[@class="dialog popupmsg"]/div[3]/input')  # save提示信息框OK按钮

    # Status Setting设置页面
    statussetting_loc = ('xpath', './/*[@id="recordcontent"]/div[1]/span[@class="sbutton iconcog"]')  # status setting 按钮

    iframestatus_loc = ('id', "iframeworkorderstatus")  # work order iframe
    # statusaddbutton_loc = ('xpath', ".//*[@id='content1']/div[2]/div[3]/span[1]") # status 新增按钮
    statusaddbutton_loc = ('xpath', '//*[@id="tab_statussetting"]/div[1]/span[@class="sbutton iconadd"]')

    statusnameinput_loc = ('id', "dialog_statusname")  # status name文本输入框
    statuscolorinput_loc = ('id', "dialog_statuscolor")  # status color文本输入框
    statusokbutton_loc = ('xpath', ".//*[@id='dialog_status']/div[3]/input[2]")  # 新增status OK 按钮
    statusrefresh_loc = ('xpath', '//*[@id="tab_statussetting"]/div[1]/span[@class="sbutton iconrefresh"]')  # status 刷新按钮
    statusexit_loc = ('xpath', '//*[@id="tab_statussetting"]/div[1]/span[@class="sbutton iconexit"]')  # status 列表退出按钮

    # Layout设置窗口
    allselect_loc = ('xpath', '//*[@id="dialog_layouts"]/div[4]/div[1]/table/tr/td[1]/input')
    # 旧位置 ('class name', "data-column-header-checkbox")
    firstcolumn_loc = ('xpath', ".//*[@id='dialog_layouts']/div[2]/div/div/div/div/table/tr[1]/td[1]/span")
    firstcolumninput_loc = ('xpath', '//*[@id="dialog_layouts"]/div[4]/div[2]/table/tr[1]/td[3]/input')
    firstcolumnselect_loc = ('xpath', '//*[@id="dialog_layouts"]/div[4]/div[2]/table/tr[1]/td[1]/input')
    secondcolumnselect_loc = ('xpath', '//*[@id="dialog_layouts"]/div[4]/div[2]/table/tr[2]/td[1]/input')
    thirdcolumnselect_loc = ('xpath', '//*[@id="dialog_layouts"]/div[4]/div[2]/table/tr[3]/td[1]/input')
    fourthcolumnselect_loc = ('xpath', '//*[@id="dialog_layouts"]/div[4]/div[2]/table/tr[4]/td[1]/input')
    fifthcolumnselect_loc = ('xpath', '//*[@id="dialog_layouts"]/div[4]/div[2]/table/tr[5]/td[1]/input')
    layoutokbutton_loc = ('xpath', './/*[@id="dialog_layouts"]/div[@class="dialog-func"]/input[2]')
    columnname1_loc = ('xpath', ".//*[@id='workorderlist']/div/div/table/tr[1]/th[1]/div")
    columnname2_loc = ('xpath', ".//*[@id='workorderlist']/div/div/table/tr[1]/th[2]/div")

    # 406版本新的Layout设置UI
    setlayoutnameinbox_loc = ('xpath', '//*[@id="dialog_savelayout"]/div[2]/input')
    savemydefault_chx_loc = ('id', 'chkMyDefault')
    savelayoutbtn_loc = ('xpath', '//*[@id="dialog_savelayout"]/div[@class="dialog-func"]/input[@value="Save Layout"]')
    savelayoutYesBtn_loc = ('xpath', yes_btn)

    # WorkOrder第一条记录的work order number和description
    first_line = '//*[@id="workorderlist"]/div/div[1]/div/table/tbody/tr/td'
    firstcell_loc = ('xpath', ".//*[@id='workorderlist']/div/div[1]/div/table/tbody/tr[1]/td[1]")
    first_wo_number = ('xpath', '//*[@id="workorderlist"]/div/div[1]/div/table/tbody/tr/td[1]/span')
    fifthcell_loc = ('xpath', ".//*[@id='workorderlist']/div/div[1]/div/table/tbody/tr[1]/td[5]/span")
    first_line_cell = ('xpath', '//*[@id="workorderlist"]/div[2]/div/div/table/tbody/tr/td[1]/span')

    wo_first_edit_btn = ('xpath', first_line + '/a[@title="Edit"]')
    wo_first_print_btn = ('xpath', first_line + '/a[@title="Print"]')
    wo_first_del_btn = ('xpath', first_line + '/a[@title="Delete"]')
    wo_first_alert_btn = ('xpath', first_line + '/a[@Asset Alert]')

    wonumber_loc = ('xpath', "//*[@id='workorderlist']/div/table/tr/th[1]/div[1]/span")

    searchresultWO_loc = ('xpath', '//*[@id="workorderlist"]/div/div[1]/div/table/tbody/tr/td[1]')
    statuslistBtn_loc = ('xpath', '//*[@id="workorderlist"]/div/div[1]/div/table/tbody/tr/td[4]/span/div/div/div[1]/label[2]')
    statuscol_loc = ('xpath', '//*[@id="workorderlist"]/div[2]/ul/li[@title="Completed"]')

    completeddateinbox = ('id', 'dialog_completeddate')
    statuschangeok_loc = ('id', "btn_save")

    defaultlayout_loc = ('xpath', "//*[@id='recordcontent']/div[2]/span[@class='sbutton iconlayout']")
    resetdefault_loc = ('xpath', "/html/body/div[@class='dialog popupmsg']/div[@class='dialog-func']/input[3]")

    # Segments
    addsegmentBtn_loc = ('xpath', '//*[@id="tab_segments"]/div/span[@class="sbutton iconadd"]')
    segmentHoursInbox_loc = ('id', 'dialog_segmenthour')
    segmentCostInbox_loc = ('id', 'dialog_segmentcost')
    segmentBillable_chx_loc = ('id', 'dialog_segmentbillable')
    segmentDescInbox_loc = ('id', 'dialog_segmentdesc')
    seg_ok = '//div[@class="dialog"]/div/span[text()="Add Segment"]/../../div[@class="dialog-func"]/input[@value="OK"]'
    segmentBtnOK_loc = ('xpath', seg_ok)  # 通过子元素定位父元素再定位

    segmenttitle_lab = ('xpath', '//*[@id="tab_segments"]/table/tr[1]/td[1]')

    # Attachments
    addattachmentsBtn_loc = ('xpath', '//*[@id="tab_attachments"]/div[1]/span[@class="sbutton iconadd"]')
    attachmentNameInbox_loc = ('xpath', '//*[@id="woaatts_tr"]/td/div/div/div[3]/input')
    attachmentViewChx_loc = ('xpath', '//*[@id="woaatts_tr"]/td/div/div/div[1]/input')

    # Estimates
    addestBtn_loc = ('xpath', '//*[@id="tab_estimates"]/div/span')
    addest_Number = ('id', 'dialog_est_number')
    addest_totalcoast_Inbox = ('id', 'dialog_est_totalcosts')
    addest_totalcost_Btn = ('xpath', '//*[@id="dialog_est_totalcosts"]/../span')  # 通过精确的子元素定位父元素，再定位元素
    addest_othercost_inbox = ('id', 'dialog_est_othercost')
    addest_partcost_inbox = ('id', 'dialog_est_partscost')
    addest_travelcost_inbox = ('id', 'dialog_est_traveltimecost')
    addest_laborcost_inbox = ('id', 'dialog_est_laborcost')
    addest_porequired_chx = ('id', 'dialog_est_porequired')  # PO Required CheckBox
    addest_technotes_inbox = ('id', 'dialog_est_technotes')
    addest_timetocomp_inbox = ('id', 'dialog_est_timetocomplete')
    addest_taxes_inbox = ('id', 'dialog_est_taxes')

    ok_loc = '//div[@class="dialog"]/div/span[text()="Add Estimate"]/../../div[@class="dialog-func"]/input[@value="OK"]'
    addest_OK_btn = ('xpath', ok_loc)  # '/html/body/div[9]/div[3]/input[@value="OK"]'
    addest_title_label = ('xpath', '//*[@id="tab_estimates"]/div[@class="subtitle estimates_div"]/span[2]')

    # publish estimate
    pub_est_ex_btn = ('xpath', '//*[@id="tab_estimates"]/div[@class="subtitle estimates_div"]/span[1]')  # sbutton iconchevronright
    pub_est_number_label = ('xpath', '//*[@id="tab_estimates"]/div[@class="subtitle estimates_div"]/span[2]')
    pub_est_status_label = ('xpath', '//*[@id="tab_estimates"]/div[@class="subtitle estimates_div"]/span[3]')
    pub_est_Save_btn = ('xpath', '//*[@id="tab_estimates"]/table/tr[10]/td[3]/input[@value="Save"]')
    pub_est_publish_btn = ('xpath', '//*[@id="tab_estimates"]/table/tr[10]/td[3]/input[@value="Publish"]')
    pub_est_revoke_btn = ('xpath', '//*[@id="tab_estimates"]/table/tr[10]/td[3]/input[@value="Revoke"]')

    pub_est_sendto_chx = ('id', 'dialog_est_chksendtextmsg')
    pub_est_phonenum_inbox = ('id', 'dialog_est_phonenum')
    pub_est_sendAtt_chx = ('id', 'dialog_est_chkSendAttachment')
    pub_btn_loc = '//div[@class="dialog"]/div/span[text()="Publish Estimate"]/../../div[@class="dialog-func"]/input[@value="Publish"]'
    pub_est_publish_publish_btn = ('xpath', pub_btn_loc)

    # 新建并发布评估
    publish_loc = '//div[@class="dialog"]/div/span[text()="Add Estimate"]/../../div[@class="dialog-func"]/input[@value="Publish"]'
    addest_publish_btn = ('xpath', publish_loc)
    addest_publish_status_label = ('xpath', '//*[@id="tab_estimates"]/div[3]/span[3]')

    # Invoice
    addinvBtn = ('xpath', '//*[@id="tab_invoices"]/div/span')
    addinv_number_inbox = ('id', 'dialog_invoice_number')
    addinv_othercost_inbox = ('id', 'dialog_invoice_othercost')
    addinv_totalcost_inbox = ('id', 'dialog_invoice_totalcosts')
    addinv_travelcost_inbox = ('id', 'dialog_invoice_traveltimecost')
    addinv_partscost_inbox = ('id', 'dialog_invoice_partscost')
    addinv_taxes_inbox = ('id', 'dialog_invoice_taxes')
    addinv_laborcost_inbox = ('id', 'dialog_invoice_laborcost')
    addinv_invstatus_sel = ('id', 'dialog_invoice_status')  # value:0,1,6,10
    addinv_paymentby_sel = ('id', 'dialog_invoice_paymentby')  # value: Credit Card,Check,Cash
    addinv_check_inbox = ('id', 'dialog_invoice_checknumber')
    addinv_customvis_chx = ('id', 'dialog_invoice_customervisible')
    addinv_notes_inbox = ('id', 'dialog_invoice_notes')
    inv_ok_loc = '//*[@class="dialog"]/div/span[text()="Add Invoice"]/../../div[@class="dialog-func"]/input[@value="OK"]'
    addinv_OK_btn = ('xpath', inv_ok_loc)
    addinv_title_label = ('xpath', '//*[@id="tab_invoices"]/div[@class="subtitle estimates_div"]/span[2]')

    # Invoice Publish
    inv_ex_btn = ('xpath', '//*[@id="tab_invoices"]/div[@class="subtitle estimates_div"]/span[1]')  # 展开： sbutton iconchevrondown
    inv_number_label = ('xpath', '//*[@id="tab_invoices"]/div[@class="subtitle estimates_div"]/span[2]')
    inv_status_label = ('xpath', '//*[@id="tab_invoices"]/div[@class="subtitle estimates_div"]/span[3]')  # Awaiting Payment\Draft
    inv_pub_status_label = ('xpath', '//*[@id="tab_invoices"]/div[3]/span[3]')
    inv_addAtt_btn = ('xpath', '//*[@id="tab_invoices"]/table/tr[7]/td[2]/div/span[@class="sbutton iconadd"]')

    # 添加附件
    inv_add_att_upload_btn = ('id', 'dialog_woinvoiceatt_uploadattfile')
    inv_add_att_caption_inbox = ('id', 'dialog_invoice_att_notes')
    save_btn_loc = '//*[@class="dialog"]/div/span[text()="Add Attachment"]/../../div[@class="dialog-func"]/input[@value="Save"]'
    inv_add_att_save_btn = ('xpath', '/html/body/div[17]/div[@class="dialog-func"]/input[@value="Save"]')
    inv_add_upload_fail_ok_btn = ('xpath', ok_btn)

    inv_pub_btn = ('xpath', '//*[@id="tab_invoices"]/table/tr[9]/td/input[@value="Publish"]')
    inv_pub_sendto_chx = ('id', 'dialog_invoice_chksendtextmsg')
    inv_pub_sendAtt_chx = ('id', 'dialog_invoice_chkSendAttachment')
    pub_inv_loc = '//*[@class="dialog"]/div/span[text()="Publish Invoice"]/../../div[@class="dialog-func"]/input[@value="Publish"]'
    inv_pub_publish_btn = ('xpath', '/html/body/div[16]/div[3]/input[2]')
    inv_pub_markCustomVisible_btn = ('xpath', '//input[@value="Mark as Customer Visible"]')

    # Work Order history
    wohis_menu = ('id', 'nav_workorderhis')
    wohis_number_inbox = ('id', 'div_wonumber')
    wohis_search_inbox = ('xpath', '//*[@id="div_wonumber"]/div/div[2]/div/input')
    wohis_searchresult = ('xpath', '//*[@id="div_wonumber"]/div/div[2]/ul/li[1]')
    wohis_search_btn = ('xpath', '//*[@id="content1"]/div/div[2]/input[@value="Search"]')
    wohis_list = ('id', 'wohlist')  # tr为行内容

    # Widgets
    widgets_btn = ('id', 'spWdigets')  # 列表上Widgets按钮
    widget_select_all_chx = ('xpath', '//*[@id="dialog_widgets"]/div[2]/div[2]/div/table/tr/th[1]/div/span/label/layer')
    widget_list = '//*[@id="dialog_widgets"]/div[2]/div[2]/div/div[1]/div/table/tbody/'
    customercommunication_chx = ('xpath', widget_list + 'tr[1]/td[1]/label/layer')  # 第1行
    internalcomments_chx = ('xpath', widget_list + 'tr[2]/td[1]/label/layer')  # 第2行
    CRComments_chx = ('xpath', widget_list + 'tr[9]/td[1]/label/layer')  # 第9行

    widget_set_ok_btn = ('xpath', '//*[@id="dialog_widgets"]/div[3]/input[@value="OK"]')

    # Customer Communication元素
    entermessage_inbox = ('xpath', '//*[@id="workorderdetail"]/div/div/div[2]/div[1]/div/div[4]/textarea')
    communication_atta_link = ('xpath', '//*[@id="workorderdetail"]/div/div/div[2]/div[1]/div/div[4]/div/div[1]/div[2]/div')
    sendmessage_btn = ('xpath', '//*[@id="workorderdetail"]/div/div/div[2]/div[1]/div/div[4]/div/button')

    last_message_txt = ('xpath', '//*[@id="workorderdetail"]/div/div/div[2]/div[1]/div/div[5]/div[last()]/div[2]/span')
    last_message_status = ('xpath', '//*[@id="workorderdetail"]/div/div/div[2]/div[1]/div/div[5]/div[last()]/div[2]/div')
    last_message_time = ('xpath', '//*[@id="workorderdetail"]/div/div/div[2]/div[1]/div/div[5]/div[last()]/div[3]')
    # Communication 状态Tooltips
    comm_status_hove_update_btn = ('xpath', '//*[@id="workorderdetail"]/div/div/div[2]/div[1]/div/div[5]/div[last()]/div[2]/div/div/div[3]/div/div[@class="tip-function-button"]')
    upstatus_line1_value = ('xpath', '/html/body/div[@class="ui-popup-mask"]/div/div[2]/div[1]/div/div/div[1]/div/table/tr[1]/td[4]')
    upstatus_line1_sele = ('xpath', '/html/body/div[@class="ui-popup-mask"]/div/div[2]/div[1]/div/div/div[1]/div/table/tr[1]/td[4]/div/div[2]/ul/li[1]')
    upstatus_line2_sele = ('xapth', '/html/body/div[@class="ui-popup-mask"]/div/div[2]/div[1]/div/div/div[1]/div/table/tr[2]/td[4]/div/div[2]/ul/li[5]')
    upstatus_ok_btn = ('xpath', '/html/body/div[@class="ui-popup-mask"]/div/div[@class="ui-popup-footer"]/button[1]')

    # Internal Comments元素
    entercomments_inbox = ('xpath', '//*[@id="workorderdetail"]/div/div/div[2]/div[1]/div/div[2]/textarea')
    commentsatt_btn = ('xpath', '//*[@id="workorderdetail"]/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div')
    postnote_btn = ('xpath', '//button[@class="roundbtn button-post-note"]')
    comments_send_message_btn = ('xpath', '//button[@class="roundbtn button-send-message"]')

    # send internal comments界面元素
    sic_search_inbox = ('id', 'sendinternalcomments_search')
    sic_result_first_text_chx = ('xpath', '//*[@id="iccontactlist"]/div/div[1]/div/table/tbody/tr/td[3]/label/layer')
    sic_result_first_mail_chx = ('xpath', '//*[@id="iccontactlist"]/div/div[1]/div/table/tbody/tr/td[4]/label/layer')
    sic_phonenumber_inbox = ('id', 'sendic_phonenumber')
    sic_OK_btn = ('xpath', '//*[@id="sendicemailpopupdialog"]/div[3]/input[@value="OK"]')

    last_comments_txt = ('xpath', '//*[@id="workorderdetail"]/div/div/div[2]/div[1]/div/div[3]/div[last()]/div[2]/span')

    # Customer Record Comments
    crc_enter_comments_inbox = ('xpath', '//*[@id="workorderdetail"]/div/div/div[2]/div[1]/div/div[2]/textarea')
    crc_post_btn = ('xpath', '//*[@id="workorderdetail"]/div/div/div[2]/div[1]/div/div[2]/div/button')
    crc_last_comments_txt = ('xpath', '//*[@id="workorderdetail"]/div/div/div[2]/div[1]/div/div[3]/div[last()]/div[2]/span')

    # 查询
    def search(self, text):
        self.send_keys(self.inputtext_loc, text)
        self.click(self.searchbutton_loc)

    def inputTo(self, inboxloc, text):
        self.send_keys(inboxloc, text)