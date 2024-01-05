# coding:utf-8

from Page.loginpage import  browser
from Page.loginpage import LoginPage
import unittest
import os
from Page.TruckAlertConfigPage import TruckAlertPage
import time
from logger import Log
from excel import excel
import ddt
from skiptest import skip_dependon
import random

log = Log()
# 判断保存报告的目录是否存在
path = ".\\report"
isExists = os.path.exists(path)
if not isExists:
    os.mkdir(path)

file_path = ".\\TestData\\truckAlert.xls"
testdata = excel.get_list(file_path)
nowtime = time.strftime('%Y%m%d%H%M%S')

@ddt.ddt
class TruckAlertTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = browser("chromeH")
        cls.login = LoginPage(cls.driver)
        cls.login.login('attruck@iicon004.com', 'Win.12345')
        cls.truckalert = TruckAlertPage(cls.driver)
        cls.driver.implicitly_wait(5)
        time.sleep(5)
        log.info('开始测试TruckAlert管理...')


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def refresh(self):
        try:
            self.truckalert.click(self.truckalert.refreshbutton_loc)
        except:
            log.info('数据刷新失败，重新刷新页面')
            self.driver.refresh()
            self.driver.implicitly_wait(60)
            time.sleep(5)
        else:
            self.driver.implicitly_wait(60)
            time.sleep(5)

    @ddt.data(*testdata)
    def test01_addconfig(self, data):
        self.refresh()
        log.info('测试添加Jobsite Limit配置 -- %s' % data['casename'])
        time.sleep(2)
        self.truckalert.click(self.truckalert.addbutton_loc)
        self.truckalert.switch_to_iframe(self.truckalert.iframe_loc)
        time.sleep(3)
        self.truckalert.select_by_value(self.truckalert.jobsiteselect_loc, '17')
        self.truckalert.select_by_value(self.truckalert.starthour_loc, data['starthour'])
        self.truckalert.select_by_value(self.truckalert.startminute_loc, data['startminute'])
        self.truckalert.select_by_value(self.truckalert.endhour_loc, data['endhour'])
        self.truckalert.select_by_value(self.truckalert.endminute_loc, data['endminute'])
        self.truckalert.send_keys(self.truckalert.mintrucks_loc, data['minnum'])
        self.truckalert.send_keys(self.truckalert.maxtrucks_loc, data['maxnum'])
        self.truckalert.click(self.truckalert.assettype_loc)
        time.sleep(1)
        check1 = ('xpath', '//*[@id="dialog_assettype"]/div/div[2]/ul/li[%d]/input' % random.randint(1, 4))
        check2 = ('xpath', '//*[@id="dialog_assettype"]/div/div[2]/ul/li[%d]/input' % random.randint(5, 9))
        self.truckalert.click(check1)
        self.truckalert.click(check2)
        time.sleep(1)
        self.truckalert.send_keys(self.truckalert.notes_loc, "The content of notes created on " + nowtime)
        self.truckalert.click(self.truckalert.savebutton_loc)
        time.sleep(3)
        result = self.truckalert.get_text(self.truckalert.savemsg_loc)
        self.truckalert.click(self.truckalert.savemsgok_loc)
        self.truckalert.click(self.truckalert.withoutsavebutton_loc)
        self.driver.switch_to.default_content()
        if self.assertEqual(result, data['mess']):
            log.info("测试失败！！")
        else:
            log.info("测试成功！！")

    def search_config_and_subscribe(self):
        log.info('测试搜索添加的配置')
        time.sleep(2)
        self.truckalert.send_keys(self.truckalert.searchinput_loc, nowtime)
        self.truckalert.click(self.truckalert.searchbutton_loc)
        time.sleep(3)
        try:
            self.truckalert.click(self.truckalert.refreshbutton_loc)
            time.sleep(3)
        except:
            log.info('未找到添加的配置')
            return False
        else:
            log.info('准备添加联系人')
            try:
                self.truckalert.click(self.truckalert.subscribeBt_loc)
                self.driver.implicitly_wait(40)
                time.sleep(2)
            except:
                log.info('打开添加联系人界面失败')
                return False
            else:
                log.info('添加全部联系人')
                data = ('xpath', '//*[@id="availablecontacts"]/div/div[1]/div/table/tbody/tr[1]/td[1]')
                if not self.truckalert.is_visibility(data):
                    log.info('数据未加载完，等待3秒')
                    time.sleep(3)
                self.truckalert.click(self.truckalert.selectallBt_loc)
                time.sleep(2)
                self.truckalert.click(self.truckalert.subscribeOK_loc)
                time.sleep(3)
                return True

    def del_config(self):
        log.info('删除刚添加的配置')
        self.driver.implicitly_wait(40)
        time.sleep(1)
        try:
            self.truckalert.click(self.truckalert.refreshbutton_loc)
            time.sleep(3)
        except:
            log.info('页面未加载好，等待3秒')
            time.sleep(3)
        finally:
            time.sleep(2)
        try:
            self.truckalert.click(self.truckalert.delsearch_loc)
            time.sleep(1)
            self.truckalert.click(self.truckalert.delOk_loc)
            time.sleep(1)
        except:
            log.info('删除失败')
            return False
        else:
            time.sleep(3)
            log.info('删除成功')
            return True

    def test02_search_truck(self):
        '''测试搜索并指派联系人'''
        res = self.search_config_and_subscribe()
        if res:
            log.info('指派联系人成功')
        else:
            log.info('指派联系人失败')
        self.assertTrue(res)

    @skip_dependon(depend='test02_search_truck')
    def test03_del_truck(self):
        '''删除配置'''
        res = self.del_config()
        if res:
            log.info('删除Trucking Alerts Configure成功')
        else:
            log.info('删除Trucking Alerts Configure失败')
        self.assertTrue(res)


if __name__ == "__main__":
    unittest.main()
