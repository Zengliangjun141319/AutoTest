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
from logger import Log
import time
from Common.cmdLine import restartService

log = Log()
path = '.\\report'


class SystemOptionsTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = browser()
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
                self.sysOption.click(self.sysOption.sysOption_loc)
                self.driver.implicitly_wait(60)
                time.sleep(3)
            except:
                log.info('第 %s 次打开System Options页面失败' % st)
                time.sleep(2)
                st += 1
            else:
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
        self.maps = MapView(self.driver)
        self.driver.refresh()
        # Open Maps
        try:
            self.maps.click(self.maps.mapmenu_loc)
            self.driver.implicitly_wait(60)
        except:
            log.info('地图菜单不可点击，刷新再试')
            self.driver.refresh()
            self.driver.implicitly_wait(60)
            time.sleep(5)
            self.maps.click(self.maps.mapmenu_loc)
            self.driver.implicitly_wait(60)
        while True:
            if self.maps.pageload():
                time.sleep(1)
                break
            else:
                time.sleep(2)
                log.info("页面未加载完，继续等待...")
                continue
        time.sleep(2)
        self.driver.implicitly_wait(60)
        self.maps.click(self.maps.ExButton_loc)
        time.sleep(1)
        try:
            self.maps.send_keys(self.maps.searchInbox_loc, "josh's")
            self.maps.select_by_text(self.maps.selOnroad_loc, 'Onroad')
            time.sleep(1)
            self.maps.click(self.maps.searchButton_loc)
            self.driver.implicitly_wait(60)
            time.sleep(3)
        except:
            log.info('机器过滤及搜索操作失败')
            return False
        else:
            # 点击第一台机器
            try:
                self.maps.click(self.maps.firstAssetLink_loc)
            except:
                log.info('选择机器失败')
                return False
            else:
                # 获取机器Odometer的单位
                odo = self.maps.get_text(self.maps.odounit_loc)
                odounit = odo[-2:]
                log.info('地图上机器里程单位为： %s' % odounit)

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
        time.sleep(10)
        restart = restartService()
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
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
