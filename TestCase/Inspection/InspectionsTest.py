# -*-coding: utf-8 -*-
"""
----------------------------------------------------------
   File Name：     InspectionsTest.py
   Description :   测试Inspections的编辑、查看Detail、下载、打印
   Author :        姜丽丽
----------------------------------------------------------
    change Log:
        1、 增加16269 Fleet - Inspection can't assign Work Order功能测试    -- 2022.8.18  曾良均
"""
from Page.loginpage import LoginPage
from Page.Inapection.InspectionsPage import InspectionsPage
from logger import Log
from operater import browser
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
        cls.driver = browser()
        cls.login = LoginPage(cls.driver)
        cls.login.login('atins@iicon004.com', 'Win.12345')
        log.info('--------开始Inspection--------')
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
            self.inspection.click(self.inspection.exButton_loc)
            self.inspection.click(self.inspection.inspectionsMenu_loc)
        except:
            log.info('--------打开Inspections列表失败！--------')
            return False
        else:
            log.info('--------打开Inspections列表成功！--------')
            self.inspection.click(self.inspection.exButton_loc)

    def is_have_records(self):
        try:
            table = self.driver.find_element_by_class_name('data-grid-body-content')
            recs = len(table.find_elements_by_tag_name('tr'))
        except:
            log.info('--------Inspections列表中无记录！--------')
            return False
        else:
            log.info('有 %s 条记录' % recs)
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
                log.info('--------打印Inspection成功！--------')
                return True
        else:
            return False

    # 增加16269：Fleet - Inspection can't assign Work Order功能测试    ------ 2022.8.18 zlj
    def asignedWO(self):
        self.inspection.search()
        res = self.is_have_records()
        if res:
            log.info('按提交时间倒序排序')
            self.inspection.js_execute("document.getElementsByClassName('data-grid')[0].scrollLeft=1000")
            self.inspection.click(self.inspection.CommittimeCol_loc)
            time.sleep(1)
            self.inspection.click(self.inspection.CommittimeCol_loc)
            time.sleep(1)
            self.inspection.js_execute("document.getElementsByClassName('data-grid')[0].scrollLeft=0")
        log.info('测试指派Inspection给WO')
        if res:
            woidl = ('xpath', '//*[@id="set_right"]/div/div[2]/div/div[1]/div/table/tbody/tr[1]/td[4]/span/div/div/div[1]/label[1]')
            woid = self.inspection.get_attribute(woidl, 'textContent')
            log.info('当前Inspection指派的WO为： %s' % woid)
            dropd = self.driver.find_element_by_xpath('//*[@id="set_right"]/div/div[2]/div/div[1]/div/table/tbody/tr[1]/td[4]/span/div/div/div[1]/label[2]')
            dropd.click()
            try:
                self.driver.find_element_by_xpath('//*[@id="set_right"]/div/div[2]/div/div[1]/div/table/tbody/tr[1]/td[4]/span/div/div/div[2]/ul/li[last()]').click()
                time.sleep(1)
                self.driver.find_element_by_xpath('/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input[@value="Yes"]').click()
                time.sleep(1)
            except:
                log.info('选择WO列表失败')
                return False
            else:
                log.info('Assigned to WO 成功!')
                woidl = ('xpath',
                    '//*[@id="set_right"]/div/div[2]/div/div[1]/div/table/tbody/tr[1]/td[4]/span/div/div/div[1]/label[1]')

                woid1 = self.inspection.get_attribute(woidl, 'textContent')
                log.info('重新指派Inspection的WO为： %s' % woid1)
                return True
        else:
            log.info('没有Inspection')
            return False

    def test01_AssignedToWO(self):
        '''测试把Inspection指派给WO'''
        res = self.asignedWO()
        self.assertTrue(res)

    def test02_edit_inspection(self):
        '''测试编辑Inspection'''
        result = self.edit_inspection()
        self.assertTrue(result)

    def test03_check_detail(self):
        '''测试Insepction明细检查'''
        result = self.check_detail()
        self.assertTrue(result)

    def test04_downloda_PDF(self):
        '''测试下载Inspection'''
        result = self.downloda_PDF()
        self.assertTrue(result)

    def test05_print_inspection(self):
        '''测试打印Inspection'''
        result = self.print_inspection()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()





