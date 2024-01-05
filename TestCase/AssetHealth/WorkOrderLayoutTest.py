# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     WorkOrderLayoutTest.py
   Author :        曾良均
   QQ:             277099728
   Date：          4/19/2023 5:25 PM   
   Description :
    Layout测试包含：
        1、 编辑保存Layout：与公司同名、已存在、为空、正确保存
        2、 新建保存为公共
        3、 Save保存为个人私有
        4、 管理Layout:删除创建的公共、私有
-------------------------------------------------
   Change Activity:
                   
-------------------------------------------------
"""
__author__ = 'ljzeng'

import unittest
from Page.loginpage import LoginPage
from Page.AssetHealth.WorkOrderPage import WorkOrderPage
from logger import Log
from operater import browser
import os, time
from excel import excel
import ddt

log = Log()
path = '.\\report'

if not os.path.exists(path):
    os.mkdir(path)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file_path = ".\\TestData\\workorderlayout.xlsx"
testData = excel.get_list(file_path)


@ddt.ddt
class WorkOrderLayoutTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = browser("chromeH")  # 无头模式下有的测试不通过
        cls.login = LoginPage(cls.driver)
        cls.login.login('autotestwo@iicon001.com', 'Win.12345')
        cls.driver.implicitly_wait(60)
        log.info('开始测试Work Order Layout功能------')
        cls.switchto_iframe(cls)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def switchto_iframe(self):
        self.workorder = WorkOrderPage(self.driver)
        self.driver.implicitly_wait(50)
        time.sleep(5)
        self.workorder.switch_to_iframe(self.workorder.iframe_loc)  # 切换到work order列表iframe
        time.sleep(1)

    def updatelayout(self):
        # update layout
        try:
            self.workorder.click(self.workorder.refreshbutton_loc)
            time.sleep(2)
        except:
            self.driver.refresh()
            self.driver.implicitly_wait(60)
            time.sleep(5)
            self.workorder.switch_to_iframe(self.workorder.iframe_loc)
        log.info('Start test update layout')

        self.workorder.click(self.workorder.layout_loc)
        self.workorder.click(self.workorder.uplayout_loc)
        try:
            self.workorder.click(self.workorder.selectAllChx_loc)  # 全选所有字段
            self.workorder.send_keys(self.workorder.firstlayoutcolumnCapInbox_loc, 'WorkOrder#')
            self.workorder.click(self.workorder.layoutOK_loc)
        except:
            log.info('打开Layout设置失败')
            return False
        else:
            time.sleep(1)
            self.workorder.send_keys(self.workorder.savelayoutname_loc, "AutoTest")  # input name
            if not self.driver.find_element_by_id('chkPublic').is_selected():
                self.workorder.click(self.workorder.makePubChx_loc)  # check Make Public
            self.workorder.click(self.workorder.savelayoutbtn_loc)
            try:
                self.workorder.click(self.workorder.saveoverwriteYes_loc)
                time.sleep(3)
                log.info('Save操作已完成，待验证')
            except:
                log.info('没有同名的Layout')
            return self.verifylayout("AutoTest")

    def managelayout(self):
        try:
            self.workorder.click(self.workorder.refreshbutton_loc)
            time.sleep(2)
        except:
            self.driver.refresh()
            self.driver.implicitly_wait(60)
            time.sleep(5)
            self.workorder.switch_to_iframe(self.workorder.iframe_loc)
        self.workorder.click(self.workorder.layout_loc)
        self.workorder.click(self.workorder.managelayout_loc)
        time.sleep(1)
        # 管理界面查找添加的Layout，并删除
        layoutspath = self.driver.find_element_by_xpath('//*[@id="dialog_managelayout"]/div[2]/div[4]')
        layouts = layoutspath.find_elements_by_xpath('./div')
        for layout in layouts:
            name = layout.find_element_by_xpath('span').text
            # log.info('Layout name: %s' % name)
            if name == 'AutoTest':
                layout.find_element_by_xpath('span[@class="sbutton icondelete"]').click()
                self.workorder.click(self.workorder.dellayoutYesBtn_loc)
                time.sleep(1)
                self.workorder.click(self.workorder.managelayoutOKBtn_loc)  # 点击OK关闭Manage Layout窗口
                return True
        else:
            self.workorder.click(self.workorder.managelayoutOKBtn_loc)  # 点击OK关闭Manage Layout窗口
            return False

    def verifylayout(self, layoutname):
        time.sleep(1)
        self.workorder.click(self.workorder.refreshbutton_loc)
        time.sleep(2)
        log.info('Start verify layout ')

        self.workorder.click(self.workorder.layout_loc)
        time.sleep(3)
        layoutlist = self.driver.find_element_by_xpath('//*[@id="layout_panel_holder"]/div/ul')
        names = layoutlist.find_elements_by_xpath('./li')
        for name in names:
            nn = name.text
            log.info('Name have: %s' % nn)
            if nn == layoutname:
                log.info('已找到Layout: %s' % layoutname)
                self.workorder.click(self.workorder.layout_loc)
                return True
        else:
            log.info('没找到layout: %s' % layoutname)
            self.workorder.click(self.workorder.layout_loc)
            return False

    @ddt.data(*testData)
    def test01_savelayout(self, data):
        '''测试保存Layout功能'''
        self.workorder.click(self.workorder.refreshbutton_loc)
        time.sleep(2)

        log.info("Start test save layout - %s" % data['casename'])
        self.workorder.click(self.workorder.layout_loc)
        self.workorder.click(self.workorder.savelayout_loc)
        time.sleep(1)

        if data['casename'] == "saved":
            self.workorder.send_keys(self.workorder.savelayoutname_loc, data['name'])
            if self.driver.find_element_by_id('chkMyDefault').is_selected():
                self.workorder.click(self.workorder.saveAsMyDefChx_loc)  # 取消勾选为默认
            if not self.driver.find_element_by_id('chkPublic').is_selected():
                self.workorder.click(self.workorder.makePubChx_loc)
            if self.driver.find_element_by_id('chkCompanyDefault').is_selected():
                self.workorder.click(self.workorder.saveCompChx_loc)
            self.workorder.click(self.workorder.savelayoutbtn_loc)
            time.sleep(3)

            return self.verifylayout(data['name'])
        elif data['casename'] == 'Layout exists':
            self.workorder.send_keys(self.workorder.savelayoutname_loc, data['name'])
            self.workorder.click(self.workorder.savelayoutbtn_loc)
            time.sleep(1)
            try:
                message = self.workorder.get_text(self.workorder.savemessage_loc)
                self.workorder.click(self.workorder.saveoverwriteNo_loc)
            except:
                self.driver.switch_to.default_content()
                message = self.workorder.get_text(self.workorder.savemessage_loc)
                self.workorder.click(self.workorder.saveoverwriteNo_loc)
                self.workorder.switch_to_iframe(self.workorder.iframe_loc)

            self.workorder.click(self.workorder.savelayoutCancel_loc)
            result = (message == data['mess'])
            return result
        else:
            self.workorder.send_keys(self.workorder.savelayoutname_loc, data['name'])
            self.workorder.click(self.workorder.savelayoutbtn_loc)
            time.sleep(1)
            try:
                message = self.workorder.get_text(self.workorder.savemessage_loc)
                self.workorder.click(self.workorder.saveOKBtn_loc)
            except:
                self.driver.switch_to.default_content()
                message = self.workorder.get_text(self.workorder.savemessage_loc)
                self.workorder.click(self.workorder.saveOKBtn_loc)
                self.workorder.switch_to_iframe(self.workorder.iframe_loc)
            self.workorder.click(self.workorder.savelayoutCancel_loc)
            result = (message == data['mess'])
            return result

    def test02_updatelayout(self):
        '''测试update Layout'''
        res = self.updatelayout()
        log.info('获取修改后的列名')
        self.workorder.click(self.workorder.refreshbutton_loc)
        time.sleep(2)
        colname = '//*[@id="workorderlist"]/div/table/tr/th[1]/div[1]/span'
        firstcolumn = self.driver.find_element_by_xpath(colname).text
        log.info('Column name: %s' % firstcolumn)
        ver = (firstcolumn == 'WorkOrder#')  # 验证列名是否修改成功
        re = res and ver
        if re:
            log.info('update layout 测试成功')
        else:
            log.info('update layout测试失败')
        self.assertTrue(re)

    def test03_delLayout(self):
        '''测试删除Layout'''
        if self.managelayout():
            res = self.verifylayout("AutoTest")
            if not res:
                log.info('Manage Layout测试成功')
            else:
                log.info('Manage Layout测试失败')
            self.assertFalse(res)
        else:
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
