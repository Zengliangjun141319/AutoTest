from operater import Operater
from time import sleep
from Page.comms import *


class ManageJobsitePage(Operater):

    # 左侧滑块大图标
    dispatchmenu_loc = ('xpath', '//div[@title="Asset Scheduling and Dispatching"]')

    # 机器管理菜单元素
    exButton_loc = ('xpath', '//*[@id="nav_arrow"]')    # 左边菜单收折按钮
    jobsiteManage_loc = ('id', 'nav_jobsitemanage')        # Job Sites菜单

    # job Sites列表元素
    iframe_loc = ('xpath', '//*[@id="set_right"]/iframe')
    table = ('xpath','//*[@id="jobsitelist"]/div/div/div/table')
    searchInbox_loc = ('id', 'searchinputtxt')
    searchButton_loc = ('xpath', '//*[@id="contentctrl"]/div[2]/input[@value="Search"]')  # 搜索按钮
    # 2.22.113增加了一列
    # 删除按钮的位置变更之前： //*[@id="jobsitelist"]/div/div[]/div/table/tbody/tr[1]/td[26]
    deleteBtn_loc = ('xpath', '//*[@id="jobsitelist"]/div/div/div/table/tbody/tr[1]/td/a[@title="Delete"]')    # 列表中的删除按钮
    addBtn_loc = ('xpath', '//div/span[@class="sbutton iconadd"]')  # 添加按钮
    refreshBtn_loc = ('xpath', '//*[@id="contentctrl"]/div[@class="function_title"]/span[@class="sbutton iconrefresh"]')

    # import相关元素
    importBtn_loc = ('xpath', '//*[@id="contentctrl"]/div[@class="function_title"]/span[@class="sbutton iconimport"]') # Import按钮
    matchOKBtn_loc = ('xpath', '//*[@id="dialog_import"]/div[4]/input[2]')  # Import列匹配页面OK按钮
    importOKBtn_loc = ('xpath', ok_btn)  # Import对话框OK按钮

    # Layout相关元素
    layoutBtn_loc = ('xpath','//*[@id="contentctrl"]/div[@class="function_title"]/span[@class="sbutton iconlayout"]') # Layout按钮
    # selectAll_loc = ('xpath','//*[@id="dialog_layouts"]/div[2]/div/div/table/tr[1]/th[3]/div[@class="data-column-header-text"]/input[@class="data-column-header-checkbox"]') # Layout页面全选按钮
    selectAll_loc = ('xpath','/html/body/div[2]/div[2]/div/div/table/tr[1]/th[3]/div/input[@class="data-column-header-checkbox"]')
    # selectAll_loc = ('xpath','//*[@id="dialog_layouts"]//[@class="data-column-header-checkbox"]')

    nameLayout_loc = ('xpath', '//*[@id="dialog_layouts"]/div[2]/div/div/div/div/table/tr[1]/td[3]')  # Layout设置页面第一个列
    regionLayout_loc = ('xpath', '//*[@id="dialog_layouts"]/div[2]/div/div/div/div/table/tr[2]/td[3]')  # Layout设置页面第二个列
    numberLayout_loc = ('xpath', '//*[@id="dialog_layouts"]/div[2]/div/div/div/div/table/tr[3]/td[3]')  # Layout设置页面第三个列
    codeLayout_loc = ('xpath', '//*[@id="dialog_layouts"]/div[2]/div/div/div/div/table/tr[4]/td[3]')
    typesLayout_loc = ('xpath', '//*[@id="dialog_layouts"]/div[2]/div/div/div/div/table/tr[5]/td[3]')
    latitudeLayout_loc = ('xpath', '//*[@id="dialog_layouts"]/div[2]/div/div/div/div/table/tr[6]/td[3]')
    longitudeLayout_loc = ('xpath', '//*[@id="dialog_layouts"]/div[2]/div/div/div/div/table/tr[7]/td[3]')
    colorLayout_loc = ('xpath', '//*[@id="dialog_layouts"]/div[2]/div/div/div/div/table/tr[8]/td[3]')
    radiusLayout_loc = ('xpath', '//*[@id="dialog_layouts"]/div[2]/div/div/div/div/table/tr[9]/td[3]')
    bindingtoAssetLayout_loc = ('xpath', '//*[@id="dialog_layouts"]/div[2]/div/div/div/div/table/tr[10]/td[3]')
    foremanLayout_loc = ('xpath', '//*[@id="dialog_layouts"]/div[2]/div/div/div/div/table/tr[11]/td[3]')
    startDateLayout_loc = ('xpath', '//*[@id="dialog_layouts"]/div[2]/div/div/div/div/table/tr[12]/td[3]')
    endDateLayout_loc = ('xpath', '//*[@id="dialog_layouts"]/div[2]/div/div/div/div/table/tr[13]/td[3]')

    layoutOKBtn_loc = ('xpath', '//*[@id="dialog_layouts"]/div[3]/input[2]')  # Layout设置页面OK按钮
    nameCol_loc = ('xpath', '//*[@id="jobsitelist"]/div/table/tr/th[1]/div')  # jobsite列表第一列
    regionCol_loc = ('xpath', '//*[@id="jobsitelist"]/div/table/tr/th[2]/div')  # jobsite列表第二列
    numberCol_loc = ('xpath', '//*[@id="jobsitelist"]/div/table/tr/th[3]/div')  # jobsite列表第三列

    resetLayoutBtn_loc = ('xpath', '//*[@id="contentctrl"]/div[@class="function_title"]/span[@class="sbutton iconresetlayout"]')  # Reset Layout按钮
    resetLayoutOKBtn_loc = ('xpath', yes_btn)  # Reset Layout对话框Yes按钮

    # Configuration相关元素
    configurationBtn_loc = ('xpath', '//*[@id="contentctrl"]/div[@class="function_title"]/span[@class="sbutton iconcog"]')  # Configuration按钮
    configIframe_loc = ('id', 'iframejobsiteacconfig')  # Configuration设置页面
    exitBtn_loc = ('xpath', '//*[@id="content1"]/div[2]/div[2]/span')  # Exit按钮

    assetTable_loc = ('xpath', '//*[@id="selectedmachinelist"]/div/div/div/table')
    addAssetBtn_loc = ('xpath', '//*[@id="div_container"]/div[1]/div[1]/span[2]')  # 添加机器按钮
    # 位置变更
    # 添加机器页面第一个机器
    assetLoc_loc = ('xpath', '//*[@id="dialog_machines"]/div[2]/div[5]/div/div[1]/div/table/tbody/tr[1]/td[1]/%s' % grid_ck)
    addAssetOKBtn_loc = ('xpath', '//*[@id="dialog_machines"]/div[3]/input[2]')  # 添加机器页面OK按钮

    # 添加机器对话框OK按钮
    addAssetDilogOKBtn_loc = ('xpath', ok_btn)

    selectAllAssets_loc = ('xpath', '//*[@id="selectedmachinelist"]/div/table/tr/th[1]/div/span/%s' % grid_ck)  # Assets全选框
    deleteAssetBtn_loc = ('xpath', '//*[@id="div_container"]/div[1]/div[1]/span[3]')  # Assets删除按钮
    deleteAssetYesBtn_loc = ('xpath', yes_btn)  # Assets删除对话框Yes按钮
    deleteAssetDilog_loc = ('xpath', '/html/body/div[4]')
    # deleteAssetDilogOKBtn_loc = ('xpath','/html/body/div[4]/div[3]/[@class="dialog-close"]') # Assets删除对话框OK按钮
    deleteAssetDilogOKBtn_loc = ('xpath', ok_btn)

    assetTypeTable_loc = ('xpath', '//*[@id="selectedassettypelist"]/div/div/div/table')
    addAssetTypeBtn_loc = ('xpath', '//*[@id="div_container"]/div[2]/div[1]/span[2]')  # 添加机器按钮
    assetTypeLoc_loc = ('xpath', '//*[@id="availableassettypelist"]/div/div/div/table/tbody/tr[1]/td[1]')  # 添加机器页面第一个机器
    addAssetTypeOKBtn_loc = ('xpath', '//*[@id="dialog_assettype"]/div[3]/input[2]')  # 添加机器页面OK按钮
    addAssetTypeDilogOKBtn_loc = ('xpath', ok_btn)

    selectAllAssetTypes_loc = ('xpath', '//*[@id="selectedassettypelist"]/div/table/tr/th[1]/div/span/%s' % grid_ck) # AssetTypes全选框
    deleteAssetTypeBtn_loc = ('xpath', '//*[@id="div_container"]/div[2]/div[1]/span[3]')  # AssetTypes删除按钮
    deleteAssetTypeYesBtn_loc = ('xpath', yes_btn)  # AssetTypes删除对话框Yes按钮
    deleteAssetTypeDilogOKBtn_loc = ('xpath', ok_btn)

    # 添加jobsite页面的元素
    jobsiteiframe_loc = ('id', 'iframejobsite')  # Jobsite添加页面
    name_loc = ('id', 'dialog_jobsitename')  # Name
    type_loc = ('id', 'dialog_jobsitetype')  # Type
    region_loc = ('id', 'dialog_region')  # Region
    number_loc = ('id', 'dialog_number')  # Number
    code_loc = ('id', 'dialog_jobsitecode')  # Code
    latitude_loc = ('id', 'dialog_latitude')  # Latitude
    longitude_loc = ('id', 'dialog_longitude')  # Longitude
    radius_loc = ('id', 'dialog_radius')  # Radius:

    saveBtn_loc = ('xpath', '//*[@id="content1"]/div[1]/div[1]/span[1]') # Save按钮
    exitWithoutSavingBtn_loc = ('xpath', '//*[ @ id="content1"]/div[1]/div[1]/span[4]')  # exit without saving按钮
    saveDialog_loc = ('xpath', msg_content)  # save后的对话框
    saveDialogOkBtn_loc = ('xpath', ok_btn)   # 对话框上的OK按钮

    deleteDialogOkBtn_loc = ('xpath', yes_btn)  # 删除对话框上的Yes按钮

    # 列表分派机器
    manangeAsset_btn = ('xpath', '//*[@id="jobsitelist"]/div/div[1]/div/table/tbody/tr[1]/td/a[@title="Manage Assets"]')
    madd_btn = ('xpath', '//*[@id="dialog_managemahchine"]/div[3]/span[@class="sbutton iconadd"]')
    maddfirstAsset_chx = ('xpath', '//*[@id="dialog_machines"]/div[2]/div[4]/div/div[1]/div/table/tbody/tr[1]/td[1]/%s' % grid_ck)
    maOKBtn_loc = ('xpath', '//*[@id="dialog_machines"]/div[@class="dialog-func"]/input[@value="OK"]')
    maCloseBtn_loc = ('xpath', '//*[@id="dialog_managemahchine"]/div[@class="dialog-func"]/input[@value="Close"]')

    def search(self, text):
        self.clear(self.searchInbox_loc)
        sleep(1)
        self.send_keys(self.searchInbox_loc, text)
        sleep(1)
        self.click(self.searchButton_loc)
        sleep(1)

    def inputTo(self, Inboxloc, text):
        self.send_keys(Inboxloc, text)





