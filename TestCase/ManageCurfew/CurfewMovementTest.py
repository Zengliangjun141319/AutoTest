# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     CurfewMovementTest.py
   Author :        曾良均
   QQ:             277099728
   Date：          4/19/2023 11:16 AM   
   Description :
-------------------------------------------------
   Change Activity:
                   
-------------------------------------------------
"""
__author__ = 'ljzeng'

import unittest
from Page.TeamIntelligence.GlobalSectionPage import GlobalSectionPage
from Page.Curfew.CurfewMovementPage import CurfewMovementPage as cmp
from operater import browser
from Page.loginpage import LoginPage
from logger import Log
import time
import random

log = Log()
path = '.\\report'


class CurfewMovementTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser("chromeH")
        cls.login = LoginPage(cls.driver)
        cls.login.login("autotester@foresight.com", "1")
        cls.driver.implicitly_wait(60)
        log.info("------ 开始测试Curfew Movement设置")
        cls.open_customer(cls)

    def open_customer(self):
        self.gs = GlobalSectionPage(self.driver)
        self.gs.click(self.gs.customerlink_loc)
        time.sleep(5)
        self.gs.send_keys(self.gs.searchinput_loc, '004')
        self.gs.click(self.gs.searchbutton_loc)
        time.sleep(2)
        self.gs.click(self.gs.customeropen_loc)
        all_h = self.driver.window_handles
        self.driver.switch_to.window(all_h[1])
        self.openCurfewMovment(self)

    def openCurfewMovment(self):
        self.cm = cmp(self.driver)
        self.driver.implicitly_wait(60)
        # 跳到地图页
        self.cm.click(self.cm.settingsBtn_loc)
        self.cm.click(self.cm.curfewconmenu_loc)
        time.sleep(1)
        self.cm.click(self.cm.curfewmov_loc)
        time.sleep(2)
        self.cm.switch_to_iframe(self.cm.curfewFrame_loc)
        try:
            self.cm.click(self.cm.refresh_loc)
            time.sleep(2)
        except:
            log.info("打开Curfew Movement页面失败")

    def setTolerance(self):
        tolvalue = random.random()   # 生成一个随机数，用于设置Tolerance
        tolvalue = str(round(tolvalue, 4))
        log.info('设置Tolerance为： %s' % tolvalue)
        try:
            self.cm.send_keys(self.cm.defaultTol_loc, tolvalue)
            time.sleep(1)
        except:
            log.info('设置Tolerance失败')
            return False
        else:
            self.cm.click(self.cm.savebtn_loc)
            time.sleep(1)
            try:
                self.cm.click(self.cm.saveOK_loc)
                self.driver.implicitly_wait(60)
                time.sleep(5)
            except:
                self.driver.switch_to.default_content()
                self.cm.click(self.cm.saveOK_loc)
                self.driver.implicitly_wait(60)
                time.sleep(5)
                self.cm.switch_to_iframe(self.cm.curfewFrame_loc)

        # 获取保存后的值
        defaulttol = self.cm.get_attribute(self.cm.defaultTol_loc, 'value')
        log.info('设置后的值为： %s' % defaulttol)
        if defaulttol == tolvalue:
            return True
        else:
            return False

    def test_settolerance(self):
        '''测试设置curfew movement tolerance'''
        res = self.setTolerance()
        if res:
            log.info('curfew movement tolerance设置成功！')
        else:
            log.info('curfew movement tolerance设置失败！')
        self.assertTrue(res)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
