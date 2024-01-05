# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     CredentialsTest.py
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
from skiptest import skip_dependon

log = Log()
path = '.\\report'

# 判断报告目录是否存在
if not os.path.exists(path):
    os.mkdir(path)

lists_loc = '//*[@id="credentiallist"]/div/div[1]/div/table/tbody/tr'


class CredentialsTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        log.info('--------开始测试Credentials功能--------')
        cls.driver = browser('chrome')
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

        self.cp.switch_to_iframe(self.cp.right_iframe)

    def add_credential(self):
        # 点击Add 新建Credential
        time.sleep(1)
        if not self.cp.is_clickable(self.cp.cred_add_btn):
            time.sleep(2)
        log.info('新建Credentials')
        pre_list = self.driver.find_elements_by_xpath(lists_loc)
        try:
            self.cp.click(self.cp.cred_add_btn)
            time.sleep(1)
            self.cp.click(self.cp.cred_add_urlkey_inbox)
        except:
            log.info('打开Add Credential失败')
            return False
        else:
            log.info('打开Add Credential窗口成功，开始输入信息...')
            try:
                self.cp.send_keys(self.cp.cred_add_urlkey_inbox, 'auto test url key')
                self.cp.send_keys(self.cp.cred_add_username_inbox, 'AutoTest')
                self.cp.send_keys(self.cp.cred_add_passwd_inbox, 'test')
                self.cp.click(self.cp.cred_add_ok_btn)
                time.sleep(2)
            except:
                log.info('输入Credential信息失败')
                return False
            else:
                log.info('信息已保存，结果待验证......')
                nex_list = self.driver.find_elements_by_xpath(lists_loc)
                if len(nex_list) == len(pre_list) + 1:
                    return True
                else:
                    return False

    def del_credential(self):
        time.sleep(1)
        if not self.cp.is_clickable(self.cp.cred_refresh_btn):
            log.info('数据未加载完，等待3秒重试！')
            time.sleep(3)
        pre_list = self.driver.find_elements_by_xpath(lists_loc)
        log.info('测试删除Credentials')
        try:
            self.cp.click(self.cp.cred_list_del_btn)
            time.sleep(1)
            try:
                self.cp.click(self.cp.cred_del_yes_btn)
                time.sleep(2)
            except:
                self.driver.switch_to.default_content()
                self.cp.click(self.cp.cred_del_yes_btn)
                time.sleep(2)
                self.cp.switch_to_iframe(self.cp.right_iframe)
            self.cp.click(self.cp.cred_refresh_btn)
            time.sleep(2)
        except:
            log.info('删除操作失败')
            return False
        else:
            log.info('已完成删除操作，结果待验证......')
            next_list = self.driver.find_elements_by_xpath(lists_loc)
            if len(next_list) == len(pre_list) - 1:
                return True
            else:
                return False

    def test01_addcred(self):
        '''测试新建Credentials'''
        res = self.add_credential()
        if res:
            log.info('新建Credentials成功！')
        else:
            log.info('新建Credentials失败！')
        self.assertTrue(res)

    @skip_dependon(depend='test01_addcred')
    def test02_delCred(self):
        '''测试删除Credentials'''
        res = self.del_credential()
        if res:
            log.info('删除Credentials成功！')
        else:
            log.info('删除Credentials失败！')
        self.assertTrue(res)

    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(10)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
