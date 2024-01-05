from operater import Operater
import time
from Page.comms import *


class DraftPage(Operater):
    # admin页面元素
    customerlink_loc = ('xpath', '//*[@id="modules"]/div[1]/div/div')  # Home页的Customer大图标

    searchinput_loc = ('id', "searchinputtxt")  # Customer页搜索框
    searchbutton_loc = ('xpath', '//div[@class="search_bar"]/input[@class="search"]')  # 搜索按钮
    customeropen_loc = ('xpath', '//table[@class="data-grid-body-content"]/tbody/tr[2]/td/a[@title="Open"]')  # Customer页面 Open 链接

    # Contractor页面
    fullmenu_loc = ('id', "button_menu")
    teamintel_loc = ('xpath', '//*[@id="menu_panel"]/ul/li/a/span[text()="Team Intelligence"]')
    exButton_loc = ('id', 'nav_arrow')
    draftmenu_loc = ('xpath', '//*[@id="set_left"]/ul/li[@title="Draft"]')

    # template页面元素
    temsearchinput_loc = ('xpath', '//div[@class="search_bar"]/input[@type="text"]')
    temsearchbutton_loc = ('xpath', '//input[@value="Search"]')

    # 查询结果第一个Template的Name
    tempname1_loc = ('xpath', '//div[@class="question-cell template-name"]/span')
    addbutton_loc = ('xpath', '//span[@class="sbutton iconadd"]')

    # 新增窗口元素
    summs = '//*[@id="right_popup"]/div/div[2]/div[1]/div/table/'
    nameinput_loc = ('xpath', summs + 'tr[1]/td[2]/input')
    location_loc = ('xpath', summs + 'tr[2]/td[2]/input[1]')
    signature_loc = ('xpath', summs + 'tr[2]/td[2]/input[2]')

    # 125版本新增Layout下拉框
    layoutinput_loc = ('xpath', '//*[@id="select-layout"]')
    # //*[@id="right_popup"]/div/div[2]/div/table/tbody/tr[6]/td[2]/input
    locked_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div/table/tr[6]/td[2]/input')
    notes_loc = ('id', 'dialog_notes')

    pageadd_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div[3]/ul/li[1]')
    pagename_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div[3]/div/div/div[1]/table/tr[1]/td[2]/input')
    pagetext_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div[3]/div/div/div[1]/table/tr[2]/td[2]/input')

    sections = '//*[@id="right_popup"]/div/div[2]/div[3]/div/div/div[2]/div[3]/div/'

    sectionadd_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span[1]')
    sectionname_loc = ('xpath', sections + 'div/div/div[3]/input')
    sectiontext_loc = ('xpath', sections + 'div/div/div[4]/input')
    sectioncopy_loc = ('xpath', sections + 'div/div/div/em[@title="Copy Section"]')
    sectiondel_loc = ('xpath', sections + 'div/div/div/em[@title="Delete Section"]')

    questionadd_loc = ('xpath', sections + 'div/div/div/em[@title="Add Question"]')

    question1name_loc = ('xpath', sections + 'div[2]/div[1]/div[@class="question-cell question-name"]/input')
    question1text_loc = ('xpath', sections + 'div[2]/div[1]/div[@class="question-cell question-display"]/input')
    question1type_loc = ('xpath', sections + 'div[2]/div[1]/div[@class="question-cell question-type"]/table/tr/td[1]/select')

    question2name_loc = ('xpath', sections + 'div[3]/div[1]/div[@class="question-cell question-name"]/input')
    question2text_loc = ('xpath', sections + 'div[3]/div[1]/div[@class="question-cell question-display"]/input')
    question2type_loc = ('xpath', sections + 'div[3]/div[1]/div[@class="question-cell question-type"]/table/tr/td[1]/select')

    question3name_loc = ('xpath', sections + 'div[4]/div[1]/div[@class="question-cell question-name"]/input')
    question3text_loc = ('xpath', sections + 'div[4]/div[1]/div[@class="question-cell question-display"]/input')
    question3type_loc = ('xpath', sections + 'div[4]/div[1]/div[@class="question-cell question-type"]/table/tr/td[1]/select')

    savebutton_loc = ('xpath', '//*[@id="right_popup"]/div/div[1]/div/span[1]')
    saveexit_loc = ('xpath', '//*[@id="right_popup"]/div/div[1]/div/span[2]')
    withoutexit_loc = ('xpath', '//*[@id="right_popup"]/div/div[1]/div/span[3]')
    savemsg_loc = ('xpath', msg_content)
    savemsgok_loc = ('xpath', ok_btn)

    editbutton_loc = ('xpath', '//em[@class="spanbtn iconedit"]')  # 列表上编辑按钮

    publishbutton_loc = ('xpath', '//em[@class="spanbtn iconshare"]')  # 发布
    publishyes_loc = ('xpath', yes_btn)

    delbutton_loc = ('xpath', '//em[@class="spanbtn icondelete"]')  # 删除按钮
    delyes_loc = ('xpath', yes_btn)

    copybutton_loc = ('xpath', '//em[@class="spanbtn iconcopy"]')  # 复制按钮
    copytemname_loc = ('xpath', '//div[@class="dialog"][@init="1"]/div[2]/table/tr/td[2]/input')
    copytemok_loc = ('xpath', '//div[@class="dialog"][@init="1"]/div[3]/input[2]')

    def search(self, text):
        self.clear(self.temsearchinput_loc)
        self.send_keys(self.temsearchinput_loc, text)
        time.sleep(1)
        self.click(self.temsearchbutton_loc)
        time.sleep(2)

