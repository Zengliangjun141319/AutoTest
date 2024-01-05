# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     InspectLayoutTest.py
   Description :
   Author :        曾良均
   QQ:             277099728
   Date：          1/27/2022 8:36 AM
-------------------------------------------------
   Change Activity:
                   1/27/2022:
-------------------------------------------------
"""
__author__ = 'ljzeng'

import unittest
from Page.Inapection.InspectionLayoutPage import InspectionLayoutPage
import time,os
from datetime import datetime
from logger import Log
from operater import browser
from Page.loginpage import LoginPage
from skiptest import skip_dependon

log = Log()
path = '.\\report'
isExists = os.path.exists(path)
if not isExists:
    os.mkdir(path)

na = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
editname = na + 'edit'

class InspectLayoutTest(unittest.TestCase):
    def time_format(self):
        current_time = datetime.now().strftime("%Y.%m.%d.%H%M%S.%f")[:-3]
        return current_time

    @classmethod
    def setUpClass(self):
        self.driver = browser("chromeH")
        self.login = LoginPage(self.driver)
        self.login.login('atInsLayout@iicon004.com', 'Win.12345')
        log.info('--------开始测试Inspection Layout设置--------')
        self.driver.implicitly_wait(60)
        time.sleep(3)
        self.openLayout(self)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def openLayout(self):
        self.layout = InspectionLayoutPage(self.driver)
        time.sleep(3)
        while True:
            try:
                self.layout.click(self.layout.exButton_loc)
                self.layout.click(self.layout.layoutsMu_loc)
            except:
                log.info('打开Layout失败，3秒后重试')
                time.sleep(3)
            else:
                log.info('正确打开Layout')
                time.sleep(3)
                self.layout.click(self.layout.exButton_loc)
                break

    def add_layout(self):
        try:
            self.layout.click(self.layout.refreshBtn_loc)
            time.sleep(3)
        except:
            log.info('Layouts列表刷新失败，等待3秒')
            time.sleep(3)
        finally:
            # log.info('Layouts列表刷新成功')
            time.sleep(2)

        try:
            self.layout.click(self.layout.addBtn_loc)
            time.sleep(2)
        except:
            log.info('Layout设置页面打开失败')
            return False
        else:
            log.info('layout设置页面打开成功,开始输入信息')
            try:
                self.layout.send_keys(self.layout.layoutNameinbox_loc, na)
                # self.layout.click(self.layout.includelogoCh_loc)    # 已取消

                note = 'Add Layout at ' + self.time_format()
                self.layout.send_keys(self.layout.notesInbox_loc, note)
                time.sleep(1)

                leftheader = 'Left Header [Advisor] ' + self.time_format()
                self.layout.send_keys(self.layout.leftHeaderInbox_loc, leftheader)
                time.sleep(1)

                midheader = 'Middle Header [Asset_Name_Custom] ' + self.time_format()
                self.layout.send_keys(self.layout.midHeaderInbox_loc, midheader)
                time.sleep(1)

                rightheader = 'Right Header [Work_Order_Number] ' + self.time_format()
                self.layout.send_keys(self.layout.rightHeaderInbox_loc, rightheader)
                time.sleep(1)

                leftfoot = 'Left Footer [Current_Location] ' + self.time_format()
                self.layout.send_keys(self.layout.leftFooterInbox_loc, leftfoot)
                time.sleep(1)

                midfoot = 'Middle Footers [VIN] ' + self.time_format()
                self.layout.send_keys(self.layout.midFooterInbox_loc, midfoot)
                time.sleep(1)

                rightfoot = 'Right Footers [Contacts] ' + self.time_format()
                self.layout.send_keys(self.layout.rightFooterInbox_loc, rightfoot)
                time.sleep(1)

                try:
                    self.layout.click(self.layout.saveBtn_loc)
                    time.sleep(1)
                    mess = self.layout.get_text(self.layout.saveLayoutmess_loc)
                except:
                    log.info('保存Layout操作失败')
                    return False
                else:
                    self.layout.click(self.layout.saveLyoutOk_loc)
                    time.sleep(2)
                    self.layout.click(self.layout.exitBtn_loc)
                    time.sleep(3)
                    if mess == 'Saved successfully.':
                        return True
            except:
                log.info('编辑Layout操作失败')
                return False


    def searchLayout(self, nas=na):
        try:
            self.layout.click(self.layout.refreshBtn_loc)
            time.sleep(1)
        except:
            log.info('Layouts列表刷新失败，等待3秒')
            time.sleep(3)
        else:
            # log.info('Layouts列表刷新成功')
            time.sleep(2)

        self.layout.send_keys(self.layout.searchInbox_loc, nas)
        self.layout.click(self.layout.searchBt_loc)
        time.sleep(2)
        try:
            searchre = self.layout.get_text(self.layout.firstLayoutName_loc)
            if searchre == nas:
                return True
            else:
                return False
        except:
            return False

    def edit_layout(self):
        self.driver.refresh()
        self.driver.implicitly_wait(60)
        time.sleep(3)
        try:
            self.layout.click(self.layout.refreshBtn_loc)
            time.sleep(1)
        except:
            log.info('Layouts列表刷新失败，等待3秒')
            time.sleep(3)
        else:
            # log.info('Layouts列表刷新成功')
            time.sleep(2)

        self.layout.send_keys(self.layout.searchInbox_loc, na)
        self.layout.click(self.layout.searchBt_loc)
        time.sleep(2)
        try:
            self.layout.click(self.layout.firstLayoutEdit_loc)
            time.sleep(2)
        except:
            log.info('点击编辑失败')
        else:
            log.info('开始编辑Layout')
            try:
                time.sleep(1)
                self.layout.send_keys(self.layout.layoutNameinbox_loc, editname)
                time.sleep(1)
            except:
                log.info('编辑Layout名称失败')
                return False
            else:
                self.layout.click(self.layout.saveExit_loc)
                time.sleep(3)
                log.info('编辑完成，待验证')
                return True


    def delLayout(self, name):
        self.driver.refresh()
        self.driver.implicitly_wait(60)
        time.sleep(3)
        try:
            self.layout.click(self.layout.refreshBtn_loc)
            time.sleep(1)
        except:
            log.info('Layouts列表刷新失败，等待3秒')
            time.sleep(3)
        else:
            # log.info('Layouts列表刷新成功')
            time.sleep(2)

        self.layout.send_keys(self.layout.searchInbox_loc, name)
        self.layout.click(self.layout.searchBt_loc)
        time.sleep(2)
        try:
            searchre = self.layout.get_text(self.layout.firstLayoutName_loc)
            if searchre == name:
                self.layout.click(self.layout.firstLayoutDel_loc)
                self.layout.click(self.layout.layoutDelOk_loc)
                time.sleep(1)
                return True
        except:
            log.info('没找到layout，删除操作失败')
            return False



    def test01_addLayout(self):
        '''测试新建Layout'''
        res = False
        if self.add_layout():
            res = self.searchLayout(nas=na)
            if res:
                log.info('新建Layout成功')
            else:
                log.info('新建Layout失败')
        self.assertTrue(res)

    @skip_dependon(depend='test01_addLayout')
    def test02_editLayout(self):
        '''测试编辑Layout'''
        if self.edit_layout():
            res = self.searchLayout(nas=editname)
            if res:
                log.info('编辑Layout成功')
            else:
                log.info('编辑Layout失败')
        else:
            res = False
        self.assertTrue(res)

    @skip_dependon(depend='test02_editLayout')
    def test03_delLayout(self):
        '''测试删除Layout'''
        res = True
        if self.delLayout(editname):
            res = self.searchLayout(nas=editname)
            if not res:
                log.info('删除Layout成功')
            else:
                log.info('删除Layout失败')
        self.assertFalse(res)

if __name__ == '__main__':
    unittest.main()
