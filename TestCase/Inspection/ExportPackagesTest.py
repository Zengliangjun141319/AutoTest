# -*-coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ExportPackagesTest.py
   Description :   测试Inspection包的导出
   Author :        姜丽丽
-------------------------------------------------
"""
from Page.loginpage import LoginPage
from Page.Inspection.ExportPackagesPage import ExportPackagesPage
from Common.logger import Log
from Common.operater import browser
import pymssql
import unittest
import time
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Common.skiptest import skip_dependon

log = Log()
path = '.\\report'

#判断报告目录是否存在
if not os.path.exists(path):
    os.mkdir(path)

current_time = time.strftime('%H%M%S',time.localtime(time.time()))
packageName = 'AutoTest001'+current_time

class ExportPackagesTest(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        log.info('--------测试导出Inspection包--------')
        self.driver = browser()
        self.login = LoginPage(self.driver)
        self.login.login('autotest@foresight.com','Win.12345')
        self.driver.implicitly_wait(60)
        log.info('--------成功登录--------')

    def open_contractor(self):
        self.package = ExportPackagesPage(self.driver)
        try:
            self.package.click(self.package.customers_loc)
            self.package.send_keys(self.package.searchinput_loc,'006')
            time.sleep(1)
            self.package.click(self.package.searchBtn_loc)
            time.sleep(2)
            self.package.click(self.package.openBtn_loc)
        except:
            log.info('--------打开contractor站点失败！--------')
        else:
            # 跳转到Contractor页面
            self.driver.switch_to.window(self.driver.window_handles[1])
            log.info('--------打开contractor站点成功！--------')

    def open_export_packages(self):
        # time.sleep(10)
        self.driver.implicitly_wait(60)
        try:
            self.package.click(self.package.inspection_loc)
            time.sleep(2)
            self.package.click(self.package.exportPackages_loc)
        except:
            log.info('--------打开Export Packages菜单失败！--------')
        else:
            log.info('--------打开Export Packages菜单成功！--------')

    def create_package(self):
        try:
            time.sleep(1)
            self.package.click(self.package.createBtn_loc)
        except:
            log.info('--------打开创建包页面失败！--------')
        else:
            log.info('--------打开创建包页面成功！开始输入信息--------')
            time.sleep(2)
            self.package.inputTo(self.package.name_loc,packageName)
            self.package.inputTo(self.package.password_loc, '123456')
            self.package.inputTo(self.package.confirmPassword_loc, '123456')
            self.package.inputTo(self.package.notes_loc,'Auto Test')

            while not self.package.is_clickable(self.package.tempplateCheckbox1_loc):
                log.info('Template数据未加载，等待3秒重试')
                time.sleep(3)
            self.package.click(self.package.templatesTab_loc)
            self.package.click(self.package.tempplateCheckbox1_loc)
            self.package.click(self.package.tempplateCheckbox2_loc)

            self.package.click(self.package.globalSectionsTab_loc)
            while not self.package.is_clickable(self.package.globalSectionsCheckbox1_loc):
                log.info('Global数据未加载完成，等待3秒重试')
                time.sleep(3)
            self.package.click(self.package.globalSectionsCheckbox1_loc)
            self.package.click(self.package.globalSectionsCheckbox2_loc)

    def save_package(self):
        try:
            self.package.click(self.package.saveBtn_loc)
            time.sleep(1)
            self.msg = self.package.get_text(self.package.saveMessage_loc)
            self.package.click(self.package.okBtn_loc)
        except:
            log.info('-----保存package失败！！-----')
        else:
            log.info('-----完成保存操作，是否导出成功待验证！-----')

    def search_and_find(self):
        # 搜索并遍历table查找刚才创建的机器组是否存在
        time.sleep(2)
        table = self.driver.find_element_by_class_name('data-grid-body-content')
        time.sleep(2)
        rows = table.find_elements_by_tag_name('tr')
        rowNum = len(rows)
        res = False
        for i in range(0, rowNum):
            row = rows[i]
            cols = row.find_elements_by_tag_name('td')
            colNum = len(cols)
            for j in range(0, colNum):
                txt = cols[j].text
                if txt == packageName:
                    res = True
                    break
        return res

    def search_and_del(self):
        time.sleep(2)
        table = self.driver.find_element_by_class_name('data-grid-body-content')
        time.sleep(2)
        rows = table.find_elements_by_tag_name('tr')
        rowNum = len(rows)
        res = False
        for i in range(0, rowNum):
            row = rows[i]
            txt = row.find_element_by_xpath('./td[1]').text
            if txt == packageName:
                try:
                    row.find_element_by_xpath('./td[6]/a').click()
                    time.sleep(2)
                except:
                    log.info('点击 删除 按钮失败')
                    res = False
                else:
                    yesB ='/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input[2]'
                    self.driver.find_element_by_xpath(yesB).click()
                    time.sleep(1)
                    res = True

        return res

    @classmethod
    def tearDownClass(self) -> None:
        self.driver.quit()

    def test01_create_package_Success(self):
        '''测试创建及导出包'''
        self.open_contractor()
        self.open_export_packages()
        self.create_package()
        self.save_package()
        res = self.search_and_find()
        if res:
            log.info('-----导出包成功！----')
        else:
            log.info('-----导出包失败！----')
        self.assertTrue(res)

    @skip_dependon(depend='test01_create_package_Success')
    def test02_delete_package(self):
        '''删除测试创建的包'''
        res = self.search_and_del()
        self.assertTrue(res)

if __name__ == '__main__':
    unittest.main()





