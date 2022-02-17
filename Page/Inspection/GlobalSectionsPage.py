from Common.operater import Operater

class GlobalSectionsPage(Operater):

    # 左侧滑块大图标
    inspection_loc = ('xpath', '//*[@id="divLeftTitle"]/div[@title="Inspection"]')

    # Asset Scheduling菜单元素
    exButton_loc = ('xpath', '//*[@id="nav_arrow"]')    # 左边菜单收折按钮
    globalSections_loc = ('link text', 'Global Sections')    # Global Sections菜单

    # Global Sections列表元素
    addBtn_loc = ('xpath', '//*[@id="set_right"]/div/div[1]/div[2]/span[1]')  # 添加按钮

    # 添加页面的元素
    name_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div/table/tbody/tr[1]/td[2]/input') # Name
    displayText_loc = ('xpath', '//*[@id="right_popup"]/div/div[2]/div/table/tbody/tr[2]/td[2]/input') # Display Text
    notes = ('id','dialog_notes') # Notes

    saveBtn_loc = ('xpath', '//*[@id="right_popup"]/div/div[1]/div/span[1]')   # save
    saveAndExitBtn_loc = ('xpath', '//*[@id="right_popup"]/div/div[1]/div/span[2]')  # save and Exit
    exitWithoutSavingBtn_loc = ('xpath', '//*[@id="right_popup"]/div/div[1]/div/span[3]')  # exit without saving

    saveMessage_loc = ('xpath', '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-content"]/div')    # 保存提示对话框
    okBtn_loc = ('xpath', '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input')  # 提示对话框上的‘OK’按钮



    def inputTo(self, Inboxloc, text):
        self.send_keys(Inboxloc, text)





