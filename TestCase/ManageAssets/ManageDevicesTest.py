# -*-coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ManageDevicesTest.py
   Description :   测试设备管理的添加、编辑、发送Notes功能
   Author :        姜丽丽
-------------------------------------------------
"""

from Page.loginpage import LoginPage
from Page.ManageAssets.ManageDevicesPage import ManageDevicesPage
from Common.logger import Log
from Common.operater import browser
import unittest
import time
import os

log = Log()
path = '.\\report'

#判断报告目录是否存在
if not os.path.exists(path):
    os.mkdir(path)

current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
current_date = time.strftime('%m/%d/%Y')

deviceSN ='AutoTestSN'+current_time
deviceEsn ='AutoTestEsn'+current_time
addNotes = 'AutoTestNotes'+current_time
editNotes = deviceSN+'Edit'

class ManageDevicesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        log.info('--------开始测试Manage Device--------')
        cls.driver = browser()
        cls.login = LoginPage(cls.driver)
        cls.login.login('atdevice@iicon001.com','Win.12345')
        cls.driver.implicitly_wait(60)
        log.info('--------成功登录--------')
        time.sleep(5)
        cls.to_iframe(cls)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def to_iframe(self):
        self.device = ManageDevicesPage(self.driver)
        try:
            # self.device.click(self.device.manageAssetLink_loc)
            time.sleep(5)
            # self.device.click(self.device.manageDevices_loc)
            time.sleep(1)
            self.device.switch_to_iframe(self.device.iframe_loc)
            time.sleep(1)
        except:
            log.info('--------打开ManageDevices列表失败!--------')
        else:
            time.sleep(3)
            log.info('--------打开ManageDevices列表成功!--------')


    def save_device(self):
        try:
            while not self.device.is_clickable(self.device.addBtn_loc):
                log.info('添加按钮不可点击，等待3秒再看')
                time.sleep(3)
            self.device.click(self.device.addBtn_loc)
            self.device.switch_to_iframe(self.device.addDeviceIframe_loc)
            time.sleep(1)
        except:
            log.info('--------打开添加设备页面失败！--------')
        else:
            log.info('--------打开添加设备页面成功！开始输入信息--------')
            time.sleep(3)
            self.device.select_by_text(self.device.selectSource_loc,'Foresight Device (non-HOS)')
            self.device.send_keys(self.device.deviceId_loc,deviceSN)
            time.sleep(2)
            self.device.send_keys(self.device.deviceEsn_loc, deviceEsn)
            self.device.send_keys(self.device.deviceType_loc, 'AutoTest')
            self.device.send_keys(self.device.invoiceDate_loc, current_date)
            self.device.send_keys(self.device.invoiceNo_loc, current_time)
            self.device.send_keys(self.device.startDate_loc, current_date)
            self.device.send_keys(self.device.notes_loc, addNotes)
            try:
                self.device.click(self.device.saveBtn_loc)
                time.sleep(1)
                self.device.click(self.device.saveDialogOkBtn_loc)
                time.sleep(1)
            except:
                log.info('-----保存设备添加失败！-----')
            else:
                log.info('-----设备添加操作保存成功！是否添加成功待验证！-----')
                self.device.click(self.device.exitWithoutSavingBtn_loc)
                self.driver.switch_to.default_content()
                self.device.switch_to_iframe(self.device.iframe_loc)
                time.sleep(3)

    def verify_add_and_edit(self, SN, notes):
        self.device.search(SN)
        time.sleep(3)
        try:
            txt = self.device.get_text(self.device.searchNotes_loc)
        except:
            log.info('-----搜索目标Device失败！-----')
            return False
        else:
            if txt == notes:
                return True
            else:
                return False

    def edit_device(self):
        # self.device.search(SN)
        time.sleep(1)
        self.device.js_execute("window.scrollTo(0,300)")
        try:
            self.device.click(self.device.editDeviceBtn_loc)
            time.sleep(1)
            self.device.switch_to_iframe(self.device.addDeviceIframe_loc)
        except:
            log.info('-----打开Device编辑页面失败！----')
        else:
            self.device.send_keys(self.device.notes_loc, editNotes)
            try:
                self.device.click(self.device.saveBtn_loc)
                self.device.click(self.device.saveDialogOkBtn_loc)
            except:
                log.info('-----保存设备编辑失败!-----')
            else:
                log.info('-----设备编辑操作保存成功！是否添加成功待验证！-----')
                self.device.click(self.device.exitWithoutSavingBtn_loc)
                self.driver.switch_to.default_content()
                self.device.switch_to_iframe(self.device.iframe_loc)
                time.sleep(1)

    def send_notes(self, notes):
        # self.device.search(SN)
        time.sleep(1)
        self.device.js_execute("window.scrollTo(0,300)")
        time.sleep(2)
        try:
            self.device.click(self.device.notesBtn_loc)
            time.sleep(2)
            self.device.switch_to_iframe(self.device.addDeviceIframe_loc)
        except:
            log.info('-----打开Notes管理页面失败！----')
            return False
        else:
            log.info('Notes: %s' % notes)
            self.device.send_keys(self.device.notesText_loc, notes)
            try:
                self.device.click(self.device.sendNotesBtn_loc)
                time.sleep(1)
            except:
                log.info('-----发送Notes失败！-----')
                return False
            else:
                log.info('-----完成Notes发送操作，是否发送成功待验证！-----')
                time.sleep(3)
                try:
                    txt = self.device.get_text(self.device.sendedNotes_loc)
                    time.sleep(1)
                    log.info('搜索Notes： %s' % txt)
                except:
                    log.info('-----发送Notes失败！-----')
                    return False
                else:
                    self.device.click(self.device.exitWithoutSavingBtn_loc)
                    time.sleep(2)
                    self.driver.switch_to.default_content()
                    self.device.switch_to_iframe(self.device.iframe_loc)
                    time.sleep(1)
                    if txt == notes:
                        log.info('-----Notes发送成功！-----')
                        return True
                    else:
                        log.info('-----Notes发送失败！-----')
                        return False

    def test01_Add_Device(self):
        '''测试添加设备'''
        self.save_device()
        time.sleep(1)
        res = self.verify_add_and_edit(deviceSN, addNotes)
        if res:
            log.info('-----Device添加成功！----')
        else:
            log.info('-----Device添加失败！----')
        self.assertTrue(res)

    def test02_edit_device(self):
        '''测试编辑设备'''
        self.edit_device()
        res = self.verify_add_and_edit(deviceSN, editNotes)
        if res:
            log.info('-----Device编辑成功！----')
        else:
            log.info('-----Device编辑失败！----')
        self.assertTrue(res)

    def test03_send_notes(self):
        '''测试发送Notes'''
        res = self.send_notes(editNotes)
        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()





