from Common.operater import Operater
import time


class DraftPage(Operater):

    # admin页面元素
    searchinput_loc = ('id', "searchinputtxt")
    searchbutton_loc = ('xpath', "//*[@id='recordcontent']/div[2]/input[3]")

    customerlink_loc = ('xpath', '//*[@id="modules"]/div[1]/div/div')
    customeropen_loc = ('xpath', '//*[@id="customerlist"]/div/div/div/table/tbody/tr[2]/td[5]/a')

    # Contractor页面
    fullmenu_loc = ('id', "button_sites")
    teamintel_loc = ('xpath', '//*[@id="sites_panel"]/div[1]/div[2]/ul/li[13]/a/span')
    draftmenu_loc = ('xpath', '//*[@id="set_left"]/ul/li[4]/a/span')

    # template页面元素
    temsearchinput_loc = ('xpath', '//*[@id="set_right"]/div/div[1]/div[2]/input[1]')
    temsearchbutton_loc = ('xpath', '//*[@id="set_right"]/div/div[1]/div[2]/input[2]')

    # 查询结果第一个Template的Name
    tempname1_loc = ('xpath', ".//*[@id='set_right']/div/div[3]/div[1]/div[2]/span")

    addbutton_loc = ('xpath', '//*[@id="set_right"]/div/div[1]/div[3]/span[1]')

    # 新增窗口元素
    nameinput_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div/table/tbody/tr[1]/td[2]/input')
    location_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div/table/tbody/tr[2]/td[2]/input[1]')
    signature_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div/table/tbody/tr[2]/td[2]/input[2]')
    forWorkOrder_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div/table/tbody/tr[2]/td[2]/input[3]')

    # 125版本新增Layout下拉框
    layoutinput_loc = ('xpath', '//*[@id="select-layout"]')
    # //*[@id="right_popup"]/div/div[2]/div/table/tbody/tr[6]/td[2]/input
    locked_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div/table/tbody/tr[6]/td[2]/input')
    notes_loc = ('id', 'dialog_notes')

    pageadd_loc = ('xpath', '//*[@id="right_popup"]/div/div[4]/ul/li[1]')
    pagename_loc = ('xpath', '//*[@id="right_popup"]/div/div[4]/div/div/div[1]/table/tbody/tr[1]/td[2]/input')
    pagetext_loc = ('xpath', '//*[@id="right_popup"]/div/div[4]/div/div/div[1]/table/tbody/tr[2]/td[2]/input')

    sectionadd_loc = ('xpath', '//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[1]/div/span[1]')
    sectionname_loc = ('xpath', '//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div/div[3]/input')
    sectiontext_loc = ('xpath', '//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div/div[4]/input')
    sectioncopy_loc = ('xpath', '//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div/div[5]/em[2]')
    sectiondel_loc = ('xpath', '//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div[1]/div[5]/em[3]')

    questionadd_loc = ('xpath', '//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div/div[5]/em[1]')

    question1name_loc = ('xpath', '//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div[2]/div[1]/div[3]/input')
    question1text_loc = ('xpath', '//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div[2]/div[1]/div[4]/input')
    question1type_loc = ('xpath', '//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div[2]/div[1]/div[5]/table/tbody/tr/td[1]/select')

    question2name_loc = ('xpath', '//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div[3]/div[1]/div[3]/input')
    question2text_loc = ('xpath', '//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div[3]/div[1]/div[4]/input')
    question2type_loc = ('xpath', '//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div[3]/div[1]/div[5]/table/tbody/tr/td[1]/select')

    question3name_loc = ('xpath', '//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div[4]/div[1]/div[3]/input')
    question3text_loc = ('xpath', '//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div[4]/div[1]/div[4]/input')
    question3type_loc = ('xpath', '//*[@id="right_popup"]/div/div[4]/div/div/div[2]/div[3]/div/div[4]/div[1]/div[5]/table/tbody/tr/td[1]/select')

    savebutton_loc = ('xpath', '//*[@id="right_popup"]/div/div[1]/div/span[1]')
    saveexit_loc = ('xpath', '//*[@id="right_popup"]/div/div[1]/div/span[2]')
    withoutexit_loc = ('xpath', '//*[@id="right_popup"]/div/div[1]/div/span[3]')
    savemsg_loc = ('xpath', '/html/body/div[24]/div[2]/div')
    savemsgok_loc = ('xpath', '/html/body/div[24]/div[3]/input')

    editbutton_loc = ('xpath', '//*[@id="set_right"]/div/div[3]/div/div[5]/em[1]')

    publishbutton_loc = ('xpath', '//*[@id="set_right"]/div/div[3]/div/div[5]/em[2]')
    publishyes_loc = ('xpath', '/html/body/div[26]/div[3]/input[2]')

    delbutton_loc = ('xpath', '//*[@id="set_right"]/div/div[3]/div/div[5]/em[3]')
    delyes_loc = ('xpath', '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input[2]')


    copybutton_loc = ('xpath', '//*[@id="set_right"]/div/div[3]/div/div[5]/em[4]')
    copytemname_loc = ('xpath', '/html/body/div[@class="dialog"]/div[@class="dialog-content"]/table/tbody/tr/td[2]/input')
    copytemok_loc = ('xpath', '/html/body/div[@class="dialog"][@init="1"]/div[3]/input[2]')


    def search(self, text):
        self.clear(self.temsearchinput_loc)
        self.send_keys(self.temsearchinput_loc, text)
        time.sleep(1)
        self.click(self.temsearchbutton_loc)
        time.sleep(2)

