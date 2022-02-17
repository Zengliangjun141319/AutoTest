# -*-coding: utf-8 -*-
"""
----------------------------------------------------------
   File Name：     InspectionsTest.py
   Description :   测试Inspections的编辑、查看Detail、下载、打印
   Author :        姜丽丽
----------------------------------------------------------
"""
from Page.loginpage import LoginPage
from Page.Inspection.InspectionsPage import InspectionsPage
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

class InspectionsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        log.info('--------测试用例开始--------')
        cls.driver = browser()
        cls.login = LoginPage(cls.driver)
        cls.login.login('autotest@dev.com', 'Win.12345')
        log.info('--------成功登录--------')
        cls.open_inspectionsMenu(cls)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def open_inspectionsMenu(self):
        self.inspection = InspectionsPage(self.driver)
        self.driver.implicitly_wait(60)
        try:
            self.inspection.click(self.inspection.inspection_loc)
            time.sleep(2)
            self.inspection.click(self.inspection.inspectionsMenu_loc)
        except:
            log.info('--------打开Inspections列表失败！--------')
            return False
        else:
            log.info('--------打开Inspections列表成功！--------')

    def is_have_records(self):
        try:
            table = self.driver.find_element_by_class_name('data-grid-body-content')
            recs = len(table.find_elements_by_tag_name('tr'))
        except:
            log.info('--------Inspections列表中无记录！--------')
            return False
        else:
            # log.info('有 %s 条记录' % recs)
            return True

    def edit_inspection(self):
        self.inspection.search()
        self.driver.implicitly_wait(60)
        time.sleep(3)
        res = self.is_have_records()
        if res:
            time.sleep(2)
            try:
                #  //*[@id="set_right"]/div/div[2]/div/div[1]/div/table/tbody/tr[1]/td[14]/a
                self.inspection.click(self.inspection.editBtn_loc)
            except:
                log.info('--------打开Inspections编辑页面失败！--------')
                return False
            else:
                time.sleep(3)    # 添加延时，等编辑页面加载完成
                self.inspection.click(self.inspection.saveBtn_loc)
                time.sleep(1)
                self.inspection.click(self.inspection.okBtn_loc)
                log.info('--------成功编辑Inspection！--------')
                self.inspection.click(self.inspection.exitBtn_loc)
                return True
        else:
            return False

    def check_detail(self):
        self.inspection.search()
        res = self.is_have_records()
        if res:
            self.inspection.js_execute("document.getElementById('right_popup').scrollLeft=1000")
            time.sleep(2)
            try:
                self.inspection.click(self.inspection.detailBtn_loc)
            except:
                log.info('--------点击Detail按钮失败！--------')
                return False
            else:
                self.driver.switch_to.window(self.driver.window_handles[1])
                try:
                    self.driver.find_element_by_id('button-edit')
                except:
                    log.info('--------打开Inspections Detail页面失败！--------')
                    return False
                else:
                    log.info('--------打开Inspections Detail页面成功！--------')
                    self.driver.close()
                    time.sleep(1)
                    self.driver.switch_to.window(self.driver.window_handles[0])
                    time.sleep(1)
                    return True
        else:
            return False

    def downloda_PDF(self):
        self.inspection.search()
        res = self.is_have_records()
        if res:
            self.inspection.js_execute("document.getElementById('right_popup').scrollLeft=1000")
            time.sleep(2)
            try:
                self.inspection.click(self.inspection.downloadBtn_loc)
                time.sleep(1)
            except:
                log.info('--------点击Download PDF按钮失败！--------')
                return False
            else:
                log.info('--------Download PDF成功！--------')
                return True
        else:
            return False

    def print_inspection(self):
        self.inspection.search()
        res = self.is_have_records()
        if res:
            self.inspection.js_execute("document.getElementById('right_popup').scrollLeft=1000")
            time.sleep(2)
            try:
                self.inspection.click(self.inspection.printBtn_loc)
            except:
                log.info('--------点击Print按钮失败！--------')
                return False
            else:
                # try:
                #     self.driver.switch_to.window(self.driver.window_handles[1])
                # except:
                #     log.info('--------打印Inspection失败！--------')
                #     return False
                log.info('--------打印Inspection成功！--------')
                return True
        else:
            return False

    def test01_edit_inspection(self):
        result = self.edit_inspection()
        self.assertTrue(result)

    def test02_check_detail(self):
        result = self.check_detail()
        self.assertTrue(result)

    def test03_downloda_PDF(self):
        result = self.downloda_PDF()
        self.assertTrue(result)

    def test04_print_inspection(self):
        result = self.print_inspection()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()





