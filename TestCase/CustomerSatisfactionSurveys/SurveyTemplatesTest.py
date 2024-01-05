# -*-coding: utf-8 -*-
"""
------------------------------------------------------------------
   File Name：     SurveyTemplatesTest.py
   Description :   测试Work Order Survey Templates的添加、编辑、删除
   Author :        姜丽丽
   change log:
    1、 增加Template复制和预览功能测试　---- 2022.12.29  zlj
------------------------------------------------------------------
"""
from Page.loginpage import LoginPage
from Page.CustomerSatisfactionSurveys.TemplatesPage import TemplatesPage
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

current_time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
templateName = 'AutoTest' + current_time
editTemplateName = templateName + 'Edit'
copyTemplateName = templateName + 'Copy'


class SurveyTemplatesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = browser()
        cls.login = LoginPage(cls.driver)
        cls.login.login('atsurvey@iicon004.com','Win.12345')
        log.info('--------开始测试Work Order Survey Templates功能--------')
        time.sleep(5)
        cls.template = TemplatesPage(cls.driver)
        cls.driver.implicitly_wait(60)
        log.info('--------成功登录--------')
        cls.open_templates(cls)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def open_templates(self):
        # 打开Templates页面
        time.sleep(3)
        while not self.template.is_clickable(self.template.surveyTemplates_loc):
            log.info('Template菜单不能点击，等待3秒重试')
            self.template.click(self.template.exButton_loc)
            time.sleep(3)
        while True:
            try:
                self.template.click(self.template.surveyTemplates_loc)
                time.sleep(1)
                self.template.click(self.template.exButton_loc)
            except:
                log.info('--------打开Work Order Survey Templates页面失败！--------')
                log.info('3秒后重试……')
                time.sleep(3)
            else:
                log.info('--------打开Work Order Survey Templates页面成功！--------')
                time.sleep(2)
                break

    def add_template(self):
        try:
            self.template.switch_to_iframe(self.template.iframe_loc)
            time.sleep(1)
            while not self.template.is_clickable(self.template.addBtn_loc):
                log.info('添加Template按钮不能点击，等待3秒重试')
                time.sleep(3)
            self.template.click(self.template.addBtn_loc)
        except:
            log.info('--------打开添加Templates页面失败！--------')
        else:
            log.info('--------打开添加Templates页面成功！开始输入信息--------')
            self.template.switch_to_iframe(self.template.addIframe_loc)
            time.sleep(1)
            self.template.inputTo(self.template.templateName_loc, templateName)
            try:
                for i in range(0,5):
                    self.template.click(self.template.addQuestion_loc)
                    time.sleep(1)

                # 输入第1个问题
                self.template.inputTo(self.template.qustion1Name_loc, 'question1')
                self.template.inputTo(self.template.qustion1Text_loc, 'test question1')
                self.template.select_by_index(self.template.qustion1Type_loc,0)
                time.sleep(1)

                # 输入第2个问题
                self.template.inputTo(self.template.qustion2Name_loc, 'question2')
                self.template.inputTo(self.template.qustion2Text_loc, 'test question2')
                self.template.select_by_index(self.template.qustion2Type_loc,1)
                time.sleep(1)

                # 输入第3个问题
                self.template.inputTo(self.template.qustion3Name_loc, 'question3')
                self.template.inputTo(self.template.qustion3Text_loc, 'test question3')
                self.template.select_by_index(self.template.qustion3Type_loc,2)
                time.sleep(1)

                # 输入第4个问题
                self.template.inputTo(self.template.qustion4Name_loc, 'question4')
                self.template.inputTo(self.template.qustion4Text_loc, 'test question4')
                self.template.select_by_index(self.template.qustion4Type_loc,3)
                time.sleep(1)

                # 输入第5个问题
                self.template.inputTo(self.template.qustion5Name_loc, 'question5')
                self.template.inputTo(self.template.qustion5Text_loc, 'test question5')
                self.template.select_by_index(self.template.qustion5Type_loc,4)
                time.sleep(1)
            except:
                log.info('--------添加Questions失败！--------')
            else:
                log.info('--------添加了5个Questions！--------')
                try:
                    time.sleep(1)
                    self.template.click(self.template.saveAndExitBtn_loc)
                    time.sleep(1)
                except:
                    log.info('-----保存Template失败！！-----')
                else:
                    log.info('-----完成保存操作，是否添加成功待验证！-----')

    def search_template(self, templateName):
        # 查询目标template是否存在
        time.sleep(1)
        self.template.search(templateName)
        time.sleep(3)
        # template = self.template.get_attribute(self.template.templateName_loc, "title")
        try:
            template = self.driver.find_element('xpath', '//*[@id="surveylist"]/div/div[1]/div/table/tbody/tr[1]/td[1]/span').text
            # template = target.get_attribute("text")
        except:
            return False
        else:
            if template == templateName:
                return True
            else:
                return False

    def verify_template(self, templateName):
        # 查询刚才创建的template是否存在
        self.driver.switch_to.default_content()
        self.template.switch_to_iframe(self.template.iframe_loc)
        time.sleep(1)
        self.template.search(templateName)
        time.sleep(2)
        try:
            template = self.driver.find_element('xpath', '//*[@id="surveylist"]/div/div[1]/div/table/tbody/tr[1]/td[1]/span').text
            # template = target.get_attribute("text")
        except:
            return False
        else:
            if template == templateName:
                return True
            else:
                return False

    def edit_template(self, templateName):
        res = self.search_template(templateName)
        if res:
            try:
                self.template.click(self.template.editBtn_loc)
                self.driver.implicitly_wait(60)
                time.sleep(2)
            except:
                log.info('-----打开Template编辑页面失败！----')
            else:
                time.sleep(3)
                self.template.switch_to_iframe(self.template.addIframe_loc)
                time.sleep(1)
                self.template.send_keys(self.template.templateName_loc, editTemplateName)
                time.sleep(1)
                self.template.click(self.template.saveAndExitBtn_loc)
                time.sleep(3)
                log.info('-----完成Template编辑操作！是否编辑成功待验证----')
        else:
            log.info('-----未找到待编辑的Template!----')

    def copy_template(self, templateName):
        rr = self.search_template(templateName)
        if rr:
            try:
                self.template.click(self.template.copytemplateBtn_loc)
                self.driver.implicitly_wait(60)
                time.sleep(2)
            except:
                log.info('------打开复制Template编辑页面失败!------')
            else:
                time.sleep(3)
                self.template.switch_to_iframe(self.template.addIframe_loc)
                time.sleep(1)
                self.template.send_keys(self.template.templateName_loc, copyTemplateName)
                time.sleep(1)
                self.template.click(self.template.saveAndExitBtn_loc)
                time.sleep(3)
                log.info('-----完成复制Template编辑操作！是否编辑成功待验证----')
        else:
            log.info('------未找到待复制的Template! ------')

    def preview_template(self, templateName):
        # 预览复制的Template
        try:
            self.template.click(self.template.previewtemplate_loc)
            self.driver.implicitly_wait(60)
            time.sleep(2)
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(2)
        except:
            log.info('预览Template失败')
            return False
        else:
            try:
                self.template.click(self.template.previewAdv_loc)
                time.sleep(1)
                self.template.click(self.template.previewLink_loc)
                time.sleep(3)
            except:
                log.info('链接不是HTTPS，可直接打开')
            title = self.template.get_text(self.template.previewTitle_loc)
            log.info('预览的Template名称是： %s' % title)
            time.sleep(2)
            # 跳回Template列表页
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.switch_to.default_content()
            time.sleep(2)
            self.template.switch_to_iframe(self.template.iframe_loc)
            time.sleep(1)
            if title == templateName:
                return True
            else:
                return False

    def delete_template(self, templateName):
        res = self.search_template(templateName)
        if res:
            try:
                self.template.click(self.template.deleteBtn_loc)
            except:
                log.info('-----打开Templates删除对话框失败！----')
            else:
                try:
                    self.template.click(self.template.deleteOKBtn_loc)
                    time.sleep(1)
                except:
                    self.driver.switch_to.default_content()
                    self.template.click(self.template.deleteOKBtn_loc)
                    time.sleep(1)
                    self.template.switch_to_iframe(self.template.iframe_loc)
                log.info('-----完成Template删除操作！是否删除成功待验证----')
        else:
            log.info('-----未找到待删除的Template!----')

    def test01_add_template(self):
        '''添加Template'''
        self.add_template()
        res = self.verify_template(templateName)
        if res:
            log.info('-----添加Template成功！----')
        else:
            log.info('-----添加Template失败！----')
        self.assertTrue(res)

    @skip_dependon(depend='test01_add_template')
    def test02_edit_template(self):
        '''编辑Template'''
        self.edit_template(templateName)
        res = self.verify_template(editTemplateName)
        if res:
            log.info('-----编辑Template成功！----')
        else:
            log.info('-----编辑Template失败！----')
        self.assertTrue(res)

    @skip_dependon(depend='test02_edit_template')
    def test03_copy_template(self):
        '''测试复制Template'''
        self.copy_template(editTemplateName)
        res = self.verify_template(copyTemplateName)
        if res:
            log.info('-----复制Template成功！-----')
        else:
            log.info('-----复制Template失败！-----')
        self.assertTrue(res)

    def test04_preview_template(self):
        '''测试预览Template功能'''
        res = self.preview_template(copyTemplateName)
        if res:
            log.info('------预览Template成功！-----')
        else:
            log.info('------预览Template失败！-----')
        self.assertTrue(res)

    @skip_dependon(depend='test03_copy_template')
    def test05_delete_template(self):
        '''删除Template'''
        self.delete_template(editTemplateName)
        time.sleep(1)
        self.delete_template(copyTemplateName)
        time.sleep(1)
        res1 = self.search_template(copyTemplateName)
        res2 = self.search_template(editTemplateName)
        res = res1 and res2
        if not res:
            log.info('-----删除Template成功！----')
        else:
            log.info('-----删除Template失败！----')
        self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()





