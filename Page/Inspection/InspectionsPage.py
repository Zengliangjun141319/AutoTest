from operater import Operater
import time
from Page.comms import *


class InspectionsPage(Operater):

    # 左侧滑块大图标
    inspection_loc = ('xpath', '//*[@id="divLeftTitle"]/div[@title="Inspection"]/div')

    # Inspections菜单元素
    exButton_loc = ('xpath', '//*[@id="nav_arrow"]')    # 左边菜单收折按钮
    # inspectionsMenu_loc = ('link text', 'Inspections')    # Inspections菜单
    inspectionsMenu_loc = ('xpath', '//*[@id="set_left"]/ul/li[@title="Inspections"]')

    # Inspections列表元素
    beginDate_loc = ('xpath', '//*[@id="set_right"]/div/div[1]/div[2]/span[2]/input')  # Begin Date搜索框
    endDate_loc = ('xpath', '//*[@id="set_right"]/div/div[1]/div[2]/span[5]/input')  # End Date搜索框
    searchBtn_loc = ('xpath', '//*[@id="set_right"]/div/div[1]/div[2]/input[@value="Search"]')  # Search按钮
    tableList_loc = ('xpath', '//*[@id="set_right"]/div/div[2]/div/div/div/table')

    CommittimeCol_loc = ('xpath', '//*[@id="set_right"]/div/div[2]/div/table/tr/th[@data-key="CommitTimeLocal"]')   # 提交时间

    # 编辑Inspections相关元素
    editBtn_loc = ('xpath', '//*[@id="set_right"]/div/div[2]/div/div/div/table/tbody/tr[1]/td/a[@title="Edit"]')  # Edit按钮
    saveBtn_loc = ('xpath', '//*[@id="right_popup"]/div/div[1]/span[1]')   # 编辑页面的Create按钮
    exitBtn_loc = ('xpath', '//*[@id="right_popup"]/div/div[1]/span[3]')  # 编辑页面的Exit按钮

    saveMessage_loc = ('xpath', msg_content)  # 提示对话框
    okBtn_loc = ('xpath', ok_btn)  # 提示对话框上的‘OK’按钮

    # Inspections Detail页面相关元素
    detailBtn_loc = ('xpath', '//*[@id="set_right"]/div/div[2]/div/div/div/table/tbody/tr[1]/td/a[@title="Detail"]')  # Detail按钮
    detailEditBtn_loc = ('id', 'button-edit')  # Detail页面的Edit按钮

    # Download PDF相关元素
    downloadBtn_loc = ('xpath', '//*[@id="set_right"]/div/div[2]/div/div/div/table/tbody/tr[1]/td/a[@title="Download PDF"]')  # Download PDF按钮

    # Print相关元素
    printBtn_loc = ('xpath', '//*[@id="set_right"]/div/div[2]/div/div/div/table/tbody/tr[1]/td/a[@title="Print"]')  # print按钮

    def search(self):
        self.clear(self.beginDate_loc)
        time.sleep(1)
        self.clear(self.endDate_loc)
        time.sleep(1)
        self.click(self.searchBtn_loc)
        time.sleep(1)

    def inputTo(self, Inboxloc, text):
        self.send_keys(Inboxloc, text)





