from operater import Operater
from time import sleep
from Page.comms import *


class ManageRentalsPage(Operater):
    # 左侧滑块大图标
    manageAssetLink_loc = ('xpath', '//div[@title="Manage Assets"]')

    # 机器管理菜单元素
    exButton_loc = ('xpath', '//*[@id="nav_arrow"]')    # 左边菜单收折按钮
    manageRentals_loc = ('id', 'nav_managrentals')       # 租赁管理菜单

    # 租赁管理列表元素
    iframe_loc = ('xpath', '//iframe[@class="set_iframe"]')  # 租赁管理主体页面内嵌的iframe
    startDate_loc = ('id', 'startdatetxt')  # 搜索条件开始时间
    endDate_loc = ('id', 'enddatetxt')  # 搜索条件结束时间
    searchInbox_loc = ('id', 'searchinputtxt')  # 搜索框
    searchBtn_loc = ('xpath', '//*[@id="recordcontent"]/table/tbody/tr[1]/td[4]/input[@value="Search"]')  # 搜索按钮
    addBtn_loc = ('id', 'btnAdd')  # 添加租赁按钮
    searchVendor_loc = ('xpath', '//*[@id="rentallist"]/div/div/div/table/tbody/tr/td[5]')   # 搜索结果中的vendor列

    # 租赁添加页面元素
    iframeRental_loc = ('id', 'iframerental')   # 添加租赁页面的iframe
    assetSelect_loc = ('id', 'dialog_machine')  # Asset下拉列表
    assetSelectOption_loc = ('xpath', '//*[@id="dialog_machine"]/option[2]') #选择Asset下拉列表中的第二个值
    outsideSelect_loc = ('id', 'dialog_outside')  # outside下拉列表
    vendor_loc = ('id', 'dialog_vendor')  # Rental Vendor文本框
    rate_loc = ('id', 'dialog_rentalrate')  # Rental Rate文本框
    term_loc = ('id', 'dialog_term')  # Rental Term文本框
    termUnit_loc = ('id', 'dialog_termunit')  # ental Term Unit下拉框
    billingDate_loc = ('id', 'dialog_rentaltermbillingdate')  # Rental Term Billing Date文本框
    billingCycleDays_loc = ('id', 'dialog_billingcycledays')  # Number of Days in Billing Cycle文本框
    rentalDate_loc = ('id', 'dialog_rentaldata')  # Rental Date On文本框
    projectReturnDate_loc = ('id', 'dialog_projectreturndate')  # Proj.Return Date文本框
    returnDate_loc = ('id', 'dialog_returndate')  # Return Date文本框
    poNumber_loc = ('id', 'dialog_ponumber')  # P.O.#文本框
    insuredValue_loc = ('id', 'dialog_insuredvalue')    # Insured Value文本框
    comments_loc = ('id', 'dialog_comments')  # Comments多行文本框

    # 保存对话框元素
    saveBtn_loc = ('xpath', '//*[@id="content1"]/div[2]/div[1]/span[1]')  # Save 按钮
    saveAndExitBtn_loc = ('xpath', '//*[@id="content1"]/div[2]/div[1]/span[2]')  # Save and Exit 按钮
    exitWithoutSavingBtn_loc = ('xpath', '//*[@id="content1"]/div[2]/div[1]/span[3]')  # exitWithoutSaving按钮
    saveDialog_loc = ('xpath', msg_content)  # 保存提示框
    saveDialogOkBtn_loc = ('xpath', ok_btn)  # 保存提示框上的OK按钮

    # 删除记录
    # 1102版本添加了一个字段，列表上删除按钮的位置后移1位   ---- 曾良均    2021.11.02
    deleteBtn_loc = ('xpath', '//*[@id="rentallist"]/div/div/div/table/tbody/tr[1]/td/a[@title="Delete"]')  # 删除记录按钮
    deleteDialogOkBtn_loc = ('xpath', yes_btn)  # 删除提示框上的Yes按钮

    # 编辑租赁相关元素
    # 1102版本添加了一个字段，列表上编辑按钮的位置后移1位   ---- 曾良均    2021.11.02
    editBtn_loc = ('xpath', '//*[@id="rentallist"]/div/div/div/table/tbody/tr/td[15]/a')

    def search(self, text):
        self.clear(self.startDate_loc)
        self.clear(self.endDate_loc)
        self.send_keys(self.searchInbox_loc, text)
        sleep(1)
        self.click(self.searchBtn_loc)
        sleep(1)

    def inputTo(self, Inboxloc, Texts):
        '''
        定义的通用方法，两个参数：输入框位置，输入内容
        usage:
        InputTo(SNInbox_loc, 'SNInfo')
        '''
        self.send_keys(Inboxloc, Texts)