from Common.operater import Operater

class AlertsManagementPage(Operater):
    # 左侧滑块大图标
    assetHealth_loc = ('xpath', '//*[@id="divLeftTitle"]/div[8]/div')

    # Alerts Management菜单元素
    exButton_loc = ('xpath', '//*[@id="nav_arrow"]')  # 左边菜单收折按钮
    alertsManagement_loc = ('link text', 'Alerts Management')  # Alerts Management菜单

    # Alert View列表元素
    iframe_loc = ('xpath', '//*[@id="set_right"]/iframe')  # 主iframe
    alertViewTab_loc = ('id', 'tabAlertView')  # Alert View Tab
    beginDate_loc = ('id', 'txtbegindate')  # Begin Date
    searchBtn_loc = ('xpath', '//*[@id="recordcontent"]/div[3]/input')  # 搜索按钮
    acknowledgeAlertBtn_loc = ('xpath', '//*[@id="div_function"]/span[1]')  # Acknowledge Alert按钮
    acknowledgeAlerComment_loc = ('id', 'dialog_acknowledgmentcomment')  # Acknowledge对话框的Comment
    acknowledgeAlerOKBtn_loc = ('xpath', '//*[@id="dialog_acknowledgingalerts"]/div[@class="dialog-func"]/input[2]')  # Acknowledge对话框的OK按钮

    # Create Work Order相关元素
    createWorkOrderBtn_loc = ('id','btnassignworkorder')  # Create Work Order按钮
    workOrderIframe_loc = ('id', 'iframeworkorder')  # Work Order页面的Iframe
    workOrderDescription_loc = ('id', 'dialog_description')  # Work Order页面的Description
    selectAsset_loc = ('id', 'btnSelectAsset')  # Work Order页面的机器选择按钮
    firstAsset_loc = ('xpath','//*[@id="dialog_machines"]/div[2]/div[4]/div/div[1]/div/table/tbody/tr[1]')  # 第一个机器
    selectAssetOKBtn_loc = ('xpath','//*[@id="dialog_machines"]/div[3]/input[2]')
    saveBtn_loc = ('xpath', '//*[@id="tab_workorder"]/div[1]/span[1]')  # Save按钮
    exitWithoutSavingBtn_loc = ('xpath', '//*[@id="tab_workorder"]/div[1]/span[3]')# exit without saving按钮
    saveDialog_loc = ('xpath', '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-content"]/div')  # save后的对话框
    saveDialogOkBtn_loc = ('xpath', '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input')  # 对话框上的OK按钮

    # Alert View列表元素
    assetViewTab_loc = ('id', 'tabAssetView')  # Asset View Tab页
    expandAll_loc = ('id', 'btnExpandAll')  # Expand All按钮

    # Acknowledged Alerts列表元素
    acknowledgedAlerstab_loc = ('id', 'tabAcknowledgedAlertsView')  # Acknowledged Alers Tab页
    acknowledgedBy_loc = ('xpath', '//*[@id="acknowledgedalertslist"]/div/table/tbody/tr/th[1]/div[1]/span')# Acknowledged By列