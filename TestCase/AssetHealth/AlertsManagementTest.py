# -*-coding: utf-8 -*-
"""
-------------------------------------------------------------------------------------------------------------------------
   File Name：    AlertsManagementTest.py
   Description :   测试AlertsManagement的Aacknowledge Alert、Create Work Order、查看Asset View列表、查看Aacknowledged Alerts列表
   Author :        姜丽丽

   Change Log:
        1、 新建WO保存时增加弹出提示
-------------------------------------------------------------------------------------------------------------------------
"""
from Page.loginpage import LoginPage
from Page.AssetHealth.AlertsManagementPage import AlertsManagementPage
from logger import Log
from operater import browser
import unittest
import time
import os

log = Log()
path = '.\\report'

# 判断报告目录是否存在
if not os.path.exists(path):
    os.mkdir(path)

# current_time = time.strftime('%H%M%S')
# planName = 'AutoTest'+current_time


# noinspection PyTypeChecker
class AlertsManagementTest(unittest.TestCase):
    login = None
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = browser()
        cls.login = LoginPage(cls.driver)
        cls.login.login('atalert@iicon004.com', 'Win.12345')
        log.info('--------开始测试Alerts Management--------')
        cls.driver.implicitly_wait(60)
        log.info('--------成功登录--------')
        cls.to_frame(cls)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def to_frame(self):
        self.alert = AlertsManagementPage(self.driver)
        self.driver.implicitly_wait(60)
        time.sleep(5)
        self.alert.switch_to_iframe(self.alert.iframe_loc)
        time.sleep(3)

    def is_have_records(self):
        try:
            time.sleep(5)
            self.alert.clear(self.alert.beginDate_loc)
            time.sleep(1)
            self.alert.click(self.alert.searchBtn_loc)
            time.sleep(3)

            # 增加按WO ID升序排序
            while True:
                try:
                    self.alert.click(self.alert.woid_loc)
                    time.sleep(1)
                    log.info('已升序显示')
                    break
                except:
                    log.info('排序操作失败，等待3秒重试')
                    time.sleep(3)

            table = self.driver.find_element_by_class_name('data-grid-body-content')
        except:
            log.info('--------Alerts Management列表中无记录！--------')
            return False
        else:
            elements = table.find_elements_by_tag_name('label')  # 元素位置更新
            for element in elements:
                at = element.get_attribute('style')
                if not at:
                    element.click()
                    return True
            log.info('--------Alerts Management列表中没有可以Acknowledge的记录！--------')
            return False

    def acknowledge_alert(self):
        res = self.is_have_records()
        if res:
            try:
                time.sleep(1)
                self.alert.click(self.alert.acknowledgeAlertBtn_loc)
            except:
                log.info('--------点击Acknowledge Alert(s)按钮失败！--------')
                return False
            else:
                try:
                    self.alert.send_keys(self.alert.acknowledgeAlerComment_loc,'AutoTest')
                    time.sleep(1)
                    self.alert.click(self.alert.acknowledgeAlerOKBtn_loc)
                except:
                    log.info('--------Acknowledge Alert(s)失败！--------')
                    return False
                else:
                    log.info('--------Acknowledge Alert(s)成功！--------')
                    return True
        else:
            return False

    def create_work_order(self):
        time.sleep(3)
        try:
            self.alert.click(self.alert.alertViewTab_loc)
            time.sleep(2)
            self.alert.click(self.alert.createWorkOrderBtn_loc)
        except:
            log.info('--------点击Create Work Order按钮失败！--------')
            return False
        else:
            try:
                self.alert.switch_to_iframe(self.alert.workOrderIframe_loc)
                time.sleep(1)
                self.alert.click(self.alert.selectAsset_loc)
            except:
                log.info('--------打开机器选择页面失败！--------')
                return False
            else:
                try:
                    time.sleep(5)
                    a = time.strftime('%S')[1]
                    log.info('----- 选择机器 ')
                    si = ('xpath', '//*[@id="dialog_machines"]/div[2]/div[1]/input')
                    sb = ('xpath', '//*[@id="dialog_machines"]/div[2]/div[1]/div')
                    self.alert.send_keys(si, a)
                    self.alert.click(sb)
                    time.sleep(5)
                    self.alert.click(self.alert.firstAsset_loc)
                    time.sleep(1)
                    self.alert.click(self.alert.selectAssetOKBtn_loc)
                except:
                    log.info('--------选择机器失败！--------')
                    return False
                else:
                    try:
                        time.sleep(2)
                        # self.alert.click(self.alert.desc_not_empty_ok_loc)
                        # time.sleep(1)
                        self.alert.send_keys(self.alert.workOrderDescription_loc, 'AutoTest')
                        self.alert.click(self.alert.saveBtn_loc)
                        # self.alert.click(self.alert.skip_loc)
                        time.sleep(1)
                        # 729版本增加弹出提示
                        self.alert.click(self.alert.saveStatusChange_loc)
                        time.sleep(1)

                        times = 1
                        msg = None
                        while times <= 3:
                            try:
                                msg = self.alert.get_text(self.alert.saveDialog_loc)
                            except:
                                log.info('第 %s 次未取到保存结果' % times)
                                time.sleep(2)
                                times += 1
                            else:
                                log.info(msg)
                                self.alert.click(self.alert.saveDialogOkBtn_loc)
                                time.sleep(5)
                                break

                        # time.sleep(5)
                        # msg = self.alert.get_text(self.alert.saveDialog_loc)
                        # self.alert.click(self.alert.saveDialogOkBtn_loc)
                        time.sleep(2)
                        ts = 1
                        while ts <= 3:
                            try:
                                self.alert.click(self.alert.exitWithoutSavingBtn_loc)
                            except:
                                log.info('第 %s 次不保存退出失败' % ts)
                                ts += 1
                                time.sleep(2)
                            else:
                                self.driver.implicitly_wait(60)
                                time.sleep(1)
                                break
                        # self.alert.click(self.alert.exitWithoutSavingBtn_loc)
                        time.sleep(2)
                    except:
                        log.info('--------保存Work Order失败！--------')
                        return False
                    else:
                        if msg == 'Saved successfully.':
                            log.info('--------Create Work Order成功！--------')
                            return True
                        else:
                            log.info('--------Create Work Order失败！--------')
                            return False

    def asset_view(self):
        time.sleep(5)
        try:
            self.alert.click(self.alert.assetViewTab_loc)
        except:
            log.info('--------打开Asset View Tab页失败！--------')
            return False
        else:
            time.sleep(5)
            self.alert.click(self.alert.expandAll_loc)
            txt = self.alert.get_text(self.alert.expandAll_loc)
            if txt == 'Collapse All':
                log.info('--------在Asset View Tab页Expand All成功！--------')
                return True
            else:
                log.info('--------在Asset View Tab页Expand All失败！--------')
                return False

    def acknowledged_alerts(self):
        time.sleep(2)
        try:
            self.alert.click(self.alert.acknowledgedAlerstab_loc)
        except:
            log.info('--------打开Acknowledged Alers Tab页失败！--------')
            return False
        else:
            try:
                self.alert.find_element(self.alert.acknowledgedBy_loc)
            except:
                log.info('--------打开Acknowledged Alers列表失败！--------')
                return False
            else:
                log.info('--------打开Acknowledged Alers列表成功！--------')
                return True

    def test01_acknowledge_alert(self):
        res = self.acknowledge_alert()
        self.assertTrue(res)

    def test02_asset_view(self):
        res = self.asset_view()
        self.assertTrue(res)

    def test03_acknowledged_alers(self):
        res = self.acknowledged_alerts()
        self.assertTrue(res)

    def test04_create_work_order(self):
        res = self.create_work_order()
        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()





