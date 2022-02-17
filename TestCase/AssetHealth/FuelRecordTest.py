# coding:utf-8

import time
from Common.operater import browser
from Page.loginpage import LoginPage
from Page.AssetHealth.FuelRecordPage import FuelRecordPage
import unittest
from Common.operater import Operater
import os
from Common.logger import Log
from Common.skiptest import skip_dependon

log = Log()


class FuelRecordTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = browser()
        cls.login = LoginPage(cls.driver)
        cls.login.login('atfuel@iicon004.com', 'Win.12345')
        cls.driver.implicitly_wait(60)
        log.info('-----开始测试Fuel Record管理')
        cls.switch_to_iframe(cls)


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def switch_to_iframe(self):
        self.fuel = FuelRecordPage(self.driver)
        # self.fuel.click(self.fuel.assethealth_loc)
        self.driver.implicitly_wait(60)
        time.sleep(10)
        # self.fuel.click(self.fuel.fuelmenu_loc)
        self.fuel.switch_to_iframe(self.fuel.iframe_loc)
        time.sleep(5)
        # self.search_and_delete(self)

    def search_and_delete(self):
        try:
            self.fuel.click(self.fuel.refreshB_loc)
            time.sleep(3)
        except:
            log.info('页面数据未加载完，等待3秒')
            time.sleep(3)
        finally:
            time.sleep(2)
        self.fuel.clear(self.fuel.begindate_loc)
        self.fuel.send_keys(self.fuel.begindate_loc, '10/13/2019')
        time.sleep(1)
        self.fuel.send_keys(self.fuel.searchinput_loc, '1T0310SLAHF306520')
        self.fuel.click(self.fuel.searchbutton_loc)
        log.info('搜索Fuel Record')
        while True:
            if self.fuel.pageload():
                time.sleep(1)
                break
            else:
                time.sleep(2)
                log.info("页面未加载完，继续等待...")
                continue
        time.sleep(3)
        self.fuel.js_execute('window.scrollTo(0, 300)')
        try:
            time.sleep(1)
            self.fuel.click(self.fuel.deletebutton_loc)
        except:
            log.info('没有数据可删除')
            return False
        else:
            self.fuel.click(self.fuel.checkdelete_loc)
            time.sleep(3)
            log.info('已删除')
            return True


    def addfuelrecord(self):
        crruntdate = time.strftime('%m%d%Y')
        while True:
            if self.fuel.pageload():
                time.sleep(1)
                break
            else:
                time.sleep(2)
                log.info("页面未加载完，继续等待...")
                continue
        try:
            self.fuel.click(self.fuel.refreshB_loc)
            time.sleep(3)
        except:
            log.info('页面数据未加载完，等待3秒')
            time.sleep(3)
        else:
            log.info('已刷新')
            time.sleep(2)
        finally:
            time.sleep(2)
        try:
            self.fuel.click(self.fuel.addbutton_loc)
            log.info('打开新建Fuel')
            self.fuel.switch_to_iframe(self.fuel.iframefuel_loc)
            time.sleep(5)
        except:
            log.info('click add failer')
        else:
            log.info('开始录入信息')
            self.fuel.click(self.fuel.assetddicon_loc)
            self.fuel.click(self.fuel.assetselect_loc)
            self.fuel.clear(self.fuel.transdate_loc)
            self.fuel.send_keys(self.fuel.transdate_loc, crruntdate)
            self.fuel.select_by_value(self.fuel.transtimehour_loc, '07')
            self.fuel.select_by_value(self.fuel.transtimeminute_loc, '17')
            self.fuel.send_keys(self.fuel.ticketnumber_loc, 'TN' + time.strftime('%Y%m%d%H%M%S'))
            self.fuel.send_keys(self.fuel.drivername_loc, 'Brandon Ingram')
            self.fuel.send_keys(self.fuel.retailername_loc, 'CostLine')
            self.fuel.send_keys(self.fuel.retaileraddress_loc, '24487, Williamsville, Virginia')
            self.fuel.send_keys(self.fuel.city_loc, 'LossAngel')
            self.fuel.click(self.fuel.stateddicon_loc)
            self.fuel.click(self.fuel.stateselect_loc)
            self.fuel.send_keys(self.fuel.zip_loc, 'ZIP000001')
            self.fuel.send_keys(self.fuel.odometer_loc, '1230')
            self.fuel.select_by_value(self.fuel.odometeruom_loc, 'mile')
            self.fuel.select_by_value(self.fuel.fueltype_loc, 'GRO')
            self.fuel.send_keys(self.fuel.brandname_loc, 'Shell')
            self.fuel.clear(self.fuel.measureunit_loc)
            self.fuel.send_keys(self.fuel.measureunit_loc, 'Gallon')
            self.fuel.send_keys(self.fuel.quantity_loc, '100')
            self.fuel.send_keys(self.fuel.unitcost_loc, '5.6')
            self.fuel.send_keys(self.fuel.notes_loc, 'This record is created on ' + crruntdate)


            self.fuel.click(self.fuel.addfilebutton_loc)
            log.info('添加附件')
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            # print(BASE_DIR)
            fpath = os.path.abspath(os.path.join(BASE_DIR, '..\..'))
            # print(fpath)
            time.sleep(3)
            imfile = os.path.join(fpath, 'upfile.exe')
            # print(imfile)
            file = os.path.join(fpath, 'TestData\\FuelRecordAttachment.docx')
            # print(file)
            os.system("%s %s" % (imfile, file))
            time.sleep(3)

            log.info('保存Fuel')
            self.fuel.click(self.fuel.savebutton_loc)  # //*[@id="content1"]/div[2]/div[1]/span[1]
            time.sleep(3)
            text = self.fuel.get_text(self.fuel.alertmsg_loc)
            self.fuel.click(self.fuel.alertokbutton_loc)
            self.fuel.click(self.fuel.exitwithoutsave_loc)
            self.driver.switch_to.default_content()
            time.sleep(1)
            self.fuel.switch_to_iframe(self.fuel.iframe_loc)
            time.sleep(1)
            return text

    def test01_add_fuelrecord(self):
        '''新建Fuel Record'''
        res = self.addfuelrecord()
        if self.assertEqual(res, 'Saved successfully.'):
            log.info('新增Fuel Record失败！')
        else:
            log.info('新增Fuel Record成功！')

    @skip_dependon(depend='test01_add_fuelrecord')
    def test02_del_fuelrecord(self):
        '''删除Fuel Record'''
        res = self.search_and_delete()
        if res:
            log.info('删除Fuel Record成功')
        else:
            log.info('删除Fuel Record失败')
        self.assertTrue(res)

if __name__ == '__main__':
    unittest.main()


