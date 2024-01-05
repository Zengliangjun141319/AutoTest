from operater import Operater
from Page.comms import *


class GlobalSectionPage(Operater):
    # admin页面元素
    searchinput_loc = ('id', "searchinputtxt")
    searchbutton_loc = ('xpath', "//*[@id='recordcontent']/div[2]/input[3]")

    customerlink_loc = ('xpath', '//*[@id="modules"]/div[1]/div/div')
    customeropen_loc = ('xpath', '//*[@id="customerlist"]/div/div/div/table/tbody/tr[2]/td[5]/a')

    # Contractor页面
    fullmenu_loc = ('id', "button_sites")
    teamintel_loc = ('xpath', '//*[@id="sites_panel"]/div[1]/div[2]/ul/li[13]/a/span')
    globalsection_loc = ('xpath', '//*[@id="set_left"]/ul/li[@title="Global Sections"]')

    addbutton_loc = ('xpath', '//*[@id="set_right"]/div/div[1]/div[2]/span[1]')

    nameinput_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div/table/tr[1]/td[2]/input')
    displayinput_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div/table/tr[2]/td[2]/input')
    notesinput_loc = ('id', "dialog_notes")

    savebutton_loc = ('xpath', '//*[@id="right_popup"]/div/div[1]/div/span[1]')
    saveexit_loc = ('xpath', '//*[@id="right_popup"]/div/div[1]/div/span[2]')
    withoutsave_loc = ('xpath', '//*[@id="right_popup"]/div/div[1]/div/span[3]')
    # /html/body/div[20]/div[2]/div
    savemsg_loc = ('xpath', msg_content)
    saveok_loc = ('xpath', ok_btn)