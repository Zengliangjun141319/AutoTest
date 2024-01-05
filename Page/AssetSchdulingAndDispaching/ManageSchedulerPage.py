from operater import Operater
from time import sleep

class ManageSchedulerPage(Operater):

    # 左侧滑块大图标
    dispatchmenu_loc = ('xpath', '//div[@title="Asset Scheduling and Dispatching"]')

    # Asset Scheduling菜单元素
    exButton_loc = ('xpath', '//*[@id="nav_arrow"]')    # 左边菜单收折按钮
    schedulerManage_loc = ('id', 'nav_scheduler')    # Scheduler菜单

    # Scheduler列表元素
    iframe_loc = ('xpath', '//*[@id="set_right"]/iframe')
    beginDateSearch_loc = ('id', 'txtbegindate') # Begin Date搜索条件
    searchInbox_loc = ('id', 'searchinputtxt') # 搜索文本框
    searchButton_loc = ('xpath', '//*[@id="contentctrl"]/div[2]/input[2]')  # 搜索按钮
    td4_loc = ('xpath','//*[@id="schedulerlist"]/div/div/div/table/tbody/tr[1]/td[4]') #搜索后的机器名称
    addBtn_loc = ('xpath', '//*[@id="contentctrl"]/div[@class="function_title"]/span[@class="sbutton iconadd"]')  # 添加按钮
    refreshBtn_loc = ('xpath', '//*[@id="contentctrl"]/div[@class="function_title"]/span[@class="sbutton iconrefresh"]')

    # 添加scheduler页面的元素
    schedulerIframe_loc = ('id', 'iframescheduler') # scheduler添加页面
    assetList_loc = ('xpath', '//*[@id="dialog_machine"]/div/div[1]')  # Asset下拉列表
    asset_loc = ('xpath', '//*[@id="dialog_machine"]/div/div[1]/label[2]')  # 选择Asset
    jobsite_loc = ('id', 'dialog_jobsite') # Jobsite
    beginDate_loc = ('id', 'dialog_begindate') # Begin Date
    endDate_loc = ('id', 'dialog_enddate') # End Date
    notes_loc = ('id', 'dialog_notes') # Notes
    saveBtn_loc = ('xpath', '//*[@id="content1"]/div/div[1]/span[1]')   # save按钮
    exitWithoutSavingBtn_loc = ('xpath', '//*[@id="content1"]/div/div[1]/span[3]')  # exit without saving按钮

    def search(self,text):
        self.send_keys(self.searchInbox_loc, text)
        sleep(1)
        self.click(self.searchButton_loc)
        sleep(1)

    def inputTo(self, Inboxloc, text):
        self.send_keys(Inboxloc, text)





