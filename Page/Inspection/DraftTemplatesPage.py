from Common.operater import Operater
import time

class DraftTemplatesPage(Operater):

    # 左侧滑块大图标
    inspection_loc = ('xpath', '//*[@id="divLeftTitle"]/div[@title="Inspection"]')

    # Asset Scheduling菜单元素
    exButton_loc = ('xpath', '//*[@id="nav_arrow"]')    # 左边菜单收折按钮
    templates_loc = ('link text', 'Draft')    # Templates菜单

    # Templates列表元素
    addBtn_loc = ('xpath', '//*[@id="set_right"]/div/div[1]/div[3]/span[1]')  # 添加按钮
    searchText_loc = ('xpath', '//*[@id="set_right"]/div/div[1]/div[2]/input[1]') # 搜索文本框
    searchBtn_loc = ('xpath', '//*[@id="set_right"]/div/div[1]/div[2]/input[2]') # 搜索按钮

    # Summary部分的元素
    templateName_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div/table/tbody/tr[1]/td[2]/input')
    locationEnabled_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div/table/tbody/tr[2]/td[2]/input[1]')
    signatureRequired_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div/table/tbody/tr[2]/td[2]/input[2]')
    forWorkOrder_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div/table/tbody/tr[2]/td[2]/input[3]')

    # 125版本新增Layout下拉框
    layoutinput_loc = ('xpath', '//*[@id="select-layout"]')
    locked_loc = ('xpath','//*[@id="right_popup"]/div/div[2]/div/table/tbody/tr[7]/td[2]/input')
    notes = ('id','dialog_notes')

    # page的元素
    addPage_loc = ('xpath','//*[@id="right_popup"]/div/div[4]/ul/li[1]')
    pageName_loc = ('xpath','//*[@id="right_popup"]/div/div[4]/div/div/div[1]/table/tbody/tr[1]/td[2]/input')
    pageText_loc = ('xpath','//*[@id="right_popup"]/div/div[4]/div/div/div[1]/table/tbody/tr[2]/td[2]/input')

    # section的元素
    addSection_loc = ('xpath','//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[1]/div/span[1]')
    sectionName_loc = ('xpath','//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div/div[3]/input')
    sectionText_loc = ('xpath','//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div/div[4]/input')
    addQuestion_loc = ('xpath','//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div[1]/div/div[5]/em[1]')

    # 第1个问题的元素
    qustion1Name_loc = ('xpath','//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div[2]/div[1]/div[3]/input')
    qustion1Text_loc = ('xpath','//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div[2]/div[1]/div[4]/input')
    qustion1Type_loc = ('xpath', '//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div[2]/div[1]/div[5]/table/tbody/tr/td[1]/select')

    # 第2个问题的元素
    qustion2Name_loc = ('xpath', '//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div[3]/div[1]/div[3]/input')
    qustion2Text_loc = ('xpath', '//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div[3]/div[1]/div[4]/input')
    qustion2Type_loc = ('xpath','//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div[3]/div[1]/div[5]/table/tbody/tr/td[1]/select')

    # 第3个问题的元素
    qustion3Name_loc = ('xpath', '//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div[4]/div[1]/div[3]/input')
    qustion3Text_loc = ('xpath', '//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div[4]/div[1]/div[4]/input')
    qustion3Type_loc = ('xpath','//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div[4]/div[1]/div[5]/table/tbody/tr/td[1]/select')

    # 第4个问题的元素
    qustion4Name_loc = ('xpath', '//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div[5]/div[1]/div[3]/input')
    qustion4Text_loc = ('xpath', '//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div[5]/div[1]/div[4]/input')
    qustion4Type_loc = ('xpath','//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div[5]/div[1]/div[5]/table/tbody/tr/td[1]/select')

    # 第5个问题的元素
    qustion5Name_loc = ('xpath', '//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div[6]/div[1]/div[3]/input')
    qustion5Text_loc = ('xpath', '//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div[6]/div[1]/div[4]/input')
    qustion5Type_loc = ('xpath','//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div[6]/div[1]/div[5]/table/tbody/tr/td[1]/select')

    saveBtn_loc = ('xpath', '//*[@id="right_popup"]/div/div[1]/div/span[1]')   # save
    saveAndExitBtn_loc = ('xpath', '//*[@id="right_popup"]/div/div[1]/div/span[2]')  # save and Exit
    exitWithoutSavingBtn_loc = ('xpath', '//*[@id="right_popup"]/div/div[1]/div/span[4]')  # exit without saving

    saveMessage_loc = ('xpath', '/html/body/div[24]/div[2]/div') # 保存提示对话框
    okBtn_loc = ('xpath', '/html/body/div[24]/div[3]/input')  # 提示对话框上的‘OK’按钮

    # 编辑Template相关元素
    editBtn_loc = ('xpath','//*[@id="set_right"]/div/div[3]/div[1]/div[5]/em[1]') # 编辑按钮

    # 复制Template相关元素
    copyBtn_loc = ('xpath','//*[@id="set_right"]/div/div[3]/div[@class="question-holder"]/div[@class="question-cell template-func"]/em[4]') # 复制按钮
    copyTemplateName_loc = ('xpath','/html/body/div[@class="dialog"]/div[@class="dialog-content"]/table/tbody/tr/td[2]/input') # 复制对话框中的template name文本框
    copyOKBtn_loc = ('xpath', '/html/body/div[@class="dialog"][@init="1"]/div[3]/input[2]') # 复制对话框中的OK按钮

    # 删除Template相关元素
    deleteBtn_loc = ('xpath','//*[@id="set_right"]/div/div[3]/div[@class="question-holder"]/div[@class="question-cell template-func"]/em[@title="Delete Template"]') # 删除按钮
    deleteOKBtn_loc = ('xpath','/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input[2]') # 删除对话框OK按钮

    # 发布Template相关元素
    publishBtn_loc = ('xpath','//*[@id="set_right"]/div/div[3]/div[1]/div[5]/em[2]')
    publsihOKBtn_loc= ('xpath','/html/body/div[@class="dialog popupmsg"]/div[3]/input[2]')

    # published
    publish_menu_loc = ('xpath', '//*[@id="set_left"]/ul/li[@title="Published"]')

    def search(self, text):
        self.clear(self.searchText_loc)
        self.send_keys(self.searchText_loc, text)
        time.sleep(1)
        self.click(self.searchBtn_loc)
        time.sleep(2)

    def inputTo(self, Inboxloc, text):
        self.send_keys(Inboxloc, text)





