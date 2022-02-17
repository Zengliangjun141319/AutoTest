# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     PermissionTest.py
   Description :
   Author :        曾良均
   QQ:             277099728
   Date：          10/27/2021 5:12 PM
-------------------------------------------------
   Change Activity:
                   10/27/2021:
-------------------------------------------------
"""
__author__ = 'ljzeng'

import unittest
from Common.operater import browser
from Page.loginpage import LoginPage
from Common.logger import Log
import os
import ddt
from Common.excel import excel
from Common.setPermissions import setPermission
import time
import sys

log = Log()
path = '.\\report'

if not os.path.exists(path):
    os.mkdir(path)

# Jobsite权限测试数据
jobsitepermission_file = ".\\TestData\\jobsitePermission.xlsx"
jobsitePermissionData = excel.get_list(jobsitepermission_file)

# Asset Health权限测试数据
AssetHealthPer_file = ".\\TestData\\AssetHealthPermission.xlsx"
AssetHealthPerData = excel.get_list(AssetHealthPer_file)

# Inspection权限测试数据
inspectionPer_file = ".\\TestData\\InspectionPermission.xlsx"
inspectionPerData = excel.get_list(inspectionPer_file)

# 其他权限测试数据
otherPer_file = ".\\TestData\\OtherPermission.xlsx"
otherPerData = excel.get_list(otherPer_file)

@ddt.ddt
class PermissionTest(unittest.TestCase):
    # 元素位置
    home_menu = ('id', 'button_home')
    jobsites_home_loc = ('xpath', '//*[@id="sysModules"]/div[@title="Jobsites"]')
    assethealth_home_loc = ('xpath', '//*[@id="sysModules"]/div[@title="Asset Health"]')

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = browser()
        log.info("权限相关功能测试 ---- ")
        cls.login = LoginPage(cls.driver)
        cls.login.login('atpermission@iicon004.com', 'Win.12345')
        cls.driver.implicitly_wait(60)
        time.sleep(10)


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @ddt.data(*jobsitePermissionData)
    def test01_jobsitePermission(self, data):
        '''测试用户对Jobsites相关权限'''
        log.info('测试Jobsite权限 -- %s' % data['casename'])
        self.driver.find_element_by_id('button_home').click()
        # log.info('设置权限')
        setr = setPermission(data['clientdata'])
        time.sleep(2)
        pers = []
        if setr:
            # log.info('检查设置结果')  # 权限设置成功，界面可以操作
            self.driver.refresh()
            self.driver.implicitly_wait(40)
            time.sleep(2)
            ti = 1
            while ti <= 3:
                try:
                    self.driver.find_element_by_xpath('//*[@id="sysModules"]/div[@title="Jobsites"]').click()
                    self.driver.implicitly_wait(60)
                except:
                    # log.info('第 %s 次跳转Jobsite失败，重试' % ti)
                    time.sleep(2)
                    ti += 1
                else:
                    # log.info('第 %s 次跳转Jobsite成功' % ti)
                    break
            time.sleep(5)
            try:
                lst = self.driver.find_elements_by_xpath('//*[@id="set_left"]/ul/li')
                for l in lst:
                    if l.get_attribute('title'):
                        pers.append(l.get_attribute('title'))
            except:
                log.info('菜单项未找到')
                res = False
            else:
                expect = str(data['expect']).split(',')
                res = (expect == pers)
        else:
            res = False

        if res:
            log.info('------测试成功')
        else:
            log.info('------测试失败')
        self.assertTrue(res)

    @ddt.data(*AssetHealthPerData)
    def test02_AssetHealthPermission(self, data):
        '''测试用户对Asset Health相关权限'''
        log.info('测试Asset Health权限 -- %s' % data['casename'])
        self.driver.find_element_by_id('button_home').click()
        # log.info('设置权限')
        setr = setPermission(data['clientdata'])
        time.sleep(2)
        pers = []
        if setr:
            # log.info('检查设置结果')  # 权限设置成功，界面可以操作
            self.driver.refresh()
            self.driver.implicitly_wait(40)
            time.sleep(2)
            ti = 1
            while ti <= 3:
                try:
                    self.driver.find_element_by_xpath('//*[@id="sysModules"]/div[@title="Asset Health"]').click()
                    self.driver.implicitly_wait(60)
                except:
                    # log.info('第 %s 次跳转Asset Health失败，重试' % ti)
                    time.sleep(2)
                    ti += 1
                else:
                    # log.info('第 %s 次跳转Asset Health成功' % ti)
                    break

            time.sleep(5)
            try:
                lst = self.driver.find_elements_by_xpath('//*[@id="set_left"]/ul/li')
                for l in lst:
                    if l.get_attribute('title'):
                        pers.append(l.get_attribute('title'))
            except:
                log.info('菜单项未找到')
                res = False
            else:
                expect = str(data['expect']).split(',')
                res = (expect == pers)
        else:
            res = False

        if res:
            log.info('------测试成功')
        else:
            log.info('------测试失败')
        self.assertTrue(res)

    @ddt.data(*inspectionPerData)
    def test03_inspectionPermission(self, data):
        '''测试用户对inspection相关权限'''
        log.info('测试Inspection权限 -- %s' % data['casename'])
        self.driver.find_element_by_id('button_home').click()
        # log.info('设置权限')
        setr = setPermission(data['clientdata'])
        time.sleep(2)
        pers = []
        if setr:
            # log.info('检查设置结果')  # 权限设置成功，界面可以操作
            self.driver.refresh()
            self.driver.implicitly_wait(40)
            time.sleep(2)
            ti = 1
            while ti <= 3:
                try:
                    self.driver.find_element_by_xpath('//*[@id="sysModules"]/div[@title="Inspection"]').click()
                    self.driver.implicitly_wait(60)
                except:
                    # log.info('第 %s 次跳转Inspection失败，重试' % ti)
                    time.sleep(2)
                    ti += 1
                else:
                    # log.info('第 %s 次跳转Inspection成功' % ti)
                    break

            time.sleep(5)
            try:
                lst = self.driver.find_elements_by_xpath('//*[@id="set_left"]/ul/li')
                for l in lst:
                    if l.get_attribute('title'):
                        pers.append(l.get_attribute('title'))
            except:
                log.info('菜单项未找到')
                res = False
            else:
                expect = str(data['expect']).split(',')
                res = (expect == pers)
        else:
            res = False

        if res:
            log.info('------测试成功')
        else:
            log.info('------测试失败')
        self.assertTrue(res)

    @ddt.data(*otherPerData)
    def test04_otherPermission(self, data):
        '''测试用户对其他设置项相关权限'''
        log.info('测试其他设置项权限 -- %s' % data['casename'])
        self.driver.find_element_by_id('button_home').click()
        # log.info('设置权限')
        setr = setPermission(data['clientdata'])
        time.sleep(2)
        pers = []
        if setr:
            # log.info('检查设置结果')  # 权限设置成功，界面可以操作
            self.driver.refresh()
            self.driver.implicitly_wait(60)
            time.sleep(5)
            try:
                lst = self.driver.find_elements_by_xpath('//*[@id="sysModules"]/div')
                for l in lst:
                    if l.get_attribute('title'):
                        pers.append(l.get_attribute('title'))
            except:
                log.info('菜单项未找到')
                res = False
            else:
                expect = str(data['expect']).split(',')
                res = (expect == pers)
        else:
            res = False

        if res:
            log.info('------测试成功')
        else:
            log.info('------测试失败')
        self.assertTrue(res)

if __name__ == '__main__':
    unittest.main()
