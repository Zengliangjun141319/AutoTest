# coding: utf-8

from Common.operater import Operater

class FuelRecordPage(Operater):

    # 左侧滑块中AssetHealth按钮
    assethealth_loc = ('xpath', ".//*[@id='divLeftTitle']/div[8]/div")

    # 左侧菜单中fuel records菜单
    fuelmenu_loc = ('xpath', ".//*[@id='nav_fuelrecord']/a/span")

    # Fuel Records iframe
    iframe_loc = ('xpath', ".//*[@id='set_right']/iframe")

    # Fuel Records管理页面查询条件
    begindate_loc = ('id', "startdatetxt")  # 开始时间
    enddate_loc = ('id', "enddatetxt") # 结束时间
    type_loc = ('id', "typeselectinput") # 机器类型
    searchinput_loc = ('id', "searchinputtxt") # 搜索输入框
    searchbutton_loc = ('xpath', ".//*[@id='recordcontent']/div[2]/input[2]")  # 搜索按钮

    deletebutton_loc = ('xpath', ".//*[@id='recordlist']/div/div[1]/div/table/tbody/tr[1]/td/a[@title='Delete']")
    checkdelete_loc = ('xpath', 'html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input[@value="Yes"]')

    addbutton_loc = ('xpath', ".//*[@id='recordcontent']/div[@class='function_title']/span[@class='sbutton iconadd']") # 新增按钮
    refreshB_loc = ('xpath', '//*[@id="recordcontent"]/div[@class="function_title"]/span[@class="sbutton iconrefresh"]')  # class="sbutton iconrefresh"

    # 新增窗口元素
    iframefuel_loc = ('id', "iframfuelrecord")   # 新增窗口iframe

    assetddicon_loc = ('xpath', ".//*[@id='dialog_machine']/div/div") # 机器下拉列表打开按钮
    assetselect_loc = ('xpath', ".//*[@id='dropdowndiv']/ul/li[7]") # 机器列表第7台机器
    transdate_loc = ('id', "dialog_transactiondate") # Transaction date时间控件
    transtimehour_loc = ('id', "dialog_timehour") # Transaction time hour下拉选择框
    transtimeminute_loc = ('id', "dialog_timeminute") # Transaction time minute下拉选择框
    ticketnumber_loc = ('id', "dialog_ticketnumber") # Ticket number输入框
    drivername_loc = ('id', "dialog_drivername") # Driver name输入框
    fuelingasset_loc = ('id', "dialog_rdofuelingasset") # Fueling asset单选按钮
    retailername_loc = ('id', "dialog_retailername") # retailer name输入框
    retaileraddress_loc = ('id', "dialog_retaileraddress") # retailer address输入框
    city_loc = ('id', "dialog_retailercity") # City输入框
    stateddicon_loc = ('xpath', ".//*[@id='dialog_retailerstate']/div/div") # State下拉框列表打开按钮
    stateselect_loc = ('xpath', ".//*[@id='dropdowndiv']/ul/li[2]") # State列表第二个选项
    zip_loc = ('id', "dialog_retailerzip") # Zip输入框
    odometer_loc = ('id', "dialog_odometer") # Odometer输入框
    odometeruom_loc = ('id', "dialog_odometeruom") # Odometer 单位下拉选择框
    fueltype_loc = ('id', "dialog_fueltype") # Fuel type下拉选择框
    brandname_loc = ('id', "dialog_brandname") # Brand name输入框
    measureunit_loc = ('xpath', ".//*[@id='dialog_unitofmeasure']/div/input") # Unit of measure输入框
    measureunitselect_loc = ('xpath', ".//*[@id='dropdowndiv']/ul/li[1]")  # Unit of measure第一个选项
    quantity_loc = ('id', "dialog_quantity") # Quantity输入框
    unitcost_loc = ('id', "dialog_unitcost") # Unit cost输入框
    totalcost_loc = ('id', "dialog_totalcost") # Total cost文本框
    notes_loc = ('id', "dialog_notes") # Notes输入框
    addfilebutton_loc = ('id', "uploadattfile") # Add File按钮

    # 保存及提示信息
    savebutton_loc = ('xpath', ".//*[@id='content1']/div[2]/div[1]/span[1]") # 保存按钮
    exitwithoutsave_loc = ('xpath', ".//*[@id='content1']/div[2]/div[1]/span[5]") # 不保存退出按钮
    alertmsg_loc = ('xpath', 'html/body/div[@class="dialog popupmsg"]/div[@class="dialog-content"]/div') # 提示信息
    alertokbutton_loc = ('xpath', 'html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input')

