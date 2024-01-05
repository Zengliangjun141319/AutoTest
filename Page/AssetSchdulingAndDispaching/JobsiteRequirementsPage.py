from operater import Operater
from Page.comms import *


class JobsiteRequirementsPage(Operater):
    # 左侧滑块大图标
    dispatchmenu_loc = ('xpath', '//div[@title="Asset Scheduling and Dispatching"]')

    # Jobsite Requirements菜单元素
    exButton_loc = ('xpath', '//*[@id="nav_arrow"]')    # 左边菜单收折按钮
    requirementsManage_loc = ('id', 'nav_jobsiterequirements')    # Jobsite Requirements菜单

    # Jobsite Requirements列表元素
    iframe_loc = ('xpath', '//*[@id="set_right"]/iframe')  # Jobsite Requirement列表
    latestDate_loc = ('id', 'latesdatetxt')  # Latest Start Date输入框
    unscheduledBox_loc = ('id', 'chk_unscheduled')  # Unscheduled Requirements Only单选框
    # Begin date排序
    beginSort_loc = ('xpath', '//*[@id="jobsitelist"]/div/table/tr/th[1]/div')

    searchButton_loc = ('xpath', '//*[@id="contentctrl"]/div[2]/input[3]')  # 搜索按钮
    td4_loc = ('xpath', '//*[@id="schedulerlist"]/div/div/div/table/tbody/tr[1]/td[4]')  # 搜索后的机器名称
    addBtn_loc = ('xpath', '//*[@id="contentctrl"]/div[3]/span[1]')  # 添加按钮

    # 添加Jobsite Requirement页面的元素
    requirementIframe_loc = ('id', 'iframerequirements')  # Jobsite Requirement添加页面
    jobsiteSelect_loc = ('id', 'dialog_jobsite')  # Jobsite
    beginDate_loc = ('id', 'begindatetxt')  # Begin Date
    endDate_loc = ('id', 'enddatetxt')  # End Date
    assetTypeList_loc = ('xpath', '//*[@id="div_assettypes"]/div/div[1]/label[2]')  # Asset Type下拉列表
    assetType_loc = ('xpath', '//*[@id="div_assettypes"]/div/div[2]/ul/li[1]/input')  # 具体的Jobsite
    pointOfContact_loc = ('id', 'pointofcontacttxt')  # Point Of Contact:
    applyBtn_loc = ('id', 'search_requirements')  # Apply按钮
    manageAssetBtn_loc = ('xpath', '//*[@id="requirementlist"]/div/div/div/table/tbody/tr/td/a[@title="Manage Assets"]')  # ManageAsset按钮
    firstAsset_loc = ('xpath', '//*[@id="selectedmachinelist"]/div/div/div/table/tbody/tr[1]/td[1]/%s' % grid_ck) # 机器列表中的第一个机器
    selectAssetOKBtn_loc = ('xpath', '//*[@id="dialog_managemahchine"]/div[5]/input[2]')  # 机器选择页面OK按钮
    saveBtn_loc = ('xpath', '//*[@id="content1"]/div/div[1]/span[1]')   # save按钮
    continueBtn_loc = ('xpath', '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input[3]') # 保存提示对话框中的continue按钮
    deleteBtn_loc = ('xpath', '//*[@id="jobsitelist"]/div/div/div/table/tbody/tr[1]/td[13]/a')  # delete按钮
    deleteYesBtn_loc = ('xpath', yes_btn)  # delete对话框上的Yes按钮

    selectAttaassetOK_btn = ('id', 'btn_addattasset')

    #ViewChangeHistory相关元素
    viewChangeHistoryBtn_loc = ('xpath', '//*[@id="jobsitelist"]/div/div/div/table/tbody/tr[41]/td[14]/a') # ViewChangeHistory按钮
    requirementChangeHistory_loc = ('id', 'div_title')

    # View Deleted Records相关元素
    viewDeletedRecordsBtn_loc = ('xpath', '//*[@id="contentctrl"]/div[@class="function_title"]/span[@class="sbutton iconview"]')  # View Deleted Records按钮
    deletedJobsiteRequirements_loc = ('id', 'contentctrl')

    def inputTo(self, Inboxloc, text):
        self.send_keys(Inboxloc, text)