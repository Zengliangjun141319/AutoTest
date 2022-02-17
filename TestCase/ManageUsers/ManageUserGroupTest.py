# -*- coding: utf-8 -*-

from Page.ManageUsers.ManageUserGroupPage import ManageUserGroupPage
from Page.loginpage import LoginPage
from Common.operater import browser
import unittest
import os
from Common.logger import Log
import time
from Common.skiptest import skip_dependon

log = Log()
path = ".\\report"
if not os.path.exists(path):
    os.mkdir(path)

class ManageUserGroupTest(unittest.TestCase):
    current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    groupname = "UserGroup" + current_time
    description = "This user group is created on  " + current_time

    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.login = LoginPage(cls.driver)
        log.info('--------开始测试用户组管理--------')
        cls.login.login("atusergroup@iicon004.com", "Win.12345")
        cls.driver.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def switchto_iframe(self):
        self.usergroup = ManageUserGroupPage(self.driver)
        self.driver.implicitly_wait(60)
        while True:
            if self.usergroup.pageload():
                time.sleep(1)
                break
            else:
                time.sleep(2)
                log.info("页面未加载完，继续等待...")
                continue
        self.usergroup.switch_to_iframe(self.usergroup.iframe_loc)
        time.sleep(3)

    def add_usergroup(self):
        try:
            self.usergroup.click(self.usergroup.addgroupbutton_loc)
            time.sleep(2)
        except:
            log.info("-----打开新增窗口失败-----")
        else:
            log.info("-----打开新增窗口成功-----")
            time.sleep(3)
            self.usergroup.send_keys(self.usergroup.groupname_loc, self.groupname)
            self.usergroup.send_keys(self.usergroup.description_loc, self.description)
            self.usergroup.click(self.usergroup.allselect_loc)
            time.sleep(2)
            self.usergroup.click(self.usergroup.okbuttong_loc)
            time.sleep(3)


    def search_groupnames(self):
        if not self.usergroup.is_clickable(self.usergroup.refreshbutton_loc):
            log.info('刷新按钮不可点击，等待')
            time.sleep(3)
        self.usergroup.click(self.usergroup.refreshbutton_loc)
        time.sleep(3)
        table = self.driver.find_element_by_xpath(".//*[@id='grouplist']/div/div/div/table/tbody")  # 先定位到table
        rows = table.find_elements_by_tag_name("tr")  # 再定位table的行
        rownames = []
        for row in rows:
            col = row.find_element_by_xpath(".//td[1]/span")  # 最后定位行上对应的列
            rowtext = col.text
            rownames.append(rowtext)
        return rownames

    def test01_addUserGroup(self):
        '''测试添加用户组'''
        self.switchto_iframe()
        self.add_usergroup()
        groupnames = self.search_groupnames()
        self.assertIn(self.groupname, groupnames, '新增User Group失败！')


    @skip_dependon(depend='test01_addUserGroup')
    def test02_delUserGroup(self):
        '''删除用户组'''
        groups = self.driver.find_elements_by_xpath('//*[@id="grouplist"]/div/div[1]/div/table/tbody/tr')
        for group in groups:
            groupn = group.find_element_by_xpath('.//td[1]').text
            if groupn == self.groupname:
                try:
                    group.find_element_by_xpath('.//td/a[@title="Edit"]').click()
                    time.sleep(1)
                except:
                    res = False
                else:
                    self.driver.find_element_by_xpath('//*[@id="tab_groupinfo"]/table[2]/tbody/tr/td[2]/input[4]').click()
                    time.sleep(1)
                    self.driver.find_element_by_xpath(".//*[@id='dialog_user_group']/div[3]/input[2]").click()
                    time.sleep(3)
                # delete
                try:
                    group.find_element_by_xpath('.//td/a[@title="Delete"]').click()
                except:
                    res = False
                else:
                    self.driver.switch_to.default_content()
                    time.sleep(1)
                    self.driver.find_element_by_xpath('/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input[2]').click()
                    res = True
                    log.info("删除用户组 %s 成功" % groupn)
        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()