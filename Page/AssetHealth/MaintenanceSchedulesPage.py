from Common.operater import Operater

class MaintenanceSchedulesPage(Operater):
    # 左侧滑块大图标
    assetHealth_loc = ('xpath', '//*[@id="divLeftTitle"]/div[8]/div')

    # Maintenance Schedules菜单元素
    exButton_loc = ('xpath', '//*[@id="nav_arrow"]')  # 左边菜单收折按钮
    maintenanceSchedules_loc = ('link text', 'Maintenance Schedules')  # Maintenance Schedules菜单

    # Maintenance Schedules列表元素
    iframe_loc = ('xpath','//*[@id="set_right"]/iframe')
    addBtn_loc = ('xpath', '//*[@id="content1"]/div[1]/div[3]/span[1]')  # Add按钮
    planSelect_loc = ('id','sel_plan') # 查询条件中的Plan下拉列表
    searchScheduleName_loc = ('xpath', '//*[@id="pm_tbody"]/tr[1]/td[1]/div') # 搜索出的schedule名称
    manageSchedule_loc = ('xpath','//*[@id="pm_tbody"]/tr[1]/td[5]') # 列表中的Manage schedule链接


    # 添加PM页面的元素
    planName_loc = ('id', 'sc_name')
    planType_loc = ('id', 'sc_plantype')
    description_loc = ('id', 'sc_notes')
    saveBtn_loc = ('xpath', '//*[@id="content1"]/div[1]/div[2]/span[1]')
    saveAndExitBtn_loc = ('xpath', '//*[@id="content1"]/div[1]/div[2]/span[2]')
    exitWithoutSaving_loc = ('xpath','//*[@id="content1"]/div[1]/div[2]/span[3]')
    msgBox_loc = ('xpath','/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-content"]/div[@class="dialog-text"]')
    msgOKBtn_loc = ('xpath','/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input')

    # Add Interval相关元素
    addIntervalBtn_loc = ('xpath', '//*[@id="th_intervals"]/table/thead/tr/th[8]/a[1]')  # Add Interval按钮
    serviceName_loc = ('id', 'dig_name')  # Service Name
    interval_loc = ('id', 'dig_interval')  # Interval
    notificationPeriod_loc = ('id', 'dig_period')  # Notification Period
    recurring_loc = ('id', 'dig_recurring')  # Recurring
    serviceDescription_loc = ('id', 'dig_servicedec')  # Service Description
    expectedCost_loc = ('id', 'dig_expectedcost')  # Expected Cost
    priority_loc = ('id', 'dig_priority')  # Priority
    addIntervalOKBtn_loc = ('xpath', '//*[@id="dialog_interval"]/div[3]/input[2]')

    # Manage Assets相关元素
    manageAssetsBtn_loc = ('xpath', '//*[@id="pm_tbody"]/tr[1]/td[6]')  # Manage assets按钮
    addAssetsBtn_loc = ('xpath', '//*[@id="content1"]/div[1]/div[4]/table/thead/tr[5]/td/div/input[4]')  # Add按钮
    firstAsset_loc = ('xpath', '//*[@id="dialog_assets"]/div[2]/div[4]/div/div/div/table/tbody/tr[1]/td[1]/input')  # 机器选择页面的第一个机器
    selectAssetOKBtn_loc = ('xpath', '//*[@id="dialog_assets"]/div[3]/input[2]')  # 机器选择页面的OK按钮
    setAssetOKBtn_loc_loc = ('xpath', '//*[@id="dialog_selectedassets"]/div[3]/input[2]') # 设置机器信息页面的OK按钮
    saveAssetBtn_loc = ('xpath', '//*[@id="content1"]/div[1]/div[4]/table/thead/tr[5]/td/div/input[3]') # 保存机器按钮
    saveAssetDialog_loc = ('xpath', '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-content"]/div') # 保存机器提示对话框
    saveAssetDialogOKBtn_loc = ('xpath', '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input') # 保存机器提示对话框上的OK按钮
    backBtn_loc = ('xpath','//*[@id="content1"]/div[1]/div[1]/span[1]')

    # Edit Interval相关元素
    expandIntervalsBtn_loc = ('id', 'expandintervals')  # Expand Intervals按钮
    listServiceName_loc = ('xpath', '//*[@id="pm_tbody"]/tr[2]/td/table/tbody/tr/td[1]/input')  # 列表中要编辑的Service Name
    listSaveServiceBtn_loc = ('xpath', '//*[@id="pm_tbody"]/tr[2]/td/table/tbody/tr/td[8]/div[2]/input[1]') # 列表中Service的保存按钮

    # delete schedule相关元素
    deleteScheduleBtn_loc = ('xpath', '//*[@id="pm_tbody"]/tr[1]/td[4]')  # 删除schedule按钮
    deleteScheduleYesBtn_loc = ('xpath', '/html/body/div[3]/div[3]/input[2]') # 删除对话框中的Yes按钮
    deleteResult_loc = ('xpath','//*[@id="pm_tbody"]/tr/td') # 删除后的搜索结果

    def inputTo(self, Inboxloc, text):
        self.send_keys(Inboxloc, text)