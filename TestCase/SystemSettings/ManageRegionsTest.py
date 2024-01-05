# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ManageRegionsTest.py
   Description :
   Author :        曾良均
   QQ:             277099728
   Date：          1/13/2022 3:06 PM
-------------------------------------------------
   Change Activity:
                   1/13/2022:
-------------------------------------------------
"""
__author__ = 'ljzeng'

import unittest
from Page.SystemSettings.ManageRegions import ManageRegions
from operater import browser
from Page.loginpage import LoginPage
from logger import Log
import time

log = Log()
path = '.\\report'
current_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))


class ManageRegionsTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = browser("chromeH")
        self.login = LoginPage(self.driver)
        self.login.login("atregion@iicon001.com", "Win.12345")
        self.driver.implicitly_wait(60)
        log.info('--------开始测试 Region管理')
        time.sleep(3)
        self.openToManageRegion(self)

    def openToManageRegion(self):
        self.manageregion = ManageRegions(self.driver)
        self.driver.implicitly_wait(60)
        self.manageregion.click(self.manageregion.settingsMenu_loc)
        self.manageregion.click(self.manageregion.systemsettings_loc)
        self.driver.implicitly_wait(60)
        time.sleep(3)
        st = 1
        while st <= 3:
            try:
                self.manageregion.click(self.manageregion.manageregion_loc)
                self.driver.implicitly_wait(60)
                time.sleep(3)
            except:
                log.info('第 %s 次打开Region管理页面失败' % st)
                time.sleep(2)
                st += 1
            else:
                self.manageregion.switch_to_iframe(self.manageregion.iframe_loc)
                time.sleep(1)
                log.info('正确打开Region管理页面')
                break

    def createRegion(self):
        # 新建Region
        try:
            self.manageregion.click(self.manageregion.addBtn_loc)
            time.sleep(1)
        except:
            log.info('打开Add Region失败')
        else:
            log.info('开始录入Region信息')
            self.manageregion.send_keys(self.manageregion.regionname_loc, current_time)
            self.manageregion.send_keys(self.manageregion.startdate_loc, current_time)
            time.sleep(1)
            self.manageregion.send_keys(self.manageregion.projectdate_loc, current_time)
            time.sleep(1)
            self.manageregion.send_keys(self.manageregion.enddate_loc, current_time)
            time.sleep(1)
            self.manageregion.send_keys(self.manageregion.notes_loc, 'Auto Test Add region at ' + current_time)
            time.sleep(2)
            self.manageregion.click(self.manageregion.okBtn)
            time.sleep(2)

    def delRegion(self, regiona):
        time.sleep(1)
        regionlist = self.driver.find_elements_by_xpath('//*[@id="regionlist"]/div/div[1]/div/table/tbody/tr')
        for l in regionlist:
            names = l.find_element_by_xpath('./td/span')
            if names.text == regiona:
                l.find_element_by_xpath('./td/a[@title="Delete"]').click()
                time.sleep(1)
                try:
                    self.manageregion.click(self.manageregion.delOK_loc)
                    time.sleep(3)
                except:
                    self.driver.switch_to.default_content()
                    self.manageregion.click(self.manageregion.delOK_loc)
                    self.manageregion.switch_to_iframe(self.manageregion.iframe_loc)
                    time.sleep(3)
                log.info('删除动作已执行，待验证结果')
                return True
        else:
            return False

    def searchRegion(self, regiona):
        self.driver.implicitly_wait(60)
        try:
            time.sleep(1)
            self.manageregion.click(self.manageregion.refresh_loc)
        except:
            log.info('列表数据未加载完，等待3秒')
            time.sleep(3)
        else:
            time.sleep(3)

        regionlist = self.driver.find_elements_by_xpath('//*[@id="regionlist"]/div/div[1]/div/table/tbody/tr')
        for l in regionlist:
            names = l.find_element_by_xpath('./td/span')
            if names.text == regiona:
                return True
        else:
            return False

    def test01_addRegion(self):
        '''测试新建Region'''
        self.createRegion()
        res = self.searchRegion(current_time)
        if res:
            log.info('添加Region成功')
        else:
            log.info('添加Region失败')
        self.assertTrue(res)

    def test02_delregion(self):
        '''测试删除Region功能'''
        res = True
        if self.delRegion(current_time):
            res = self.searchRegion(current_time)

        if not res:
            log.info('删除成功')
        else:
            log.info('删除失败')
        self.assertFalse(res)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()




if __name__ == '__main__':
    unittest.main()
