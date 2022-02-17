from Common.operater import Operater
import time

class InspectionsPage(Operater):

    # 左侧滑块大图标
    inspection_loc = ('xpath', '//*[@id="divLeftTitle"]/div[@title="Inspection"]/div')

    # Inspections菜单元素
    exButton_loc = ('xpath', '//*[@id="nav_arrow"]')    # 左边菜单收折按钮
    inspectionsMenu_loc = ('link text', 'Inspections')    # Inspections菜单

    # Inspections列表元素
    beginDate_loc = ('xpath', '//*[@id="set_right"]/div/div[1]/div[2]/span[2]/input')  # Begin Date搜索框
    endDate_loc = ('xpath', '//*[@id="set_right"]/div/div[1]/div[2]/span[5]/input')  # End Date搜索框
    searchBtn_loc = ('xpath', '//*[@id="set_right"]/div/div[1]/div[2]/input[2]')  # Search按钮
    tableList_loc = ('xpath','//*[@id="set_right"]/div/div[2]/div/div/div/table')

    # 编辑Inspections相关元素
    # //*[@id="set_right"]/div/div[2]/div/div[1]/div/table/tbody/tr[1]/td[14]/a
    editBtn_loc = ('xpath', '//*[@id="set_right"]/div/div[2]/div/div/div/table/tbody/tr[1]/td[14]/a')  # Edit按钮
    saveBtn_loc = ('xpath', '//*[@id="right_popup"]/div/div[1]/span[1]')   # 编辑页面的Create按钮
    exitBtn_loc = ('xpath', '//*[@id="right_popup"]/div/div[1]/span[3]')  # 编辑页面的Exit按钮

    saveMessage_loc = ('xpath', '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-content"]/div')  # 提示对话框
    okBtn_loc = ('xpath', '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input')  # 提示对话框上的‘OK’按钮

    # Inspections Detail页面相关元素
    #  //*[@id="set_right"]/div/div[2]/div/div[1]/div/table/tbody/tr[1]/td[15]/a
    detailBtn_loc = ('xpath', '//*[@id="set_right"]/div/div[2]/div/div/div/table/tbody/tr[1]/td[15]/a')  # Detail按钮
    detailEditBtn_loc = ('id', 'button-edit')  # Detail页面的Edit按钮

    # Download PDF相关元素
    downloadBtn_loc = ('xpath', '//*[@id="set_right"]/div/div[2]/div/div/div/table/tbody/tr[1]/td[16]/a')  # Download PDF按钮

    # Print相关元素
    printBtn_loc = ('xpath', '//*[@id="set_right"]/div/div[2]/div/div/div/table/tbody/tr[1]/td[17]/a')  # print按钮

    def search(self):
        self.clear(self.beginDate_loc)
        time.sleep(1)
        self.clear(self.endDate_loc)
        time.sleep(1)
        self.click(self.searchBtn_loc)
        time.sleep(1)

    def inputTo(self, Inboxloc, text):
        self.send_keys(Inboxloc, text)





