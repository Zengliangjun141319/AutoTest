# -*- coding:utf-8 -*-

import unittest
from Page.ManageUsers.ManageUsersPage import UserPage
from Page.loginpage import LoginPage
from logger import Log
import os
from operater import browser
import ddt
import time
from excel import excel
from skiptest import skip_dependon
from queryMSSQL import getTempPassword

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file_path = ".\\TestData\\userdata.xls"
testData = excel.get_list(file_path)

log = Log()

path = ".\\report"
if not os.path.exists(path):
    os.mkdir(path)


@ddt.ddt
class ManageUserTest(unittest.TestCase):
    loginer = None
    driver = None

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
        coll = self.driver.find_element_by_xpath('//*[@id="nav_arrow"]/div').get_attribute("class")
        while True:
            if coll != 'icn collapse':
                self.driver.find_element_by_id('nav_arrow').click()
                continue
            else:
                log.info('菜单已收折')
                break
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
            try:
                self.user.click(self.user.yesbutton_loc)
                time.sleep(1)
            except:
                self.driver.switch_to.default_content()
                self.user.click(self.user.yesbutton_loc)
                self.user.switch_to_iframe(self.user.iframe_loc)
            return True

    def assign_asset(self):
        self.driver.switch_to.default_content()
        self.user.switch_to_iframe(self.user.iframe_loc)
        self.user.send_keys(self.user.searchinput_loc, "TestAssign")
        self.user.click(self.user.searchbutton_loc)
        time.sleep(2)
        self.user.js_execute("window.scrollTo(0, 1000)")
        self.user.click(self.user.assetass_loc)
        time.sleep(2)
        try:
            self.user.click(self.user.firstcheckbox_loc)
            log.info("用户当前存在已分配的机器，下面删除已分配的机器！")
            self.user.click(self.user.allselect_loc)
            self.user.click(self.user.delectass_loc)
            self.user.click(self.user.infoyes_loc)
        except:
            log.info("用户当前不存在已分配的机器。")
        self.user.click(self.user.addasset_loc)
        time.sleep(5)
        self.user.send_keys(self.user.searchassetinput_loc, 'BNH01381')
        self.user.click(self.user.searchassetbutton_loc)
        try:
            self.user.click(self.user.assetcheckbox_loc)
        except:
            log.info("-----未查询到所需的机器-----")
        self.user.click(self.user.assetok_loc)
        self.user.click(self.user.assetwindowclose_loc)
        self.user.click(self.user.assetass_loc)
        text = self.user.get_text(self.user.assetinfo_loc)
        time.sleep(2)
        self.user.click(self.user.assetwindowclose_loc)
        time.sleep(2)

        if text == 'BNH01381':
            return True
        else:
            return False

    def assign_assetgroup(self):
        time.sleep(3)
        self.driver.switch_to.default_content()
        self.user.switch_to_iframe(self.user.iframe_loc)
        self.user.send_keys(self.user.searchinput_loc, "TestAssign")
        self.user.click(self.user.searchbutton_loc)
        time.sleep(2)
        self.user.js_execute("window.scrollTo(0, 1000)")
        self.user.click(self.user.assetgroup_loc)
        time.sleep(2)
        try:
            self.user.click(self.user.selectedgourp_loc)
            log.info("用户当前存在已分配的机器组，删除已存在的机器组。")
            self.user.click(self.user.allgroupremove_loc)
            self.user.click(self.user.groupok_loc)
            self.user.click(self.user.assetgroup_loc)
        except:
            log.info("当前用户不存在已分配的机器组！")
        log.info("为用户分配机器组：")
        self.user.click(self.user.availablegroup_loc)
        text1 = self.user.get_text(self.user.availablegroup_loc)
        self.user.click(self.user.groupaddedbutton_loc)
        self.user.click(self.user.groupok_loc)
        self.user.click(self.user.assetgroup_loc)
        time.sleep(1)
        text2 = self.user.get_text(self.user.selectedgourp_loc)
        self.user.click(self.user.groupok_loc)
        time.sleep(2)

        if text1 == text2:
            return True
        else:
            return False

    def assign_assettype(self):
        time.sleep(3)
        self.driver.switch_to.default_content()
        self.user.switch_to_iframe(self.user.iframe_loc)
        self.user.send_keys(self.user.searchinput_loc, "TestAssign")
        self.user.click(self.user.searchbutton_loc)
        time.sleep(2)
        self.user.js_execute("window.scrollTo(0, 1000)")
        try:
            self.user.click(self.user.assettype_loc)
            time.sleep(2)
        except:
            log.info('打开Asset Type Assignment页面失败')
            return False
        else:
            try:
                self.user.click(self.user.selectedtype_loc)
                log.info("用户当前存在已分配的机器类型，删除已存在的机器类型。")
                self.user.click(self.user.alltyperemove_loc)
                self.user.click(self.user.typeok_loc)
                self.user.click(self.user.assettype_loc)
            except:
                log.info("用户当前不存在已分配的机器类型！")
            finally:
                log.info("为用户分配机器类型：")
                self.user.click(self.user.availabletype_loc)
                text1 = self.user.get_text(self.user.availabletype_loc)
                self.user.click(self.user.typeaddedbuttion_loc)
                self.user.click(self.user.typeok_loc)
                self.user.click(self.user.assettype_loc)
                time.sleep(1)
                text2 = self.user.get_text(self.user.selectedtype_loc)
                self.user.click(self.user.typeok_loc)
                time.sleep(2)
                if text1 == text2:
                    return True
                else:
                    return False

    def reset_password(self):
        self.driver.switch_to.default_content()
        self.user.switch_to_iframe(self.user.iframe_loc)
        self.user.send_keys(self.user.searchinput_loc, "TestAssign")
        self.user.click(self.user.searchbutton_loc)
        time.sleep(2)
        self.user.js_execute("window.scrollTo(0, 1000)")
        self.user.click(self.user.resetpw_loc)
        time.sleep(1)
        self.user.click(self.user.randomcheckbox_loc)
        self.user.click(self.user.okbutton_loc)
        try:
            self.user.click(self.user.resetok_loc)
        except:
            self.driver.switch_to.default_content()
            self.user.click(self.user.resetok_loc)
            self.user.switch_to_iframe(self.user.iframe_loc)

    @ddt.data(*testData)
    def test01_add_user(self, data):
        """测试添加用户功能"""
        if not self.user.is_clickable(self.user.addbutton_loc):
            log.info('添加按钮不可点击，刷新页面！')
            self.driver.refresh()
            self.driver.implicitly_wait(60)
            time.sleep(10)
            # self.driver.find_element_by_id('nav_arrow').click()
            # time.sleep(1)
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

    def test02_search_user(self):
        """测试搜索用户功能"""
        log.info("Test search and verify add user ... ")
        self.driver.switch_to.default_content()
        self.user.switch_to_iframe(self.user.iframe_loc)
        self.user.send_keys(self.user.searchinput_loc, "Tester11")
        self.user.click(self.user.searchbutton_loc)
        time.sleep(3)
        text = self.user.get_text(self.user.user_loc)
        self.assertEqual(text, "Tester11@iicon004.com")
        log.info("查询成功！")

    @skip_dependon(depend='test02_search_user')
    def test03_del_user(self):
        """测试删除用户"""
        res = self.search_and_delete()
        if res:
            log.info('删除成功')
        else:
            log.info('删除失败')
        self.assertTrue(res)

    def test04_assign_asset(self):
        """测试分用户分配机器"""
        res = self.assign_asset()
        if self.assertTrue(res, True):
            log.info("分配机器失败！")
        else:
            log.info("分配机器成功！")

    def test05_assign_asset_group(self):
        """测试为用户分配机器组"""
        res = self.assign_assetgroup()
        if self.assertTrue(res, True):
            log.info("分配机器组失败！")
        else:
            log.info("分配机器组成功！")

    def test06_assign_asset_type(self):
        """测试为用户分配机器类型"""
        res = self.assign_assettype()
        if self.assertTrue(res, True):
            log.info("分配机器类型失败！")
        else:
            log.info("分配机器类型成功！")


if __name__ == '__main__':
    unittest.main()


