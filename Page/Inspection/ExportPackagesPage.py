from operater import Operater
from Page.comms import *


class ExportPackagesPage(Operater):

    # foresight用户打开contractor站点
    customers_loc = ('xpath', '//*[@id="modules"]/div[1]')  # Customers大图标
    searchinput_loc = ('id', 'searchinputtxt')  # Customers列表搜索框
    searchBtn_loc = ('xpath', '//*[@id="recordcontent"]/div[2]/input[3]')  # Customers列表搜索按钮
    openBtn_loc = ('xpath', '//*[@id="customerlist"]/div/div/div/table/tbody/tr[2]/td[5]/a')  # 打开Customer按钮

    # 左侧滑块大图标
    inspection_loc = ('xpath', '//*[@id="divLeftTitle"]/div[@title="Inspection"]/div')

    # Export Packages菜单元素
    exButton_loc = ('xpath', '//*[@id="nav_arrow"]')    # 左边菜单收折按钮
    exportPackages_loc = ('link text', 'Export Packages')    # Export Packages菜单

    # Export Packages列表元素
    createBtn_loc = ('xpath', '//*[@id="set_right"]/div/div[1]/div[@class="function_title"]/span[@class="sbutton iconadd"]')  # Create按钮

    # 创建包页面的元素
    name_loc = ('xpath', '//*[@id="right_popup"]/div/table/tr[1]/td[2]/input')  # Name
    password_loc = ('xpath', '//*[@id="right_popup"]/div/table/tr[2]/td[2]/input')  # Password
    confirmPassword_loc = ('xpath', '//*[@id="right_popup"]/div/table/tr[3]/td[2]/input')  # Confirm Password
    notes_loc = ('xpath', '//*[@id="right_popup"]/div/table/tr[4]/td[2]/textarea')  # Notes

    # Templates标签页的元素
    templatesTab_loc = ('xpath', '//*[@id="right_popup"]/div/ul/li[1]/span')  # Templates Tab页
    # //*[@id="right_popup"]/div/div[2]/div/div[1]/div/table/tbody/tr[1]/td[1]/label/layer
    tempplateCheckbox1_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div/div/div/table/tbody/tr[1]/td[1]/%s' % grid_ck)  # Templates列表的第一条记录
    tempplateCheckbox2_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div/div/div/table/tbody/tr[2]/td[1]/%s' % grid_ck)  # Templates列表的第二条记录

    # Global Sections标签页的元素
    globalSectionsTab_loc = ('xpath', '//*[@id="right_popup"]/div/ul/li[2]/span') # Global Sections Tab页
    globalSectionsCheckbox1_loc = ('xpath', '//*[@id="right_popup"]/div/div[3]/div/div/div/table/tbody/tr[1]/td[1]/%s' % grid_ck)  # Global Sections列表的第一条记录
    globalSectionsCheckbox2_loc = ('xpath', '//*[@id="right_popup"]/div/div[3]/div/div/div/table/tbody/tr[2]/td[1]/%s' % grid_ck)  # Global Sections列表的第二条记录

    saveBtn_loc = ('xpath', '//*[@id="right_popup"]/div/div[@class="function_title"]/span[@class="sbutton iconadd"]')  # 创建页面的Create按钮
    exitBtn_loc = ('xpath', '//*[@id="right_popup"]/div/div[@class="function_title"]/span[@class="sbutton iconexit"]')  # 创建页面的Exit按钮

    # /html/body/div[18]/div[2]/div
    saveMessage_loc = ('xpath', msg_content)
    okBtn_loc = ('xpath', ok_btn)  # 提示对话框上的‘OK’按钮

    def inputTo(self, Inboxloc, text):
        self.send_keys(Inboxloc, text)





