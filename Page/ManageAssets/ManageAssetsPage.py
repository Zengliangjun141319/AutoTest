from operater import Operater
from time import sleep
from Page.comms import *


class ManageAssetsPage(Operater):
    # 外侧主菜单
    HomeButton_loc = ('id', 'button_home')
    # Home页元素
    ManageAssetLink_loc = ('xpath', '//*[@id="sysModules"]/div[7]')
    ManageAssetBtn_loc = ('xpath', '//*[@id="divLeftTitle"]/div[@title="Manage Assets"]')

    # 左侧菜单元素
    ExButton_loc = ('xpath', '//*[@id="nav_arrow"]')    # 左边菜单收折按钮
    ManageAssets_loc = ('id', 'nav_managmachines')    # 机器管理菜单
    ManageRetals_loc = ('id', 'nav_managrentals')        # 租赁管理菜单
    AssetGroup_loc = ('id', 'nav_machinegroups')        # 机器组
    ManageDevices_loc = ('id', 'nav_managegpsdevices')    # 设备管理
    ManageModel_loc = ('id', 'nav_managmodels')        # 制造商管理

    # 机器管理页面元素
    iframe = ('xpath', '//*[@id="set_right"]/iframe')     # 机器管理主体页面是内嵌的iframe
    SearchInbox_loc = ('id', 'searchinputtxt')    # 搜索输入框
    # SearchButton_loc = ('value', 'Search')  //*[@id="recordcontent"]/div[2]/input[3]
    SearchButton_loc = ('xpath', '//*[@id="recordcontent"]/div[2]/input[@value="Search"]')
    # //*[@id="machinelist"]/div/div[1]/div/table/tbody/tr/td[1]/span
    searchvin_loc = ('xpath', '//*[@id="machinelist"]/div/div/div/table/tbody/tr/td[1]')
    sorts = ('xpath', '//*[@id="machinelist"]/div/table/tr/th[@data-key="Odometer"]/span')
    odo_column = ('xpath', '//*[@id="machinelist"]/div/table/tr/th[@data-key="Odometer"]')
    odos = ('xpath', '//*[@id="machinelist"]/div/div[1]/div/table/tbody/tr[1]/td[10]/span')

    # 删除机器菜单
    deleteAssetMenu_loc = ('xpath', '//*[@id="recordcontent"]/div[@class="function_title"]/span[@class="sbutton icondelete"]')
    deleteAsset_loc = ('xpath', '//*[@id="machinelist"]/div/div/div/table/tbody/tr/td/a[@title="Delete Asset"]')
    deleteYes_loc = ('xpath', yes_btn)

    ShowHiddenCheck_loc = ('id', 'chkShowHidden')
    # AddButton_loc = ('id', 'btnAdd')
    AddButton_loc = ('xpath', '//*[@id="btnAdd"]')
    EditButton_loc = ('id', 'btnEdit')
    RefreshBt_loc = ('xpath', '//*[@id="recordcontent"]/div[@class="function_title"]/span[@class="sbutton iconrefresh"]')

    # 导出Excel
    exportToBtn_loc = ('xpath', '//*[@id="recordcontent"]/div[@class="function_title"]/span[@class="sbutton iconexport"]')

    # Import元素
    importBtn_loc = ('xpath', '//*[@id="recordcontent"]/div[@class="function_title"]/span[@class="sbutton iconimport"]')
    importMappingOk_loc = ('xpath', '//*[@id="dialog_import"]/div[@class="dialog-func"]/input[@value="OK"]')
    importOk_loc = ('xpath', ok_btn)
    importImp_loc = ('id', 'btnOk')
    importCloseBtn_loc = ('id', 'btnClose')

    # 界面元素增加后为： //*[@id="machinelist"]/div/div[1]/div/table/tbody/tr/td[21]
    ListHideck_loc = ('xpath', '//*[@id="machinelist"]/div/div[1]/div/table/tbody/tr/td[22]/%s' % grid_ck)
    # ListHideck_loc = ('id', 'body_checkbox_row_0')

    # 新建编辑机器页面元素
    iframemachine = ('id', 'iframemachine')    # 机器编辑界面
    SaveButton_loc = ('xpath', '//*[@id="div_content"]/div[@class="function_title"]/span[1]')        # 保存
    SaveExitButton_loc = ('xpath', '//*[@id="div_content"]/div[@class="function_title"]/span[2]')    # 保存并退出
    ExitSaveButton_loc = ('xpath', '//*[@id="div_content"]/div[@class="function_title"]/span[3]')    # 不保存退出

    CheckHide_loc = ('id', 'dialog_hide')
    CheckOnRoad_loc = ('id', 'dialog_onroad')
    CheckTelematics_loc = ('id', 'dialog_telematics')
    CheckAttachment_loc = ('id', 'dialog_attachment')

    SNInbox_loc = ('id', 'dialog_sn')
    NameInbox_loc = ('id', 'dialog_name')
    CustomNameInbox_loc = ('id', 'dialog_name2')
    YearInbox_loc = ('id', 'dialog_year')
    MakeSelect_loc = ('id', 'dialog_make')
    AddMakeButton_loc = ('id', 'btnAddMake')
    ModelSelect_loc = ('id', 'dialog_model')
    AddModelButton_loc = ('id', 'btnAddModel')
    EClass_loc = ('id', 'dialog_eqclass')
    TypeSelect_loc = ('id', 'dialog_type')
    DescInbox_loc = ('id', 'dialog_description')
    AcquisitionSelect_loc = ('id', 'dialog_AquisitionType')

    # Layout
    # Layout_loc = ('xpath', '//*[@id="recordcontent"]/div[@class="function_title"]/span[@class="sbutton iconlayout"]')
    Layout_loc = ('xpath', '//*[@id="recordcontent"]/div[3]/span[@class="sbutton iconlayout"]')
    SelectAll_loc = ('xpath', '//*[@id="dialog_layouts"]/div[2]/div/div/table/tr[1]/th[3]/div/input')
    Selectlist_loc = ('xpath', '//*[@id="dialog_layouts"]/div[2]/div/div/div/div/table')  # /tr[2]/td[3]/input')

    LayoutOKBT_loc = ('xpath', '//*[@id="dialog_layouts"]/div[@class="dialog-func"]/input[2]')

    # ResetLayout_loc = ('xpath', '//*[@id="recordcontent"]/div[@class="function_title]/span[@class="sbutton iconresetlayout"]')
    ResetLayout_loc = ('xpath', '//*[@id="recordcontent"]/div[3]/span[@class="sbutton iconresetlayout"]')
    ResetLayoutOk_loc = ('xpath', yes_btn)

    # 定义方法：搜索内容
    def SearchAssets(self, Texts):
        self.send_keys(self.SearchInbox_loc, Texts)
        sleep(1)
        self.click(self.SearchButton_loc)
        sleep(2)

    # 定义方法：输入内容
    def InputTo(self, Inboxloc, Texts):
        '''
        定义的通用方法，两个参数：输入框位置，输入内容
        usage:
        InputTo(SNInbox_loc, 'SNInfo')
        '''
        self.send_keys(Inboxloc,Texts)
