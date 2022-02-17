from Common.operater import Operater
from time import sleep

class MapView(Operater):
    # 左侧菜单
    homemenu_loc = ('id', 'button_home')    # Home菜单
    mapmenu_loc = ('xpath', '//*[@id="divLeftTitle"]/div[@title="Map View"]/div/img')  # 地图菜单
    fullmenu_loc = ('id', 'button_sites')  # 全菜单
    sysmenu_loc = ('id', 'button_menu')  # 系统菜单

    # 收折按钮
    ExButton_loc = ('id', 'splitIcon')  # 左侧收折按钮

    # 四组Tab
    tabAssets_loc = ('id', 'tabMachines')  # 机器
    tabJobsite_loc = ('id', 'tabJobSiets')  # Jobsite
    tabAssetGroup_loc = ('id', 'tabAssetGroups')  # 机器组
    tabShape_loc = ('id', 'tabShapes')  # Shape

    # 搜索选项
    selOnroad_loc = ('id', 'selOnroad')    # 下拉选择Onroad
    loadDefault_loc = ('id', 'btnLoadSearchDetault')  # Load Default
    savedSearch_loc = ('id', 'btnSavedSearches')
    saveSeachDefault_loc = ('id', 'btnSaveSearchDetault')
    searchInbox_loc = ('id', 'txtMachineSearchText')  # 搜索框
    searchButton_loc = ('id', 'btnMachineSearch')  # 搜索按钮
    showAll_loc = ('xpath', '//*[@id="machineHeader"]/input[3]')

    chxcloude0_loc = ('id', 'chkExcludeNoLoc')  # 包含0，0
    selAttachment_loc = ('id', 'selAttachment')    # 下拉选择Attachment

    # 机器列表
    firstAssetCheck_loc = ('xpath', '//*[@id="machineList"]/div/div[1]/input')
    firstAssetLink_loc = ('xpath', '//*[@id="machineList"]/div/div[1]/a')
    firstAssetI_loc = ('xpath', '//*[@id="machineList"]/div/div[1]/span[1]')
    # //*[@id="machineList"]/div/div/span[2]
    firstAssetLocationHistory_loc = ('xpath', '//*[@id="machineList"]/div/div[1]/span[2]')
    firstAssetOtherInfo_loc = ('xpath', '//*[@id="machineList"]/div/div[1]/div')
    secAssetCheck_loc = ('xpath', '//*[@id="machineList"]/div/div[2]/input')

    # 机器Location history
    selPeriod_loc = ('id', 'dialog_timeperiod')  # Period选择框
    dateFrom_loc = ('id', 'dateFrom')
    dateTo_loc = ('id', 'dateTo')

    play_loc = ('id', 'btnPlay')
    playend_loc = ('id', 'btnPlayEnd')
    closehistory_loc = ('id', 'btnClearLocationHistory')

    # Trip Report
    TripReport_loc = ('id', 'btnLoadTrip')
    closeTrip_loc = ('id', 'btnClearTrip')
    TripReports_loc = ('xpath', '//*[@id="tbTrips"]/tbody/tr')

    # Jobsite列表
    selectAllCheck_loc = ('id', 'chkSelectAll')
    firstJobsiteEx_loc = ('xpath', '//*[@id="jobsiteList"]/div/div[1]/span[1]')
    firstJobsiteCheck_loc = ('xpath', '//*[@id="jobsiteList"]/div/div[1]/input')
    firstJobsiteRediu_loc = ('xpath', '//*[@id="jobsiteList"]/div/div[1]/span[2]')
    firstJobsiteLink_loc = ('xpath', '//*[@id="jobsiteList"]/div/div[1]/a')  # //*[@id="jobsiteList"]/div/div[1]/a

    # 地图右侧
    mapLayer_loc = ('id', 'selMapAlertLayer')  # Map Alert Layer下拉框

    autoRecenter_loc = ('id', 'autoRecenterDiv')
    showlocation_loc = ('id', 'showDealerLocationsDiv')
    showtraffic_loc = ('id', 'showTrafficDiv')
    showWeather_loc = ('id', 'showWeatherDiv')
    showRoute_loc = ('id', 'showRouteBg')

    # 右侧收折
    EXRightButton_loc = ('id', 'splitIconImgRight')

    # 地图放大、缩小
    mapTobig_loc = ('class name', 'esriSimpleSliderIncrementButton')
    mapTosmall_loc = ('class name', 'esriSimpleSliderDecrementButton')

    # 地图上机器Tooltip
    editAsset_loc = ('class name', 'iconasset')
    closeTooltip_loc = ('class name', 'titleButton close')

    # 地图上Jobsite Tooltip
    editJobsite_loc = ('xpath', '//*[@id="JobsiteDetailCtrl"]/div/div[1]/img')
    jobsiteSendmail_loc = ('xpath', '//*[@id="JobsiteDetailCtrl"]/div/div[1]/span')
    jobsitesendothermail_loc = ('id', 'sendlocation_otheremailaddress')
    jobsitesendothertext_loc = ('id', 'sendlocation_othertextaddress')
    jobsitesendDesc_loc = ('id', 'sendlocation_desc')
    jobsitesendOK_loc = ('xpath', '//*[@id="dialog_sendlocation"]/div[3]/input[2]')
    sendjobsitetxt_loc = ('xpath', '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-content"]/div')
    sendjobsiteOK_loc = ('xpath', '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input')

    # 编辑Jobsite
    jobsiteFrame = ('id', 'iframejobsite')

    jobsiteSave_loc = ('xpath', '//*[@id="content1"]/div[1]/div[1]/span[1]')
    jobsiteManageAsseet_loc = ('class name', 'sbutton iconassets')
    jobsiteExit_loc = ('xpath', '//*[@id="content1"]/div[1]/div[1]/span[4]')

    displayAsset_loc = ('id', 'chk_displayassets')  # 显示机器
    displayother_loc = ('id', 'chk_displayothers')  # 显示Image和Icon

    jobsitename_loc = ('id', 'dialog_jobsitename')  # Jobsite名称
    jobsitecode_loc = ('id', 'dialog_jobsitecode')

    editjobsitetxt_loc = ('xpath', '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-content"]/div')  # /html/body/div[6]/div[2]/div
    editjobsiteOK_loc = ('xpath', '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input')  # /html/body/div[7]/div[3]/input

    # 编辑机器
    AssetFrame = ('id', 'iframemachine')

    AssetSave_loc = ('xpath', '//*[@id="div_content"]/div[2]/span[1]')
    AssetSaveandexit_loc = ('xpath', '//*[@id="div_content"]/div[2]/span[2]')
    AssetExit_loc = ('xpath', '//*[@id="div_content"]/div[2]/span[3]')

    AssetCustomName_loc = ('id', 'dialog_name2')  # Custom Asset Name
    SaveAssetTxt_loc = ('xpath', '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-content"]/div')
    SaveAssetOK_loc = ('xpath', '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input')  # /html/body/div[20]/div[3]/input

    # Details
    AssetDetailFrame = ('id', 'ifassetview')

    # Shapes Tab元素
    importshapefileBtn_loc = ('id', 'btnImportShapeFile')
    searchShapeinbox_loc = ('id', 'txtShapeSearchText')
    searchShapeBtn_loc = ('id', 'btnShapeSearch')
    shapeList_loc = ('id', 'shapeList')

    # shape列表元素
    firstShapeCheck_loc = ('xpath', '//*[@id="shapeList"]/div[1]/input')
    firstShapeName_loc = ('xpath', '//*[@id="shapeList"]/div/a')  # title属性即为名字
    firstShapeDel_loc = ('xpath', '//*[@id="shapeList"]/div/span')

    # Import shape file对话框元素
    importshapefilename_loc = ('id', 'dialog_shapename')
    importshapefilenote_loc = ('id', 'dialog_shapenotes')
    importshapeButton_loc = ('id', 'importshapefile')    # input类型上传文件附件
    importshapefileOK_loc = ('xpath', '//*[@id="dialog_importshapefile"]/div[3]/input[2]')


    # Route Navigation
    routenaviBg_loc = ('id', 'showRouteBg')

    addlocation_loc = ('id', 'routeAddStop')
    startlocation_loc = ('xpath', '//*[@id="routeStops"]/div[1]/input')
    startFir_loc = ('xpath', '//*[@id="routePlaces"]/div/span')
    midlocation_loc = ('xpath', '//*[@id="routeStops"]/div[2]/input')
    midFir_loc = ('xpath', '//*[@id="routePlaces"]/div/span')
    endlocation_loc = ('xpath', '//*[@id="routeStops"]/div[3]/input')
    endFir_loc = ('xpath', '//*[@id="routePlaces"]/div/span')

    getDirection_loc = ('id', 'buttonGetRoute')
    Optimizeroute_loc = ('id', 'buttonOptimizeRoute')

    routefaMail_loc = ('xpath', '//*[@id="routeConfigDiv"]/div[@class="routeConfigTop"]/div/em[@class="fa fa-email"]')

    SROAddress_loc = ('id', 'sendlocation_otheremailaddress')
    SRDescription_loc = ('id', 'sendlocation_desc')

    SROKButton_loc = ('xpath', '//*[@id="dialog_sendlocation"]/div[@class="dialog-func"]/input[2]')

    SRMessage_loc = ('xpath', '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-content"]/div')
    SRMessageOk_loc = ('xpath', '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input')