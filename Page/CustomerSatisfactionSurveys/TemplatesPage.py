from operater import Operater
import time
from Page.comms import *


class TemplatesPage(Operater):
    # 左侧滑块大图标
    assetHealth_loc = ('xpath', '//*[@id="divLeftTitle"]/div[@title="Asset Health"]/div')

    # Survey templates菜单元素
    exButton_loc = ('xpath', '//*[@id="nav_arrow"]')  # 左边菜单收折按钮
    surveyTemplates_loc = ('xpath', '//*[@id="nav_wosurveytemplate"]/a/span')  # Survey Templates_菜单

    # Work Order Survey Templates列表元素
    iframe_loc = ('xpath', '//*[@id="set_right"]/iframe')
    addBtn_loc = ('xpath', '//*[@id="content1"]/div/div[3]/span[1]')  # Add按钮
    editBtn_loc = ('xpath', '//*[@id="surveylist"]/div/div[1]/div/table/tbody/tr[1]/td/a[@title="Edit"]')
    deleteBtn_loc = ('xpath', '//*[@id="surveylist"]/div/div[1]/div/table/tbody/tr[1]/td/a[@title="Delete"]')
    deleteOKBtn_loc = ('xpath', yes_btn)
    searchText_loc = ('id', 'searchinputtxt')  # 搜索文本框
    searchBtn_loc = ('xpath', '//*[@id="content1"]/div/div[2]/input[@value="Search"]')  # search按钮
    searchTemplate_loc = ('xpath', '//*[@id="surveylist"]/div/div[1]/div/table/tbody/tr/td[1]')  # 搜索出的Template名称

    # 添加Template页面元素
    addIframe_loc = ('id', 'iframesurveytemplate')
    saveAndExitBtn_loc = ('xpath', '//*[@id="content1"]/div[1]/div[@class="function_title"]/span[2]')
    templateName_loc = ('id', 'dialog_name')
    addQuestion_loc = ('xpath', '//*[@id="divcontent"]/div/div[1]/span[2]')
    types_loc = ('xpath', '//*[@id="questionlist"]/div[1]/div[1]/div[5]/table/tbody/tr/td[1]/select')

    qustion1Name_loc = ('xpath', '//*[@id="questionlist"]/div[1]/div[1]/div[2]/input')
    qustion1Text_loc = ('xpath', '//*[@id="questionlist"]/div[1]/div[1]/div[3]/input')
    qustion1Type_loc = ('xpath', '//*[@id="questionlist"]/div[1]/div[1]/div[5]/table/tr/td[1]/select')

    qustion2Name_loc = ('xpath', '//*[@id="questionlist"]/div[2]/div[1]/div[2]/input')
    qustion2Text_loc = ('xpath', '//*[@id="questionlist"]/div[2]/div[1]/div[3]/input')
    qustion2Type_loc = ('xpath', '//*[@id="questionlist"]/div[2]/div[1]/div[5]/table/tr/td[1]/select')

    qustion3Name_loc = ('xpath', '//*[@id="questionlist"]/div[3]/div[1]/div[2]/input')
    qustion3Text_loc = ('xpath', '//*[@id="questionlist"]/div[3]/div[1]/div[3]/input')
    qustion3Type_loc = ('xpath', '//*[@id="questionlist"]/div[3]/div[1]/div[5]/table/tr/td[1]/select')

    qustion4Name_loc = ('xpath', '//*[@id="questionlist"]/div[4]/div[1]/div[2]/input')
    qustion4Text_loc = ('xpath', '//*[@id="questionlist"]/div[4]/div[1]/div[3]/input')
    qustion4Type_loc = ('xpath', '//*[@id="questionlist"]/div[4]/div[1]/div[5]/table/tr/td[1]/select')

    qustion5Name_loc = ('xpath', '//*[@id="questionlist"]/div[5]/div[1]/div[2]/input')
    qustion5Text_loc = ('xpath', '//*[@id="questionlist"]/div[5]/div[1]/div[3]/input')
    qustion5Type_loc = ('xpath', '//*[@id="questionlist"]/div[5]/div[1]/div[5]/table/tr/td[1]/select')

    # 复制Template
    copytemplateBtn_loc = ('xpath', '//*[@id="surveylist"]/div/div[1]/div/table/tbody/tr[1]/td/a[@title="Copy"]')
    # 预览
    previewtemplate_loc = ('xpath', '//*[@id="surveylist"]/div/div[1]/div/table/tbody/tr[1]/td/a[@title="Preview"]')
    previewAdv_loc = ('id', 'details-button')
    previewLink_loc = ('id', 'proceed-link')
    previewTitle_loc = ('xpath', '//*[@id="main-page-container"]/div/div')

    def search(self, text):
        self.clear(self.searchText_loc)
        self.send_keys(self.searchText_loc, text)
        time.sleep(1)
        self.click(self.searchBtn_loc)
        time.sleep(2)

    def inputTo(self, Inboxloc, text):
        self.send_keys(Inboxloc, text)