from Common.operater import Operater
from time import sleep

class AseetGroupsPage(Operater):
    # 左侧滑块大图标
    manageAssetLink_loc = ('xpath', '//div[@title="Manage Assets"]')

    # 机器管理菜单元素
    exButton_loc = ('xpath', '//*[@id="nav_arrow"]')    # 左边菜单收折按钮
    assetGroup_loc = ('id', 'nav_machinegroups')        # 机器组菜单

    # 机器组管理列表元素
    iframe_loc = ('xpath', '//iframe[@class="set_iframe"]')   # 机器组主体页面内嵌的iframe
    searchInbox_loc = ('id', 'searchinputtxt')    # 搜索框
    searchBtn_loc = ('id', 'search')   # 搜索按钮
    addBtn_loc = ('xpath', '//*[@id="recordcontent"]/div[3]/span[@class="sbutton iconadd"]')   # 添加机器组按钮
    deleteBtn_loc = ('xpath', '//*[@id="grouplist"]/div/div/div/table/tbody/tr[1]/td[5]/a')    # 删除机器按钮
    td1_loc = ('xpath', '//*[@id="grouplist"]/div/div/div/table/tbody/tr[1]/td[1]')    #列 表第一个机器组的名称

    # 机器组管理页面元素
    iframeMachineGroup_loc = ('id', 'iframe_machinegroup')  # 添加机器组页面又是iframe
    saveBtn_loc = ('xpath', '//*[@id="div_content"]/div[2]/span[1]')    # save按钮
    saveAndExitBtn_loc = ('xpath', '//*[@id="div_content"]/div[2]/span[2]')    # save and exit按钮
    exitWithoutSavingBtn_loc = ('xpath', '//*[@id="div_content"]/div[2]/span[3]')   # exit without saving按钮
    groupName_loc = ('id', 'dialog_groupname')  # Group Name文本框
    groupCode_loc = ('id', 'dialog_groupcode')  # Code文本框
    description_loc = ('id', 'dialog_description')  # Description多行文本框

    addAssetsBtn_loc = ('xpath', '//*[@id="divcontent"]/div/span[3]')   # 添加机器按钮
    firstAsset_loc = ('xpath', '//*[@id="dialog_machines"]/div[2]/div[4]/div/div/div/table/tbody/tr[1]/td[1]/input') # 机器选择页面的第一台机器
    assetOkBtn_loc = ('xpath', '//*[@id="dialog_machines"]/div[3]/input[2]')    # 机器复选框

    saveDialog_loc = ('xpath','/html/body/div[5]/div[2]') # save后的对话框
    saveDialogOkBtn_loc = ('xpath', '/html/body/div[5]/div[3]/input')   # 对话框上的OK按钮

    # 删除机器组相关元素
    deleteBtn_loc = ('xpath','//*[@id="grouplist"]/div/div/div/table/tbody/tr[1]/td[5]') # 删除机器组按钮
    deleteDialogOkBtn_loc = ('xpath','/html/body/div[3]/div[3]/input[2]') #确认删除按钮

    # 编辑机器组相关元素
    editBtn_loc = ('xpath', '//*[@id="grouplist"]/div/div/div/table/tbody/tr[1]/td[4]')


    # 定义方法：搜索内容
    def search(self, text):
        self.send_keys(self.searchInbox_loc, text)
        sleep(1)
        self.click(self.searchBtn_loc)
        sleep(1)

    # 定义方法：输入内容
    def inputTo(self, Inboxloc, Texts):
        '''
        定义的通用方法，两个参数：输入框位置，输入内容
        usage:
        InputTo(SNInbox_loc, 'SNInfo')
        '''
        self.send_keys(Inboxloc,Texts)