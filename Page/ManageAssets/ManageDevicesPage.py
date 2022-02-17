from Common.operater import Operater
from time import sleep

class ManageDevicesPage(Operater):
    # 左侧滑块大图标
    manageAssetLink_loc = ('xpath', '//div[@title="Manage Assets"]')

    # 机器管理菜单元素
    exButton_loc = ('xpath', '//*[@id="nav_arrow"]')  # 左边菜单收折按钮
    manageDevices_loc = ('id', 'nav_managegpsdevices')  # 设备管理

    # 设备管理列表元素
    iframe_loc = ('xpath', '//iframe[@class="set_iframe"]')  # 机器组主体页面内嵌的iframe
    searchInbox_loc = ('id', 'searchinputtxt')  # 搜索框
    searchBtn_loc = ('xpath', '//*[@id="recordcontent"]/div[2]/input[2]')  # 搜索按钮
    addBtn_loc = ('xpath', '//*[@id="recordcontent"]/div[3]/span[@class="sbutton iconadd"]')  # 添加设备按钮
    searchSN_loc = ('xpath', '//*[@id="devicelist"]/div/div/div/table/tbody/tr/td[1]')  # 搜索出的设备的SN
    searchNotes_loc = ('xpath','//*[@id="devicelist"]/div/div/div/table/tbody/tr/td[7]')   # 搜索出的设备的Notes

    # 添加设备页面元素
    addDeviceIframe_loc = ('id', 'iframe_gpsdevice') # 添加设备页面iframe
    saveBtn_loc = ('xpath', '//*[@id="content1"]/div[1]/span[1]')    # save按钮
    saveAndExitBtn_loc = ('xpath', '//*[@id="content1"]/div[1]/span[2]')    # save and exit按钮
    exitWithoutSavingBtn_loc = ('xpath', '//*[@id="content1"]/div[1]/span[3]')   # exit without saving按钮

    selectSource_loc = ('id','dialog_source') # Source下拉列表框
    deviceId_loc = ('id','dialog_sn')   # Device Air Id
    deviceEsn_loc = ('id','dialog_asn') # Device ESN
    deviceType_loc = ('id','dialog_devicetype') # Device Type
    deviceStatus_loc = ('id', 'dialog_status')  # Status
    invoiceDate_loc = ('id', 'dialog_invoicedate')  # Invoice Date
    invoiceNo_loc = ('id', 'dialog_invoiceno')  # Invoice
    startDate_loc = ('id', 'dialog_servicestartdate')   # Service Start Date
    notes_loc = ('id', 'dialog_notes')  # Notes

    saveDialog_loc = ('xpath','/html/body/div[6]/div[2]/div') # save后的对话框
    saveDialogOkBtn_loc = ('xpath', '/html/body/div[6]/div[3]/input')   # 对话框上的OK按钮

    # 编辑设备相关元素
    editDeviceBtn_loc = ('xpath','//*[@id="devicelist"]/div/div/div/table/tbody/tr[1]/td[19]') # 编辑设备按钮

    # Notes相关元素
    notesBtn_loc = ('xpath','//*[@id="devicelist"]/div/div/div/table/tbody/tr[1]/td[20]/a') # Notes按钮
    notesText_loc = ('id','dialog_comments') # Notes文本框
    sendNotesBtn_loc = ('xpath','//*[@id="tab_comments"]/div/div[1]/table/tbody/tr/td/div/div/span') # 发送Notes按钮
    sendedNotes_loc = ('xpath','//*[@id="divcomments"]/div[1]/div[2]') # 发送后的Notes内容


    def search(self, text):
        self.send_keys(self.searchInbox_loc, text)
        sleep(1)
        self.click(self.searchBtn_loc)
        sleep(3)

    def inputTo(self, inBoxloc, text):
        self.send_keys(inBoxloc, text)






