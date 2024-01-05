from operater import Operater
from time import sleep
from Page.comms import *


class ShareAssetsPage(Operater):
    # 外侧主菜单
    HomeButton_loc = ('id', 'button_home')
    # Home页元素
    ManageAssetLink_loc = ('xpath', '//*[@id="sysModules"]/div[7]')
    ManageAssetBtn_loc = ('xpath', '//*[@id="divLeftTitle"]/div[7]')

    # 左侧菜单
    ExButton_loc = ('xpath', '//*[@id="nav_arrow"]')  # 左边菜单收折按钮
    ShareAssets_loc = ('id', 'nav_shareasset')

    # 共享机器页面元素
    iframe_loc = ('xpath', '//*[@id="set_right"]/iframe')
    searchInbox_loc = ('id', 'searchinputtxt')
    searchBtn_loc = ('xpath', '//*[@id="recordcontent"]/div[@class="search_bar"]/input[@value="Search"]')
    showHiddenChx_loc = ('id', 'chkShowHidden')    # 勾选显示隐藏机器

    ShareBtn_loc = ('xpath', '//*[@id="recordcontent"]/div[@class="function_title"]/span[@class="sbutton iconshare"]')   # 共享
    unShareBtn_loc = ('xpath', '//*[@id="recordcontent"]/div[@class="function_title"]/span[@class="sbutton iconunshare"]')    # 取消共享
    Refresh_loc = ('xpath', '//*[@id="recordcontent"]/div[@class="function_title"]/span[@class="sbutton iconrefresh"]')
    Layout_loc = ('xpath', '//*[@id="recordcontent"]/div[@class="function_title"]/span[@class="sbutton iconlayout"]')
    ResetLayout_loc = ('xpath', '//*[@id="recordcontent"]/div[@class="function_title"]/span[@class="sbutton iconresetlayout"]')

    # 布局相关
    ResetLayoutYes_loc = ('xpath', yes_btn)
    allColumnChx_loc = ('xpath', '//*[@id="dialog_layouts"]/div[2]/div/div/table/tr[1]/th[3]/div/input')
    vinChx_loc = ('xpath', '//*[@id="dialog_layouts"]/div[2]/div/div/div/div/table/tr[1]/td[3]/input')
    sharewith_loc = ('xpath', '//*[@id="dialog_layouts"]/div[2]/div/div/div/div/table/tr[4]/td[3]/input')
    setLayoutOk_loc = ('xpath', '//*[@id="dialog_layouts"]/div[@class="dialog-func"]/input[2]')

    # 列表标题行
    fullSelect_loc = ('xpath', '//*[@id="machinelist"]/div[2]/table/tr/th[1]/div/span/label/layer')
    #  406版本之前 全选 的位置 ('id', 'header_checkbox_column_0')
    VINColumn_loc = ('xpath', '//*[@id="machinelist"]/div/table/tr/th[@data-key="VIN"]/div/span')

    # 第一行数据
    Sharedwith_loc = ('xpath', '//*[@id="machinelist"]/div/div[1]/div/table/tbody/tr/td[5]/span')
    ExpectedDate_loc = ('xpath', '//*[@id="machinelist"]/div/div[1]/div/table/tbody/tr/td[7]/span')
    ShareAsset_loc = ('xpath', '//*[@id="machinelist"]/div/div[1]/div/table/tbody/tr/td/a[@title="Share Asset"]')
    unshareAsset_loc = ('xpath', '//*[@id="machinelist"]/div/div[1]/div/table/tbody/tr/td/a[@title="UnShare Asset"]')

    # Share窗口
    shareText_loc = ('xpath', '//*[@id="tab_assetinfo"]/tbody/tr[1]/td[1]')
    sharelist_loc = ('id', 'dialog_sharewith')
    enddate_loc = ('id', 'dialog_enddate')
    hideon_loc = ('id', 'dialog_hideasset')
    OKBtn_loc = ('xpath', '//*[@id="dialog_share"]/div[@class="dialog-content"]/div/input[@value="OK"]')
    CancelBtn_loc = ('xpath', '//*[@id="dialog_share"]/div[@class="dialog-content"]/div/input[@value="Cancel"]')

    confirmYes_loc = ('xpath', yes_btn)

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
        self.send_keys(Inboxloc, Texts)