# -*-coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     GlobalSectionsTest.py
   Description :   测试Global Sections的添加
   Author :        姜丽丽
-------------------------------------------------
"""
from Page.loginpage import LoginPage
from Page.Inapection.GlobalSectionsPage import GlobalSectionsPage
from logger import Log
from operater import browser
import pymssql
import unittest
import time
import os
from skiptest import skip_dependon

log = Log()
path = '.\\report'

#判断报告目录是否存在
if not os.path.exists(path):
    os.mkdir(path)

current_time = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))


class GlobalSectionsTest(unittest.TestCase):
    login = None
    driver = None

    @classmethod
    def setUpClass(self) -> None:
        self.driver = browser()
        self.login = LoginPage(self.driver)
        self.login.login('autotest@iicon006.com', 'Win.12345')
        log.info('--------开始测试Inspection Global Section--------')
        self.driver.implicitly_wait(60)
        log.info('--------成功登录--------')
        if not self.open_globalSections(self):
            self.driver.quit()
            quit()

    def open_globalSections(self):
        self.section = GlobalSectionsPage(self.driver)
        try:
            self.section.click(self.section.inspection_loc)
            self.section.click(self.section.exButton_loc)
            self.section.click(self.section.globalSections_loc)
        except:
            log.info('--------打开Global Sections列表失败！--------')
            return False
        else:
            log.info('--------打开Global Sections列表成功！--------')
            self.section.click(self.section.exButton_loc)
            return True

    def input_globalSection_information(self):
        try:
            self.section.click(self.section.addBtn_loc)
            time.sleep(2)
        except:
            log.info('--------打开添加Global Section页面失败！--------')
            return False
        else:
            log.info('--------打开添加Global Section页面成功！开始输入信息--------')
            self.section.inputTo(self.section.name_loc, current_time)
            self.section.inputTo(self.section.displayText_loc,'Auto Test Global Sections')
            self.section.inputTo(self.section.notes, 'Test Global Sections')
            return True

    def save_globalSection(self):
        try:
            self.section.click(self.section.saveBtn_loc)
            self.msg = self.section.get_text(self.section.saveMessage_loc)
            self.section.click(self.section.okBtn_loc)
            self.section.click(self.section.exitWithoutSavingBtn_loc)
        except:
            log.info('-----保存Global Sections失败！-----')
            return False
        else:
            log.info('-----完成保存操作！-----')
            res = (self.msg == 'Saved successfully.')
            return res

    def del_global_Section(self):
        # 先循环取得所有Section名称，把名称与目标名称对比，如果正确，则删除
        log.info('查找并删除新建的Global Section')
        lists = self.driver.find_elements_by_xpath('//*[@id="set_right"]/div/div[3]/div')
        for ls in lists:
            secname = ls.find_element_by_xpath('./div/div/div[@class="section-cell section-name"]/input').get_attribute('value')
            # log.info('Section: %s' % secname)
            if secname == current_time:
                ls.find_element_by_xpath('./div/div/div[@class="section-cell section-func"]/em[@title="Delete Section"]').click()
                time.sleep(1)
                self.driver.find_element_by_xpath('/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input[@value="Yes"]').click()
                time.sleep(2)
                return True
        else:
            return False

    @classmethod
    def tearDownClass(self) -> None:
        self.driver.quit()

    def test01_add_inspect_global_sections(self):
        """测试添加Global Section"""
        res = False

        if self.input_globalSection_information():
            res = self.save_globalSection()

        if res:
            log.info('-----成功添加Global Sections！-----')
        else:
            log.info('添加Global Sections失败！ ')
        self.assertTrue(res)

    @skip_dependon(depend='test01_add_inspect_global_sections')
    def test02_del_inspect_global_section(self):
        """测试删除Global Section"""
        time.sleep(3)
        res = self.del_global_Section()
        if res:
            log.info('删除Global Section： %s 成功' % current_time)
        else:
            log.info('删除Global失败')
        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()





