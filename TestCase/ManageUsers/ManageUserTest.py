# -*- coding:utf-8 -*-

import unittest
from Page.ManageUsers.ManageUsersPage import UserPage
from Page.loginpage import LoginPage
from Common.logger import Log
import os
from Common.operater import browser
import ddt
import time
from Common.excel import excel
from Common.skiptest import skip_dependon

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file_path = ".\\TestData\\userdata.xls"
testData = excel.get_list(file_path)

log = Log()

path = ".\\report"
if not os.path.exists(path):
    os.mkdir(path)



@ddt.ddt
class ManageUserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.loginer = LoginPage(cls.driver)
        cls.loginer.login('testuserm@iicon004.com', 'Win.12345')
        log.info('--------开始测试用户管理--------')
        cls.driver.implicitly_wait(60)
        cls.to_frame(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def to_frame(self):
        self.user = UserPage(self.driver)
        self.driver.implicitly_wait(60)
        time.sleep(5)
        self.user.switch_to_iframe(self.user.iframe_loc)
        time.sleep(1)

    def search_and_delete(self):
        log.info("Search and delete dirty test data ... ")
        self.user.send_keys(self.user.searchinput_loc, 'Tester11')
        while not self.user.is_clickable(self.user.searchbutton_loc):
            time.sleep(3)
        self.user.click(self.user.searchbutton_loc)
        time.sleep(3)
        self.user.js_execute('window.scrollTo(0, 1000)')
        time.sleep(1)
        try:
            log.info("finding delete element")
            self.user.find_element(self.user.deletebutton_loc)
        except:
            log.info("not find delete element")
            return False
        else:
            log.info("find delete, click it.")
            self.user.click(self.user.deletebutton_loc)
            time.sleep(2)
            log.info("confirm delete")
            self.user.click(self.user.yesbutton_loc)
            time.sleep(1)
            return True

    @ddt.data(*testData)
    def test01_add_user(self, data):
        '''测试添加用户功能'''
        if not self.user.is_clickable(self.user.addbutton_loc):
            log.info('添加按钮不可点击，刷新页面！')
            self.driver.refresh()
            self.driver.implicitly_wait(60)
            time.sleep(10)
            self.user.switch_to_iframe(self.user.iframe_loc)

        log.info("start Test add user  - %s" % data['casename'])
        time.sleep(2)
        self.user.click(self.user.addbutton_loc)
        self.driver.implicitly_wait(60)
        time.sleep(1)
        self.user.switch_to_iframe(self.user.iframeuser_loc)
        self.user.send_keys(self.user.userid_loc, data['userid'])
        time.sleep(2)
        self.user.click(self.user.randompsw_loc)
        time.sleep(1)
        self.user.send_keys(self.user.psw_loc, data['password'])
        self.user.send_keys(self.user.confirmpsw_loc, data['repassword'])
        self.user.send_keys(self.user.username_loc, data['username'])
        time.sleep(1)
        self.user.click(self.user.savebutton_loc)
        time.sleep(3)
        result = self.user.get_text(self.user.boxmsg_loc)
        self.user.click(self.user.boxokbutton_loc)
        time.sleep(3)
        try:
            self.user.click(self.user.withoutsavebutton_loc)
            time.sleep(1)
        except:
            log.info('退出按钮不能操作,等待3秒再试')
            time.sleep(3)
            self.user.click(self.user.withoutsavebutton_loc)
            time.sleep(2)
        self.driver.switch_to.default_content()
        time.sleep(1)
        self.user.switch_to_iframe(self.user.iframe_loc)
        res = (result == data['mess'])
        if res:
            log.info("新建用户测试成功！")
        else:
            log.info("新建用户测试失败！")
        self.assertTrue(res)



    def test02_search(self):
        '''测试搜索用户功能'''
        log.info("Test search and verify add user ... ")
        self.driver.switch_to.default_content()
        self.user.switch_to_iframe(self.user.iframe_loc)
        self.user.send_keys(self.user.searchinput_loc, "Tester11")
        self.user.click(self.user.searchbutton_loc)
        time.sleep(3)
        text = self.user.get_text(self.user.user_loc)
        self.assertEqual(text, "Tester11@iicon004.com")
        log.info("查询成功！")

    @skip_dependon(depend='test02_search')
    def test03_del_user(self):
        '''测试删除用户'''
        res = self.search_and_delete()
        if res:
            log.info('删除成功')
        else:
            log.info('删除失败')
        self.assertTrue(res)

if __name__ == '__main__':
    unittest.main()


