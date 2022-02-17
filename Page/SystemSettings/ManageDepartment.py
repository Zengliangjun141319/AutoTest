# coding: utf-8

from Common.operater import Operater

class DepartmentPage(Operater):

    settingsbutton_loc = ('id', "button_menu")
    syssettings_loc = ('xpath', "//*[@id='lisyssetting']/a/span")
    department_loc = ('xpath', "//*[@id='nav_departments']/a/span")

    iframe_loc = ('xpath', "//*[@id='set_right']/iframe")

    addbutton_loc = ('xpath', "//*[@id='recordcontent']/div[2]/span[1]")
    departmentname_loc = ('id', "dialog_name")
    code_loc = ('id', "dialog_code")
    notes_loc = ('id', "dialog_notes")

    okbutton_loc = ('xpath', '//*[@id="dialog_department"]/div[3]/input[2]')
    cancelbutton_loc = ('xpath', '//*[@id="dialog_department"]/div[3]/input[1]')

    addmsg_loc = ('xpath', '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-content"]/div')
    msgokbutton_loc = ('xpath', '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input')

    addchild_loc = ('xpath', '//*[@id="departmentlist"]/div/div/div/table/tr[1]/td/a[@title="Add"]')
    editbutton_loc = ('xpath', '//*[@id="departmentlist"]/div/div/div/table/tr/td/a[@title="Edit"]')
    editokbutton_loc = ('xpath', '//*[@id="dialog_department"]/div[3]/input[2]')

    delbutton_loc = ('xpath', '//*[@id="departmentlist"]/div/div/div/table/tr/td/a[@title="Delete"]')

    delmsgok_loc = ('xpath', '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input[2]')

    firstdepartname_loc = ('xpath', "//*[@id='departmentlist']/div/div/div/table/tr[1]/td[1]/span")