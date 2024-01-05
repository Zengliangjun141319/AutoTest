from operater import Operater
from Page.comms import *


class ReportPage(Operater):
    # 左侧滑块大图标
    assetHealth_loc = ('xpath', '//*[@id="divLeftTitle"]/div[@title="Asset Health"]/div')

    # Survey templates菜单元素
    exButton_loc = ('xpath', '//*[@id="nav_arrow"]')  # 左边菜单收折按钮
    report_loc = ('xpath', '//*[@id="nav_wosurveytemplatereport"]/a/span')  # Report菜单

    # Report页面元素
    iframe_loc = ('xpath', '//*[@id="set_right"]/iframe')
    templatesList_loc = ('id', 'templateselectinput')  # templates下拉列表

    # 发送邮件
    sendemailBtn_loc = ('xpath', '//*[@id="content1"]/div[1]/div[@class="search_bar"]/input[@value="Send Email"]')
    otheraddress_loc = ('id', 'email_otheremailaddress')
    sendSurveyRepOK_loc = ('xpath', '//*[@id="sendemailpopupdialog"]/div[@class="dialog-func"]/input[@value="OK"]')

    # Message sent.
    sendresult_loc = ('xpath', msg_content)
    sendresultOK_loc = ('xpath', ok_btn)