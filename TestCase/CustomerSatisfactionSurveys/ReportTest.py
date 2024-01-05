# -*-coding: utf-8 -*-
"""
------------------------------------------------------------------
   File Name：     SurveyManagementTest.py
   Description :   测试Survey的报表查看
   Author :        姜丽丽
   change log:
    1、 2022.12.29 增加发送Survey Report到邮件的测试
------------------------------------------------------------------
"""
from Page.loginpage import LoginPage
from Page.CustomerSatisfactionSurveys.ReportPage import ReportPage
from logger import Log
from operater import browser
import unittest
import time
import os
from skiptest import skip_dependon

log = Log()
path = '.\\report'

#判断报告目录是否存在
if not os.path.exists(path):
    os.mkdir(path)

class SurveyReportTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        log.info('--------开始测试Survey Report功能--------')
        cls.driver = browser()
        cls.login = LoginPage(cls.driver)
        cls.login.login('atsurvey@iicon004.com', 'Win.12345')
        time.sleep(5)
        log.info('--------成功登录--------')
        cls.report = ReportPage(cls.driver)
        cls.driver.implicitly_wait(60)
        time.sleep(5)
        # cls.open_survey(cls)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def open_survey(self):
        # 打开Templates页面
        time.sleep(3)
        self.report.click(self.report.exButton_loc)
        while not self.report.is_clickable(self.report.report_loc):
            log.info('Report菜单不能点击，等待3秒重试')
            self.report.click(self.report.exButton_loc)
            time.sleep(3)
        while True:
            try:
                self.report.click(self.report.report_loc)
                time.sleep(1)
                self.report.click(self.report.exButton_loc)
            except:
                log.info('--------打开Survey Report页面失败！3秒后重试………………')
                time.sleep(3)
            else:
                self.report.switch_to_iframe(self.report.iframe_loc)
                time.sleep(1)
                log.info('--------打开Survey Report页面成功！--------')
                break

    def is_have_templates(self):
        time.sleep(1)
        try:
            select = self.driver.find_element_by_class_name('selectinput')
            options = select.find_elements_by_tag_name('option')
            optNum = len(options)
        except:
            log.info('----未找到templates下拉列表----')
        else:
            if optNum == 1:
                return False
            else:
                return True

    def survey_report(self):
        self.open_survey()
        res = self.is_have_templates()
        if res:
            try:
                self.report.select_by_index(self.report.templatesList_loc, 1)
                time.sleep(1)
            except:
                log.info('----系统中没有可用的templates!----')
                return False
            else:
                return True

    def send_survey_report(self):
        # 根据查看的结果，把报告发送到邮件
        time.sleep(5)
        try:
            self.report.click(self.report.sendemailBtn_loc)
            time.sleep(2)
            self.report.send_keys(self.report.otheraddress_loc, 'zljun8210@live.cn')
            self.report.click(self.report.sendSurveyRepOK_loc)
        except:
            log.info('send survey report Failed')
            return False
        else:
            time.sleep(1)
            txt = self.report.get_text(self.report.sendresult_loc)
            self.report.click(self.report.sendresultOK_loc)
            if txt == 'Message sent.':
                return True
            else:
                return False

    def test01_survey_report(self):
        '''查看survey报表'''
        res = self.survey_report()
        if res:
            log.info('-----查看survey报表成功！----')
        else:
            log.info('-----查看survey报表失败！----')
        self.assertTrue(res)

    @skip_dependon(depend='test01_survey_report')
    def test02_send_survey_report(self):
        '''测试发送Survey Report到邮件'''
        res = self.send_survey_report()
        if res:
            log.info('-----发送Survey Report到邮件成功！-----')
        else:
            log.info('-----发送Survey Report到邮件失败！-----')
        self.assertTrue(res)

if __name__ == '__main__':
    unittest.main()