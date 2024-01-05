# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     APICredentialsTest.py
   Author :        曾良均
   QQ:             277099728
   Date：          7/25/2023 11:28 AM   
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
from selenium.webdriver.support.select import Select
from skiptest import skip_dependon

log = Log()
path = '.\\report'

# 判断报告目录是否存在
if not os.path.exists(path):
    os.mkdir(path)
current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
name = 'AutoTest' + current_time


class APICredentialsTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        log.info('--------开始测试API Credentials功能--------')
        cls.driver = browser('chromeH')
        cls.login = LoginPage(cls.driver, 'https://fleet.foresightintelligence.com')
        cls.login.login('jack@087.com', 'Win.12345')
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
        self.cp.click(self.cp.apicred_menu)
        time.sleep(2)
        self.cp.switch_to_iframe(self.cp.right_iframe)

    def add_apicred(self):
        try:
            self.cp.click(self.cp.api_add_btn)
            time.sleep(2)
            Select(self.driver.find_element_by_id('dialog_apiname')).select_by_value('3')
            time.sleep(1)
            self.cp.send_keys(self.cp.api_username_inbox, name)
            self.cp.send_keys(self.cp.api_pwd_inbox, 'Win.12345')
            self.cp.click(self.cp.api_ok_btn)
            time.sleep(2)
        except:
            log.info('Add API Credentials失败')
            return False
        else:
            log.info('Add API Credentials成功，结果待验证...')
            self.cp.click(self.cp.api_refresh_btn)
            time.sleep(3)
            cred_lists = self.driver.find_elements_by_xpath('//*[@id="credentiallist"]/div/div[1]/div/table/tbody/tr')
            for l in cred_lists:
                apiname = l.find_element_by_xpath('./td[2]/span').text
                # log.info('API Credentials的用户名为： %s' % apiname)
                if apiname == name:
                    return True
            else:
                return False

    def del_api_cred(self):
        try:
            self.cp.click(self.cp.api_refresh_btn)
            time.sleep(3)
            loc = '//span[text()="%s"]/../../td/a[@title="Delete"]' % name
            # log.info('\n查找位置： %s' % loc)
            self.driver.find_element_by_xpath(loc).click()
            time.sleep(1)
        except:
            log.info('查找及删除操作失败')
            return False
        else:
            log.info('已点击删除按钮')
            try:
                self.cp.click(self.cp.api_del_yes_btn)
            except:
                self.driver.switch_to.default_content()
                self.cp.click(self.cp.api_del_yes_btn)
                time.sleep(2)
                self.cp.switch_to_iframe(self.cp.right_iframe)
            finally:
                log.info('已完成删除操作，结果待验证...')

            lists = self.driver.find_elements_by_xpath(
                    '//*[@id="credentiallist"]/div/div[1]/div/table/tbody/tr')
            for list in lists:
                apiname = list.find_element_by_xpath('./td[2]/span').text
                if apiname == name:
                    return False
            else:
                log.info('未找到已删除的用户名')
                return True

    def test01_add_creds(self):
        '''测试新建API Credentials'''
        res = self.add_apicred()
        if res:
            log.info('新建API Credentials成功！')
        else:
            log.info('新建API Credentials失败！')
        self.assertTrue(res)

    @skip_dependon(depend='test01_add_creds')
    def test02_del_creds(self):
        '''测试删除API Credentials'''
        res = self.del_api_cred()
        if res:
            log.info('删除API测试成功！')
        else:
            log.info('删除API测试失败！')
        self.assertTrue(res)

    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(10)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
