from operater import Operater
from Page.comms import *


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
    searchBtn_loc = ('xpath', '//*[@id="recordcontent"]/div[3]/input[@value="Search"]')  # 搜索按钮
    acknowledgeAlertBtn_loc = ('xpath', '//*[@id="div_function"]/span[1]')  # Acknowledge Alert按钮
    acknowledgeAlerComment_loc = ('id', 'dialog_acknowledgmentcomment')  # Acknowledge对话框的Comment
    acknowledgeAlerOKBtn_loc = ('xpath', '//*[@id="dialog_acknowledgingalerts"]/div[@class="dialog-func"]/input[2]')  # Acknowledge对话框的OK按钮

    # Create Work Order相关元素
    createWorkOrderBtn_loc = ('id', 'btnassignworkorder')  # Create Work Order按钮
    workOrderIframe_loc = ('id', 'iframeworkorder')  # Work Order页面的Iframe
    workOrderDescription_loc = ('id', 'dialog_description')  # Work Order页面的Description
    desc_not_empty_ok_loc = ('xpath', ok_btn)
    selectAsset_loc = ('id', 'btnSelectAsset')  # Work Order页面的机器选择按钮
    # 位置变更 //*[@id="dialog_machines"]/div[2]/div[5]/div/div[1]/div/table/tbody/tr[1]/td[1]
    firstAsset_loc = ('xpath', '//*[@id="dialog_machines"]/div[2]/div[5]/div/div[1]/div/table/tbody/tr[1]')  # 第一个机器
    selectAssetOKBtn_loc = ('xpath', '//*[@id="dialog_machines"]/div[3]/input[2]')
    saveBtn_loc = ('xpath', '//*[@id="content1"]/div[1]/span[@class="sbutton iconsave"]')  # Save按钮
    exitWithoutSavingBtn_loc = ('xpath', '//*[@id="content1"]/div[1]/span[@class="sbutton iconexit"]')# exit without saving按钮
    saveDialog_loc = ('xpath', msg_content)  # save后的对话框
    saveDialogOkBtn_loc = ('xpath', ok_btn)  # 对话框上的OK按钮

    # 729版本增加弹出窗口
    saveStatusChange_loc = ('id', 'btn_savestatuschange')
    woid_loc = ('xpath', '//*[@id="alertviewlist"]/div/table/tr/th[@data-key="WorkOrderNumber"]')
    skip_loc = ('xpath', '//*[@id="tbsummary"]/tbody/tr[3]/td[3]')

    # Alert View列表元素
    assetViewTab_loc = ('id', 'tabAssetView')  # Asset View Tab页
    expandAll_loc = ('id', 'btnExpandAll')  # Expand All按钮

    # Acknowledged Alerts列表元素
    acknowledgedAlerstab_loc = ('id', 'tabAcknowledgedAlertsView')  # Acknowledged Alers Tab页
    acknowledgedBy_loc = ('xpath', '//*[@id="acknowledgedalertslist"]/div/table/tr/th[1]/div[1]/span')# Acknowledged By列