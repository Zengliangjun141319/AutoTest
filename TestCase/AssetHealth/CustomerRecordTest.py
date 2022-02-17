# coding: utf-8

import time
from Common.operater import browser
from Page.loginpage import LoginPage
import unittest
from Page.AssetHealth.CustomerRecordPage import CustomerRecordPage
from Common.logger import Log

log = Log()
ct = time.strftime("%H%M%S")
ctname = 'Customer' + ct

class CustomerRecordTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = browser()
        cls.login = LoginPage(cls.driver)
        cls.login.login('autocustmer@iicon004.com', 'Win.12345')
        cls.driver.implicitly_wait(60)
        log.info('开始测试Customer Record')
        time.sleep(5)
        cls.customer = CustomerRecordPage(cls.driver)
        cls.open_manage_customer(cls)


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


    def open_manage_customer(self):
        time.sleep(5)
        self.customer.switch_to_iframe(self.customer.iframe_loc)
        time.sleep(2)

    def add_customer(self):
        try:
            self.customer.click(self.customer.addbutton_loc)
        except:
            log.info("-----打开Customer新增窗口失败-----")
        else:
            log.info("-----打开Customer新增窗口成功-----")
            time.sleep(3)
            self.customer.switch_to_iframe(self.customer.iframecustomer_loc)
            self.customer.send_keys(self.customer.codeinput_loc, ctname)
            self.customer.send_keys(self.customer.companyname_loc, ctname)
            self.customer.send_keys(self.customer.addressinput_loc, "No.327 ZhongShanRoad.  YuZhong district ChongQing")
            self.customer.send_keys(self.customer.notesinput_loc, "notes content of customer" + ' ' + "SearchTest")
            self.customer.click(self.customer.savebutton_loc)
            time.sleep(2)
            self.customer.click(self.customer.savemsgok_loc)
            time.sleep(3)
            res = self.add_contact()
            self.customer.click(self.customer.savebutton_loc)
            txt = self.customer.get_text(self.customer.savemsg_loc)
            result = (txt == "Saved successfully.")
            self.customer.click(self.customer.savemsgok_loc)
            self.customer.click(self.customer.withoutsaveexit_loc)
            time.sleep(2)
            self.driver.switch_to.default_content()
            return result and res


    def delete_customer(self):
        log.info('删除新添加的Customer')
        try:
            self.customer.click(self.customer.refreshbutton_loc)
        except:
            log.info('页面元素不能点击，刷新页面')
            self.driver.refresh()
            self.driver.implicitly_wait(60)
            time.sleep(5)
            self.customer.switch_to_iframe(self.customer.iframe_loc)
            time.sleep(1)
        else:
            time.sleep(3)
        self.customer.clear(self.customer.searchinput_loc)
        self.customer.send_keys(self.customer.searchinput_loc, ctname)
        self.customer.click(self.customer.searchbutton_loc)
        time.sleep(3)
        # while True:
        try:
            self.customer.click(self.customer.deletecustomer_loc)
            time.sleep(1)
            self.customer.click(self.customer.deletecustomeryes_loc)
            time.sleep(1)
        except:
            # log.info("-----查询不到该Customer-----")
            return False
        else:
            return True
            # log.info("-----删除该Customer-----")




    def search_customer(self, words):
        log.info("-----开始查询-----")
        self.customer.switch_to_iframe(self.customer.iframe_loc)
        self.customer.clear(self.customer.searchinput_loc)
        self.customer.send_keys(self.customer.searchinput_loc, words)
        self.customer.click(self.customer.searchbutton_loc)
        time.sleep(2)
        txt = self.customer.get_text(self.customer.searchresult_loc)
        # self.driver.switch_to.default_content()
        # time.sleep(1)
        # self.customer.switch_to_iframe(self.customer.iframe_loc)
        res = (txt == ctname)
        return res


    def add_contact(self):
        currenttime1 = time.strftime("%Y%m%d%H%M%S")
        try:
            while not self.customer.is_clickable(self.customer.contactaddbutton_loc):
                log.info('添加Contact按钮不可点击，等待3秒重试')
                time.sleep(3)
            self.customer.click(self.customer.contactaddbutton_loc)
        except:
            log.info("-----打开Contact新增窗口失败-----")
            return False
        else:
            log.info("-----打开Contact新增窗口成功-----")
            time.sleep(3)
            self.customer.send_keys(self.customer.contactname_loc, "Code" + currenttime1)
            self.customer.select_by_text(self.customer.preference_loc, "Email")
            self.customer.send_keys(self.customer.emailaddress_loc, "Code" + currenttime1 + "@" + "hotmail.com")
            self.customer.send_keys(self.customer.contactnotes_loc, "Code" + currenttime1 + "'s note.")
            self.customer.click(self.customer.contactokbutton_loc)
            time.sleep(3)
            return True


    def assign_asset(self):
        log.info("-----为Customer分配机器-----")
        try:
            self.customer.click(self.customer.assignedasset_loc)
            time.sleep(2)
        except:
            log.info('没有数据')
            return False
        else:
            self.customer.click(self.customer.addassetbutton_loc)
            # 检查数据是否加载完
            time.sleep(3)
            while not self.customer.is_visibility(self.customer.assetcheckbutton_loc):
                log.info('机器数据未加载完，等待3秒再重试！')
                time.sleep(3)
            self.customer.send_keys(self.customer.searchassetinput_loc, '01X06771')
            self.customer.click(self.customer.searchassetbutton_loc)
            time.sleep(2)
            while True:
                if self.customer.pageload():
                    time.sleep(1)
                    break
                else:
                    time.sleep(2)
                    log.info("页面未加载完，继续等待...")
                    continue
            self.customer.click(self.customer.assetcheckbutton_loc)
            self.customer.click(self.customer.assetokbutton_loc)
            txt = self.customer.get_text(self.customer.firstasset_loc)
            res = (txt == '01X06771')
            self.customer.click(self.customer.closebutton_loc)
            self.driver.switch_to.default_content()
            self.customer.switch_to_iframe(self.customer.iframe_loc)
            time.sleep(2)
            return res




    def test01_add_customer(self):
        '''测试新建Customer'''
        res = self.add_customer()
        if res:
            log.info("新增Customer成功！")
        else:
            log.info("新增Customer失败！")

    def test02_search_customer(self):
        '''测试搜索新建的Customer'''
        result1 = self.search_customer(ctname)
        if result1:
            log.info("查询成功！")
        else:
            log.info("查询失败！")
        self.assertTrue(result1)

    def test03_assignasset(self):
        '''测试为Customer分配机器'''
        res = self.assign_asset()
        if res:
            log.info("分配机器成功！")
        else:
            log.info("分配机器失败")
        self.assertTrue(res)

    def test04_delete_Customer(self):
        '''测试删除Customer'''
        time.sleep(2)
        res = self.delete_customer()
        self.assertTrue(res)


if __name__ == "__main__":
    unittest.main()


