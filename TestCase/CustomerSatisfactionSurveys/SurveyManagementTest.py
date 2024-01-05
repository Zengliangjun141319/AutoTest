# -*-coding: utf-8 -*-
"""
------------------------------------------------------------------
   File Name：     SurveyManagementTest.py
   Description :   测试Survey报告的查看、下载、打印
   Author :        姜丽丽
   Change log:
    1、 增加搜索后结果呈现的等待处理 ------ 曾良均  2023.10.16
------------------------------------------------------------------
"""
from Page.loginpage import LoginPage
from Page.CustomerSatisfactionSurveys.SurveyManagementPage import SurveyManagementPage
from logger import Log
from operater import browser
import unittest
import time
import os
from skiptest import skip_dependon

log = Log()
path = '.\\report'

# 判断报告目录是否存在
if not os.path.exists(path):
    os.mkdir(path)


class SurveyManagementTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = browser("chromeH")
        cls.login = LoginPage(cls.driver)
        cls.login.login('atsurvey@iicon004.com', 'Win.12345')
        log.info('--------开始测试Survey Management/Result功能--------')
        time.sleep(5)
        log.info('--------成功登录--------')
        cls.survey = SurveyManagementPage(cls.driver)
        cls.driver.implicitly_wait(60)
        cls.open_survey(cls)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def open_survey(self):
        time.sleep(3)
        while not self.survey.is_clickable(self.survey.surveyManagement_loc):
            self.survey.click(self.survey.exButton_loc)
            time.sleep(3)
        while True:
            try:
                self.survey.click(self.survey.surveyManagement_loc)
                time.sleep(1)
                self.survey.click(self.survey.exButton_loc)
            except:
                log.info('--------打开Survey Management/Result页面失败！3秒后重试………………')
                time.sleep(3)
                continue
            else:
                self.survey.switch_to_iframe(self.survey.iframe_loc)
                time.sleep(1)
                log.info('--------打开Survey Management/Result页面成功！--------')
                break

    def is_have_records(self):
        self.survey.search()
        time.sleep(1)
        while True:
            try:
                self.survey.click(self.survey.search_Inbox)
                time.sleep(1)
            except:
                time.sleep(2)
                continue
            else:
                time.sleep(1)
                break
        table = self.driver.find_element_by_class_name('data-grid-body-content')
        table.find_elements_by_tag_name('tr')
        records = table.find_elements_by_tag_name('tr')
        rec = len(records)  # 此算法获取记录数不正确，但能判断有没有记录
        if rec == 0:
            return False
        else:
            # log.info('找到 %s 条记录' % rec)
            return True

    def view_survey(self):
        res = self.is_have_records()
        r = 0
        if res:
            # 过滤状态为Replied的调查报告
            try:
                self.survey.js_execute("window.scrollTo(0,0)")
                time.sleep(1)
                self.survey.click(self.survey.status_filter_btn)
                time.sleep(1)
            except:
                log.info('打开Status Filter失败')
            else:
                self.survey.send_keys(self.survey.status_input, 'Replied')
                time.sleep(1)
                self.survey.click(self.survey.status_filter_OK)
                time.sleep(2)

            table = self.driver.find_element_by_class_name('data-grid-body-content')
            rows = table.find_elements_by_tag_name('tr')
            rowNum = len(rows)
            for i in range(0, rowNum):
                row = rows[i]
                 # 直接查找Detail
                dets = row.find_elements_by_xpath('./td/a[@title="Detail"]')
                for det in dets:
                    if not det.get_attribute('style'):    # 判断是不是没有style属性
                        r += 1
                        try:
                            self.survey.js_execute("window.scrollTo(0,300)")
                            time.sleep(1)
                            det.click()
                        except:
                            return False
                        else:
                            time.sleep(1)
                            if self.survey.find_element(self.survey.surveyIframe_loc):
                                self.survey.switch_to_iframe(self.survey.surveyIframe_loc)
                                time.sleep(1)
                                self.survey.click(self.survey.closeSurveyIframe_loc)
                                return True
            if r == 0:
                log.info('----所有问卷都没完成调查，无法查看！----')
                return False
        else:
            log.info('----系统中没有任何问卷记录！----')
            return False

    def downLoadPDF_survey(self):
        self.driver.switch_to.default_content()
        self.survey.switch_to_iframe(self.survey.iframe_loc)
        r = 0
        table = self.driver.find_element_by_class_name('data-grid-body-content')
        rows = table.find_elements_by_tag_name('tr')
        rowNum = len(rows)
        for i in range(0, rowNum):
            row = rows[i]
                # 直接查找Download PDF
            dets = row.find_elements_by_xpath('./td/a[@title="Download PDF"]')
            for det in dets:
                if not det.get_attribute('style'):    # 判断是不是没有style属性
                    r += 1
                    try:
                        self.survey.js_execute("window.scrollTo(0,300)")
                        time.sleep(1)
                        det.click()
                    except:
                        return False
                    else:
                        return True
        if r == 0:
            log.info('----所有问卷都未完成调查，无法下载PDF！----')
            return False

    def print_survey(self):
        r = 0
        table = self.driver.find_element_by_class_name('data-grid-body-content')
        rows = table.find_elements_by_tag_name('tr')
        rowNum = len(rows)
        for i in range(0, rowNum):
            row = rows[i]
                # 直接查找Print
            dets = row.find_elements_by_xpath('./td/a[@title="Print"]')
            for det in dets:
                if not det.get_attribute('style'):    # 判断是不是没有style属性
                    r += 1
                    try:
                        self.survey.js_execute("window.scrollTo(0,300)")
                        time.sleep(1)
                        det.click()
                    except:
                        return False
                    else:
                        return True
        if r == 0:
            log.info('----所有问卷都未完成调查，无法打印！----')
            return False

    def test01_view_survey(self):
        '''查看survey'''
        res = self.view_survey()
        if res:
            log.info('-----查看survey成功！----')
        else:
            log.info('-----查看survey失败！----')
        self.assertTrue(res)

    @skip_dependon(depend='test01_view_survey')
    def test02_downLoadPDF_survey(self):
        '''下载survey'''
        res = self.downLoadPDF_survey()
        if res:
            log.info('-----下载survey成功！----')
        else:
            log.info('-----下载survey失败！----')
        self.assertTrue(res)

    @skip_dependon(depend='test02_downLoadPDF_survey')
    def test03_print_survey(self):
        '''编辑Template'''
        res = self.print_survey()
        if res:
            log.info('-----打印survey成功！----')
        else:
            log.info('-----打印survey失败！----')
        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()





