# -*-coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ManageDevicesTest.py
   Description :   测试设备管理的添加、编辑、发送Notes功能
   Author :        姜丽丽
   修改记录：
        1、 修改新建设备为参数化，实现所有类型的设备添加    ------ zlj 2022.7.12
-------------------------------------------------
"""

from Page.loginpage import LoginPage
from Page.ManageAssets.ManageDevicesPage import ManageDevicesPage
from logger import Log
from operater import browser
import unittest
import time
from queryMSSQL import delSQL
import os
from excel import excel
from ddt import *
from skiptest import skip_dependon

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

file_path = "TestData\managedevice.xlsx"
testData = excel.get_list(file_path)


@ddt
class ManageDevicesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = browser()
        cls.login = LoginPage(cls.driver)
        cls.login.login('atdevice@iicon001.com', 'Win.12345')
        log.info('--------开始测试Manage Device--------')
        cls.driver.implicitly_wait(60)
        log.info('--------成功登录--------')
        cls.clearTestData(cls)
        time.sleep(5)
        cls.to_iframe(cls)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.clearTestData(cls)
        cls.driver.quit()

    def clearTestData(self):
        log.info('从数据库删除测试数据')
        dta = 'ironintel_admin'
        dtm = 'IICON_001_FLVMST'
        sqlstr = "delete from GPSDEVICES where CONTRACTORID='IICON_001' and Notes like '%AutoTest%'"
        sqls = "delete from COMMENTS where COMMENTS like '%AutoTest%'"
        delSQL(dta, sqlstr)
        delSQL(dtm, sqls)

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

    def save_device(self, data):
        current_time1 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        current_date1 = time.strftime('%m/%d/%Y')
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
            log.info('----测试：  %s' % data['casename'])
            # log.info('--------打开添加设备页面成功！开始输入信息--------')
            time.sleep(3)
            self.device.select_by_text(self.device.selectSource_loc, data['source'])
            time.sleep(2)
            if data['source'] == 'Foresight ATU':
                self.device.select_by_text(self.device.seldeviceType_loc, data['type'])
            else:
                self.device.send_keys(self.device.deviceType_loc, data['type'])

            self.device.send_keys(self.device.deviceId_loc, data['sn'])
            time.sleep(2)
            # if data['sn'] == 'TFDnonHos001':  # 此类数据有ESN
            #     time.sleep(2)
            #     self.device.clear(self.device.deviceEsn_loc)
            #     self.device.send_keys(self.device.deviceEsn_loc, data['esn'])

            self.device.send_keys(self.device.invoiceDate_loc, current_date1)
            self.device.send_keys(self.device.invoiceNo_loc, current_time1)
            self.device.send_keys(self.device.startDate_loc, current_date1)
            self.device.send_keys(self.device.notes_loc, 'AutoTestNotes' + current_time1)
            try:
                self.device.click(self.device.saveBtn_loc)
                time.sleep(1)
                mess = self.device.get_text(self.device.savemessage_loc)
                time.sleep(1)
                self.device.click(self.device.saveDialogOkBtn_loc)
                time.sleep(1)
                res = (mess == data['mess'])
            except:
                log.info('-----保存设备添加失败！-----')
                res = False
            else:
                self.device.click(self.device.exitWithoutSavingBtn_loc)
                # self.device.click(self.device.saveAndExitBtn_loc)
                time.sleep(3)
                # log.info('-----设备添加操作保存成功！是否添加成功待验证！-----')
                self.driver.switch_to.default_content()
                self.device.switch_to_iframe(self.device.iframe_loc)
                time.sleep(3)
            return res

    def edit_device(self):
        self.device.search('TFDnonHos001')
        time.sleep(1)
        self.device.js_execute("window.scrollTo(0,300)")
        try:
            self.device.click(self.device.editDeviceBtn_loc)
            time.sleep(1)
            self.device.switch_to_iframe(self.device.addDeviceIframe_loc)
        except:
            log.info('-----打开Device编辑页面失败！----')
            res = False
        else:
            self.device.send_keys(self.device.notes_loc, editNotes)
            try:
                self.device.click(self.device.saveBtn_loc)
                time.sleep(1)
                mess = self.device.get_text(self.device.savemessage_loc)
                time.sleep(1)
                res = (mess == 'Saved successfully.')
                self.device.click(self.device.saveDialogOkBtn_loc)
            except:
                log.info('-----保存设备编辑失败!-----')
                res = False
            else:
                self.device.click(self.device.exitWithoutSavingBtn_loc)
                self.driver.switch_to.default_content()
                self.device.switch_to_iframe(self.device.iframe_loc)
                time.sleep(1)
        return res

    def pair_asset(self):
        self.device.search('TFDnonHos001')
        time.sleep(1)
        self.device.js_execute("window.scrollTo(0,300)")
        try:
            self.device.click(self.device.editDeviceBtn_loc)
            time.sleep(1)
            self.device.switch_to_iframe(self.device.addDeviceIframe_loc)
        except:
            log.info('-----打开Device编辑页面失败！----')
        else:
            self.device.click(self.device.selectAssetBtn_loc)
            time.sleep(10)
            while True:
                try:
                    self.device.click(self.device.firstAsset_loc)
                    time.sleep(1)
                except:
                    log.info('机器列表还没有加载出来，等3秒再试')
                    time.sleep(3)
                else:
                    log.info('选择显示的第一台机器')
                    self.device.click(self.device.selectAssetOK_loc)
                    time.sleep(2)
                    break
            pairvin = self.device.get_text(self.device.selVin_loc)
            log.info('已配对： %s ，结果待验证' % pairvin)
            self.device.click(self.device.saveAndExitBtn_loc)
            time.sleep(3)
            self.driver.switch_to.default_content()
            self.device.switch_to_iframe(self.device.iframe_loc)
            time.sleep(1)
            return pairvin

    def unpairAsset(self):
        self.device.search('TFDnonHos001')
        time.sleep(1)
        self.device.js_execute("window.scrollTo(0,300)")
        try:
            self.device.click(self.device.editDeviceBtn_loc)
            time.sleep(1)
            self.device.switch_to_iframe(self.device.addDeviceIframe_loc)
        except:
            log.info('-----打开Device编辑页面失败！----')
        else:
            self.device.click(self.device.unpairBtn_loc)
            time.sleep(2)
            log.info('已取消配对，结果待验证')
            self.device.click(self.device.saveAndExitBtn_loc)
            time.sleep(3)
            self.driver.switch_to.default_content()
            self.device.switch_to_iframe(self.device.iframe_loc)
            time.sleep(1)

    def ver_pair(self, vin):
        while True:
            try:
                self.device.click(self.device.refreshBtn_loc)
                time.sleep(2)
            except:
                log.info('数据未加载完成，3秒后重试')
                time.sleep(3)
            else:
                log.info('数据已刷新')
                time.sleep(2)
                break

        self.device.search('TFDnonHos001')
        time.sleep(1)
        # self.device.js_execute("document.getElementsByClassName('data-grid')[0].scrollLeft=10")
        try:
            listofvin = self.device.get_text(self.device.listsVin_loc)
            log.info('列表上配对的机器是： %s' % listofvin)
        except:
            listofvin = ''
        finally:
            res = (listofvin == vin)
            return res

    def send_notes(self, notes):
        self.device.search('TFDnonHos001')
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

    def exportToExcel(self):
        # Export to excel
        try:
            self.device.click(self.device.refreshBtn_loc)
            time.sleep(3)
        except:
            log.info('数据未加载完，等待3秒')
            time.sleep(3)
        finally:
            # 重置搜索框
            self.device.clear(self.device.searchInbox_loc)
            self.device.click(self.device.searchBtn_loc)
            time.sleep(2)

        grids = self.driver.find_element_by_xpath('//*[@id="devicelist"]/div/div[1]/div')
        hei = grids.size["height"]
        counts = int(hei) / 27
        log.info('当前有 %d 条数据' % counts)
        try:
            self.device.click(self.device.exExcelBtn_loc)
            time.sleep(10)
            # 判断下载的文件是否存在
            import pathlib
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            fpath = os.path.abspath(os.path.join(BASE_DIR, '..\..'))
            exfile = os.path.join(fpath, r'.\report\Manage+Devices.xlsx')
            exportfile = pathlib.Path(exfile)
            log.info('下载文件： %s' % exportfile)
            if exportfile.exists():
                # 调用读取数据
                from excel import excel
                datas = excel.get_rows(exportfile)
                # 有效数据须减去第1行（标题行）
                datas = datas - 1
                # 下载的文件不删除，便于后续验证
                # os.system('del %s' % exportfile)
                if datas == counts:
                    log.info('导出Device数据到Excel正确')
                    return True
                else:
                    log.info('导出后数据不正确')
                    return False
            else:
                log.info('导出文件不存在')
                return False
        except:
            log.info('导出失败')
            return False

    @data(*testData)
    def test01_Add_Device(self, data):
        '''测试添加设备'''
        res = self.save_device(data)
        time.sleep(1)
        if res:
            log.info('-----添加Device，测试成功！----')
        else:
            log.info('-----添加Device，测试失败！----')
        self.assertTrue(res)

    def test02_edit_device(self):
        '''测试编辑设备'''
        res = self.edit_device()
        if res:
            log.info('-----编辑Device，测试成功！----')
        else:
            log.info('-----编辑Device，测试失败！----')
        self.assertTrue(res)

    @skip_dependon(depend='test02_edit_device')
    def test03_send_notes(self):
        '''测试发送Notes'''
        res = self.send_notes(editNotes)
        self.assertTrue(res)

    @skip_dependon(depend='test02_edit_device')
    def test04_pairasset(self):
        '''测试配对机器'''
        vins = self.pair_asset()
        res = self.ver_pair(vins)
        if res:
            log.info('机器配对，测试成功')
        else:
            log.info('机器配对，测试失败')
        self.assertTrue(res)

    @skip_dependon(depend='test02_edit_device')
    def test05_upair(self):
        '''取消配对'''
        vins = ''
        self.unpairAsset()
        res = self.ver_pair(vins)
        if res:
            log.info('取消配对，测试成功')
        else:
            log.info('取消配对，测试失败')
        self.assertTrue(res)

    def test06_export(self):
        '''测试导出Device数据'''
        res = self.exportToExcel()
        if res:
            log.info('导出Device功能，测试成功')
        else:
            log.info('导出Device功能，测试失败')
        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()





