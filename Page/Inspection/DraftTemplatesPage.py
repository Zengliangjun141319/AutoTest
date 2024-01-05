from operater import Operater
import time
from Page.comms import *


class DraftTemplatesPage(Operater):

    # 左侧滑块大图标
    inspection_loc = ('xpath', '//*[@id="divLeftTitle"]/div[@title="Inspection"]')

    # Asset Scheduling菜单元素
    exButton_loc = ('xpath', '//*[@id="nav_arrow"]')    # 左边菜单收折按钮
    templates_loc = ('link text', 'Draft')    # Templates菜单

    # Templates列表元素
    addBtn_loc = ('xpath', '//*[@id="set_right"]/div/div[1]/div[3]/span[1]')  # 添加按钮
    # //*[@id="set_right"]/div/div[1]/div[2]/input[2]
    searchText_loc = ('xpath', '//*[@id="set_right"]/div/div[1]/div[2]/input[@type="text"]')  # 搜索文本框
    searchBtn_loc = ('xpath', '//*[@id="set_right"]/div/div[1]/div[2]/input[@value="Search"]')  # 搜索按钮

    # Summary部分的元素
    templateName_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div[1]/div/table/tr[1]/td[2]/input')
    locationEnabled_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div[1]/div/table/tr[2]/td[2]/input[1]')
    signatureRequired_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div[1]/div/table/tr[2]/td[2]/input[2]')
    forWorkOrder_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div[1]/div/table/tr[2]/td[2]/input[3]')

    # 125版本新增Layout下拉框
    layoutinput_loc = ('xpath', '//*[@id="select-layout"]')
    locked_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div/table/tr[7]/td[2]/input')
    notes = ('id', 'dialog_notes')

    # page的元素
    addPage_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div[3]/ul/li[1]')
    pageName_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div[3]/div/div/div[1]/table/tr[1]/td[2]/input')
    pageText_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div[3]/div/div/div[1]/table/tr[2]/td[2]/input')
    pagedisplay_loc = ('id', 'tempchk1')

    first_sec = '//*[@id="right_popup"]/div/div[2]/div[3]/div/div/div[2]/div[3]/div/'
    # section的元素
    addSection_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span[1]')
    sectionName_loc = ('xpath', first_sec + 'div/div/div[3]/input')
    sectionText_loc = ('xpath', first_sec + 'div/div/div[4]/input')
    addQuestion_loc = ('xpath', first_sec + 'div/div/div/em[@title="Add Question"]')

    # 第1个问题的元素
    qustion1Name_loc = ('xpath', first_sec + 'div[2]/div[1]/div[@class="question-cell question-name"]/input')
    qustion1Text_loc = ('xpath', first_sec + 'div[2]/div[1]/div[@class="question-cell question-display"]/input')
    qustion1Type_loc = ('xpath', first_sec + 'div[2]/div[1]/div[@class="question-cell question-type"]/table/tr/td[1]/select')

    # 第2个问题的元素
    qustion2Name_loc = ('xpath', first_sec + 'div[3]/div[1]/div[@class="question-cell question-name"]/input')
    qustion2Text_loc = ('xpath', first_sec + 'div[3]/div[1]/div[@class="question-cell question-display"]/input')
    qustion2Type_loc = ('xpath', first_sec + 'div[3]/div[1]/div[@class="question-cell question-type"]/table/tr/td[1]/select')

    # 第3个问题的元素
    qustion3Name_loc = ('xpath', first_sec + 'div[4]/div[1]/div[@class="question-cell question-name"]/input')
    qustion3Text_loc = ('xpath', first_sec + 'div[4]/div[1]/div[@class="question-cell question-display"]/input')
    qustion3Type_loc = ('xpath', first_sec + 'div[4]/div[1]/div[@class="question-cell question-type"]/table/tr/td[1]/select')

    # 第4个问题的元素
    qustion4Name_loc = ('xpath', first_sec + 'div[5]/div[1]/div[@class="question-cell question-name"]/input')
    qustion4Text_loc = ('xpath', first_sec + 'div[5]/div[1]/div[@class="question-cell question-display"]/input')
    qustion4Type_loc = ('xpath', first_sec + 'div[5]/div[1]/div[@class="question-cell question-type"]/table/tr/td[1]/select')

    # 第5个问题的元素
    qustion5Name_loc = ('xpath', first_sec + 'div[6]/div[1]/div[@class="question-cell question-name"]/input')
    qustion5Text_loc = ('xpath', first_sec + 'div[6]/div[1]/div[@class="question-cell question-display"]/input')
    qustion5Type_loc = ('xpath', first_sec + 'div[6]/div[1]/div[@class="question-cell question-type"]/table/tr/td[1]/select')

    saveBtn_loc = ('xpath', '//*[@id="right_popup"]/div/div[1]/div/span[1]')   # save
    saveAndExitBtn_loc = ('xpath', '//*[@id="right_popup"]/div/div[1]/div/span[2]')  # save and Exit
    exitWithoutSavingBtn_loc = ('xpath', '//*[@id="right_popup"]/div/div[1]/div/span[4]')  # exit without saving

    saveMessage_loc = ('xpath', msg_content)  # 保存提示对话框
    okBtn_loc = ('xpath', ok_btn)  # 提示对话框上的‘OK’按钮

    # 编辑Template相关元素
    editBtn_loc = ('xpath', '//em[@class="spanbtn iconedit"]')  # 编辑按钮

    # 复制Template相关元素
    copyBtn_loc = ('xpath', '//em[@class="spanbtn iconcopy"]')  # 复制按钮
    copyTemplateName_loc = ('xpath', '//div[@class="dialog"][@init="1"]/div[@class="dialog-content"]/table/tr/td[2]/input')  # 复制对话框中的template name文本框
    copyOKBtn_loc = ('xpath', '//div[@class="dialog"][@init="1"]/div[@class="dialog-func"]/input[@value="OK"]')

    # 删除Template相关元素
    deleteBtn_loc = ('xpath', '//em[@class="spanbtn icondelete"]')  # 删除按钮
    deleteOKBtn_loc = ('xpath', yes_btn)  # 删除对话框OK按钮

    # 发布Template相关元素
    publishBtn_loc = ('xpath', '//em[@class="spanbtn iconshare"]')  # 发布按钮
    publsihOKBtn_loc = ('xpath', yes_btn)

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
