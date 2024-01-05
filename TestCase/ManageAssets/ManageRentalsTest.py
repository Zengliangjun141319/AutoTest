# -*-coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ManageRentalsTest.py
   Description :   测试租赁管理的添加、删除、编辑功能
   Author :        姜丽丽
-------------------------------------------------
"""
from operater import browser
from Page.ManageAssets.ManageRentalsPage import ManageRentalsPage
from Page.loginpage import LoginPage
from logger import Log
import unittest
import time
import os
from skiptest import skip_dependon

log = Log()
# 判断报告目录是否存在
path = '.\\report'
if not os.path.exists(path):
    os.mkdir(path)

current_time = time.strftime('%H%M%S', time.localtime(time.time()))
current_date = time.strftime('%m/%d/%Y')
vendor = 'AutoTest' + current_time
editVendor = vendor+'Edit'


class ManageRentalsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = browser("chromeH")
        cls.login = LoginPage(cls.driver)
        cls.login.login('atrental@iicon006.com', 'Win.12345')
        log.info('----开始测试租赁管理----')
        cls.to_frame(cls)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def to_frame(self):
        log.info('----登录成功,打开到Manage Rentals页面----')
        try:
            times = 0
            while times < 3:
                self.rental = ManageRentalsPage(self.driver)
                # self.rental.click(self.rental.manageAssetLink_loc)
                # time.sleep(1)
                # self.rental.click(self.rental.manageRentals_loc)
                time.sleep(5)
                self.rental.switch_to_iframe(self.rental.iframe_loc)
                time.sleep(1)
                times += 1

                if self.rental.is_visibility(self.rental.addBtn_loc):
                    break
                else:
                    log.info('打开Rentals列表失败，第 %d 次重试' % times)
        except:
            log.info('--------打开ManageRentals列表失败！--------')
        else:
            log.info('--------打开ManageRentals列表成功！--------')

    def save_rental(self):
        try:
            self.rental.click(self.rental.addBtn_loc)
            self.rental.switch_to_iframe(self.rental.iframeRental_loc)
        except:
            log.info('--------打开添加租赁页面失败！！--------')
        else:
            log.info('--------打开添加租赁页面成功！开始输入信息--------')
            time.sleep(5)
            import random
            num = random.randint(1, 5)
            self.rental.select_by_index(self.rental.assetSelect_loc, num)
            self.asset = self.rental.get_text(self.rental.assetSelectOption_loc)
            self.rental.select_by_index(self.rental.outsideSelect_loc,1)
            self.rental.send_keys(self.rental.vendor_loc, vendor)
            self.rental.send_keys(self.rental.rate_loc, '10')
            self.rental.send_keys(self.rental.term_loc, '8')
            self.rental.select_by_text(self.rental.termUnit_loc, 'Weekly')
            self.rental.send_keys(self.rental.billingDate_loc,current_date)
            self.rental.send_keys(self.rental.billingCycleDays_loc,'6')
            self.rental.send_keys(self.rental.rentalDate_loc,current_date)
            self.rental.send_keys(self.rental.projectReturnDate_loc, current_date)
            self.rental.send_keys(self.rental.returnDate_loc, current_date)
            self.rental.send_keys(self.rental.poNumber_loc, 'AutoTest001')
            self.rental.send_keys(self.rental.insuredValue_loc, '1350')
            self.rental.send_keys(self.rental.comments_loc, 'AutoTest')
            try:
                self.rental.click(self.rental.saveBtn_loc)
                msg = self.rental.get_text(self.rental.saveDialog_loc)
                time.sleep(2)
                self.rental.click(self.rental.saveDialogOkBtn_loc)
            except:
                log.info('-----保存租赁失败！！-----')
            else:
                self.rental.click(self.rental.exitWithoutSavingBtn_loc)
                self.driver.switch_to.default_content()
                self.rental.switch_to_iframe(self.rental.iframe_loc)
                time.sleep(1)
                if msg == 'Saved successfully.':
                    return True
                else:
                    return False

    def edit_rental(self, vendor):
        time.sleep(3)
        self.rental.search(vendor)
        self.rental.js_execute('window.scrollTo(0,300)')
        # self.rental.js_execute("document.getElementById('rentallist').scrollLeft=1000")
        try:
            self.rental.click(self.rental.editBtn_loc)
            time.sleep(1)
            self.rental.switch_to_iframe(self.rental.iframeRental_loc)
        except:
            log.info('-----打开租赁编辑页面失败！！-----')
        else:
            time.sleep(5)
            self.rental.send_keys(self.rental.vendor_loc, editVendor)
            try:
                self.rental.click(self.rental.saveAndExitBtn_loc)
                time.sleep(2)
            except:
                log.info('-----编辑租赁时保存失败！！-----')
            else:
                time.sleep(3)
                self.driver.switch_to.default_content()
                self.rental.switch_to_iframe(self.rental.iframe_loc)

    def search_and_delete(self, asset):
        self.rental.search(asset)
        # self.rental.js_execute('window.scrollTo(0,300)')
        self.rental.js_execute("document.getElementById('rentallist').scrollLeft=2000")
        time.sleep(2)
        while True:
            try:
                self.rental.click(self.rental.deleteBtn_loc)
                time.sleep(1)
                try:
                    self.rental.click(self.rental.deleteDialogOkBtn_loc)
                except:
                    self.driver.switch_to.default_content()
                    self.rental.click(self.rental.deleteDialogOkBtn_loc)
                    time.sleep(1)
                    self.rental.switch_to_iframe(self.rental.iframe_loc)
            except:
                break
            else:
                log.info('------已执行删除操作，删除结果待验证！')

    def verify_add_and_edit(self, vendor):
        self.rental.search(vendor)
        time.sleep(1)
        try:
            txt = self.rental.get_text(self.rental.searchVendor_loc)
        except:
            log.info('-----未搜索到目标Rentals！-----')
            return False
        else:
            if txt == vendor:
                return True
            else:
                return False

    def test01_add_rental(self):
        '''添加租赁'''
        savRes = self.save_rental()
        if savRes:
            log.info('-----完成保存操作，是否添加成功待验证！-----')
            res = self.verify_add_and_edit(vendor)
            time.sleep(2)
            if res:
                log.info('-----添加Rental成功！----')
            else:
                log.info('-----添加Rental失败！----')
            self.assertTrue(res)
        else:
            log.info('-----保存租赁失败，删除已有记录后再执行添加操作！-----')
            self.search_and_delete(self.asset)
            time.sleep(2)
            savRes = self.save_rental()
            if savRes:
                log.info('-----完成保存操作，是否添加成功待验证！-----')
                res = self.verify_add_and_edit(vendor)
                time.sleep(2)
                if res:
                    log.info('-----添加Rental成功！----')
                else:
                    log.info('-----添加Rental失败！----')
                self.assertTrue(res)

    # 如果添加租赁失败，则跳过编辑租赁测试
    @skip_dependon(depend='test01_add_rental')
    def test02_edit_rental(self):
        '''编辑租赁'''
        self.edit_rental(vendor)
        res = self.verify_add_and_edit(editVendor)
        if res:
            log.info('-----编辑Rental成功！----')
        else:
            log.info('-----编辑Rental失败！----')
        self.assertTrue(res)

    # 如果编辑租赁失败，则跳过删除租赁测试
    @skip_dependon(depend='test02_edit_rental')
    def test03_delete_rental(self):
        '''删除租赁'''
        self.search_and_delete(editVendor)
        res = self.verify_add_and_edit(editVendor)
        if not res:
            log.info('-----删除Rental成功！----')
        else:
            log.info('-----删除Rental失败！----')
        self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()



