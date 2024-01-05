# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     JohnDeereTest.py
   Author :        曾良均
   QQ:             277099728
   Date：          7/25/2023 11:27 AM   
   Description :
-------------------------------------------------
   Change Activity:
                   
-------------------------------------------------
"""
__author__ = 'ljzeng'

import unittest
from Page.Credentials.CredentialsPage import CredentialsPage
import os, time
from logger import Log
from Page.loginpage import LoginPage
from operater import browser

log = Log()
path = '.\\report'

# 判断报告目录是否存在
if not os.path.exists(path):
    os.mkdir(path)


class JohnDeereTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        log.info('--------开始测试John Deere Credentials功能--------')
        cls.driver = browser('chromeH')
        cls.login = LoginPage(cls.driver)
        cls.login.login('atcred@iicon004.com', 'Win.12345')
        time.sleep(5)
        log.info('--------成功登录--------')
        cls.to_iframe(cls)

    def to_iframe(self):
        self.cp = CredentialsPage(self.driver)
        self.driver.implicitly_wait(60)
        time.sleep(3)
        coll = self.driver.find_element_by_xpath('//*[@id="nav_arrow"]/div').get_attribute("class")
        while True:
            if coll != 'icn collapse':
                self.driver.find_element_by_id('nav_arrow').click()
                continue
            else:
                log.info('菜单已收折')
                break
        self.cp.click(self.cp.johndeere_menu)
        time.sleep(2)
        self.cp.switch_to_iframe(self.cp.right_iframe)

    def add_jdlink(self):
        time.sleep(1)
        if not self.cp.is_clickable(self.cp.jdlink_add_btn):
            log.info('数据未加载完，等待3秒重试')
            time.sleep(3)
        log.info('点击 JD Link 的Add')
        try:
            self.cp.click(self.cp.jdlink_add_btn)
            time.sleep(1)
            # 跳转到John Deere站点
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(4)
            txt = self.cp.get_text(self.cp.jdlink_page_signin_lable)
        except:
            log.info('Add 跳转失败')
            return False
        else:
            log.info('Add 跳转成功')
            self.driver.switch_to.window(self.driver.window_handles[0])
            if txt == 'Sign In':
                return True
            else:
                return False

    def test01_addJDLink(self):
        '''测试Add JD Link功能'''
        res = self.add_jdlink()
        if res:
            log.info('Add JD Link测试成功！')
        else:
            log.info('Add JD Link测试失败！')
        self.assertTrue(res)

    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(10)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
