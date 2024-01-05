# coding: utf-8

from operater import Operater
from Page.comms import *


class DepartmentPage(Operater):
    # Department
    settingsbutton_loc = ('id', "button_menu")
    syssettings_loc = ('xpath', "//*[@id='lisyssetting']/a/span")
    department_loc = ('xpath', "//*[@id='nav_departments']/a/span")
    exButton_loc = ('id', 'nav_arrow')

    iframe_loc = ('xpath', "//*[@id='set_right']/iframe")

    addbutton_loc = ('xpath', "//*[@id='recordcontent']/div[2]/span[1]")
    departmentname_loc = ('id', "dialog_name")
    code_loc = ('id', "dialog_code")
    notes_loc = ('id', "dialog_notes")

    okbutton_loc = ('xpath', '//*[@id="dialog_department"]/div[3]/input[2]')
    cancelbutton_loc = ('xpath', '//*[@id="dialog_department"]/div[3]/input[1]')

    addmsg_loc = ('xpath', msg_content)
    msgokbutton_loc = ('xpath', ok_btn)

    addchild_loc = ('xpath', '//*[@id="departmentlist"]/div/div/div/table/tr[1]/td/a[@title="Add"]')
    editbutton_loc = ('xpath', '//*[@id="departmentlist"]/div/div/div/table/tr/td/a[@title="Edit"]')
    editokbutton_loc = ('xpath', '//*[@id="dialog_department"]/div[3]/input[2]')

    delbutton_loc = ('xpath', '//*[@id="departmentlist"]/div/div/div/table/tr/td/a[@title="Delete"]')

    delmsgok_loc = ('xpath', yes_btn)

    firstdepartname_loc = ('xpath', "//*[@id='departmentlist']/div/div/div/table/tr[1]/td[1]/span")