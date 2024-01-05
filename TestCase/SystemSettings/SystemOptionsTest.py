# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     SystemOptionsTest.py
   Author :        曾良均
   QQ:             277099728
   Date：          7/18/2022 2:11 PM   
   Description :    测试系统设置项中的功能
-------------------------------------------------
   Change Activity:
                   1、 新建测试：测试单位设置后是否正确显示    --- 曾良均  2022.7.18
-------------------------------------------------
"""
__author__ = 'ljzeng'

import unittest
from operater import browser
from Page.loginpage import LoginPage
from Page.SystemSettings.SystemOptions import SystemOptions
from selenium.webdriver.support.select import Select
from Page.Maps.MapView import MapView
from Page.ManageAssets.ManageAssetsPage import ManageAssetsPage as masp
from logger import Log
import time
from Common.cmdLine import *

log = Log()
path = '.\\report'


class SystemOptionsTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = browser("chrome")
        self.login = LoginPage(self.driver)
        self.login.login("atsysop@iicon004.com", "Win.12345")
        self.driver.implicitly_wait(60)
        log.info('--------开始测试 系统单位设置功能')
        time.sleep(3)
        self.openToSysOption(self)

    def openToSysOption(self):
        self.sysOption = SystemOptions(self.driver)
        self.driver.implicitly_wait(60)
        self.sysOption.click(self.sysOption.settingsMenu_loc)
        self.sysOption.click(self.sysOption.systemsettings_loc)
        self.driver.implicitly_wait(60)
        time.sleep(3)
        st = 1
        while st <= 3:
            try:
                self.sysOption.click(self.sysOption.exButton_loc)
                self.sysOption.click(self.sysOption.sysOption_loc)
                self.driver.implicitly_wait(60)
                time.sleep(3)
            except:
                log.info('第 %s 次打开System Options页面失败' % st)
                time.sleep(2)
                st += 1
            else:
                self.sysOption.click(self.sysOption.exButton_loc)
                self.sysOption.switch_to_iframe(self.sysOption.iframe_loc)
                time.sleep(1)
                log.info('正确打开System Options页面')
                break

    def setunitOdo(self):
        # 获取单位并设置里程单位
        time.sleep(1)
        so = Select(self.driver.find_element_by_xpath('//*[@id="txtOdoUnit"]'))
        un = so.first_selected_option.text
        log.info('当前单位是： %s' % un)
        # 设置单位
        if un == 'Mile':
            self.sysOption.select_by_text(self.sysOption.unitOdo_loc, 'Kilometer')
        else:
            self.sysOption.select_by_text(self.sysOption.unitOdo_loc, 'Mile')

        time.sleep(1)
        # 获取设置后的单位
        so = Select(self.driver.find_element_by_xpath('//*[@id="txtOdoUnit"]'))
        aun = so.first_selected_option.text
        log.info('设置后的单位是： %s' % aun)
        time.sleep(1)
        self.sysOption.click(self.sysOption.saveBtn)
        time.sleep(1)
        self.driver.switch_to.default_content()
        self.sysOption.click(self.sysOption.SaveOK)
        time.sleep(2)
        return aun

    def checkOdoUnit(self, units):
        self.asset = masp(self.driver)
        time.sleep(1)
        try:  # 跳转到机器管理页
            self.asset.click(self.asset.ManageAssetBtn_loc)
            self.driver.implicitly_wait(60)
        except:
            log.info('页面未加载完')
            time.sleep(10)
        else:
            time.sleep(5)
            log.info('在机器管理页面验证设置结果')

        try:   # 确定页面加载完成
            self.asset.click(self.asset.ExButton_loc)
            self.driver.implicitly_wait(30)
        except:
            time.sleep(3)
        finally:
            time.sleep(3)
            self.asset.switch_to_iframe(self.asset.iframe)   # 跳转到机器管理页面
        js = "document.querySelector('#machinelist .data-grid-body').scrollLeft = 1000"
        self.driver.execute_script(js)
        odo_column = self.driver.find_element_by_xpath('//*[@id="machinelist"]/div/table/tr/th[@data-key="Odometer"]')
        odo_column.click()
        while True:  # 判断是否为降序排序
            sorts = self.driver.find_element_by_xpath(
                '//*[@id="machinelist"]/div/table/tr/th[@data-key="Odometer"]/span').get_attribute("class")

            if sorts == "arrow desc":
                break
            else:
                # self.asset.click(self.asset.odo_column)
                odo_column.click()
                continue

        time.sleep(3)
        try:
            self.asset.js_execute("document.getElementById('machinelist').scrollLeft=1000")
            odo_loc = self.asset.get_text(self.asset.odos)
            odounit = odo_loc[-2:]
            log.info('机器里程数据为： %s' % odo_loc)
        except:
            log.info('未取到里程信息')
            return False
        else:
            if units == 'Mile':
                if odounit == 'mi':
                    return True
                else:
                    return False
            else:
                if odounit == 'km':
                    return True
                else:
                    return False

    def test01_odoUnit(self):
        '''测试系统设置Odo单位'''
        uns = self.setunitOdo()
        time.sleep(5)
        # restart = restartService()
        restart = ps()
        time.sleep(5)
        if restart:
            re = self.checkOdoUnit(uns)
            if re:
                log.info('单位设置成功')
            else:
                log.info('单位设置失败')
        else:
            re = False

        self.assertTrue(re)

    @classmethod
    def tearDownClass(cls):
        # cls.driver.execute_script('chrome.settingsPrivate.setDefaultZoom(1);')
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
