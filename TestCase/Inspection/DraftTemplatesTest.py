# -*-coding: utf-8 -*-
"""
------------------------------------------------------------------
   File Name：     DrafTemplatestTest.py
   Description :   测试Draft类型Templates的添加、编辑、发布、复制、删除
   Author :        姜丽丽
------------------------------------------------------------------
"""
from Page.loginpage import LoginPage
from Page.Inspection.DraftTemplatesPage import DraftTemplatesPage
from Common.logger import Log
from Common.operater import browser
import unittest
import time
import os
from Common.skiptest import skip_dependon

log = Log()
path = '.\\report'

#判断报告目录是否存在
if not os.path.exists(path):
    os.mkdir(path)

current_time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
templateName = 'AutoTest'+current_time
editTemplateName = templateName+'Edit'
copyTemplateName = editTemplateName+'Copy'


class DrafTemplatesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        log.info('--------开始测试Inspection Templates功能--------')
        cls.driver = browser()
        cls.login = LoginPage(cls.driver)
        cls.login.login('atdraf@iicon006.com','Win.12345')
        time.sleep(5)
        log.info('--------成功登录--------')
        cls.template = DraftTemplatesPage(cls.driver)
        cls.driver.implicitly_wait(60)
        cls.open_templates(cls)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def open_templates(self):
        # 打开Templates页面
        try:
            log.info('打开Draft Templates页面')
            time.sleep(5)
            self.template.click(self.template.templates_loc)
            time.sleep(3)
            while not self.template.is_clickable(self.template.addBtn_loc):
                log.info('添加Template按钮不能点击，等待3秒重试')
                time.sleep(3)
        except:
            log.info('--------打开Templates列表失败！--------')
        else:
            log.info('--------打开Templates列表成功！--------')
            time.sleep(2)

    def add_template(self):
        try:
            self.template.click(self.template.addBtn_loc)
        except:
            log.info('--------打开添加Templates页面失败！--------')
        else:
            log.info('--------打开添加Templates页面成功！开始输入信息--------')
            self.template.inputTo(self.template.templateName_loc, templateName)
            self.template.click(self.template.locationEnabled_loc)
            self.template.click(self.template.signatureRequired_loc)
            # self.template.click(self.template.locked_loc)
            self.template.inputTo(self.template.notes, 'template test')
            try:
                self.template.click(self.template.addPage_loc)
                # self.template.js_execute("window.scrollTo(0,200)")
                time.sleep(1)
                self.template.js_execute("document.getElementById('right_popup').scrollTop=1000")
                time.sleep(2)
                self.template.inputTo(self.template.pageName_loc, current_time)
                self.template.inputTo(self.template.pageText_loc, 'test page')
            except:
                log.info('--------添加Page失败！--------')
            else:
                log.info('--------添加Page成功！--------')
                try:
                    self.template.click(self.template.addSection_loc)
                    self.template.inputTo(self.template.sectionName_loc, current_time)
                    self.template.inputTo(self.template.sectionText_loc, 'test section')
                except:
                    log.info('--------添加Section失败！--------')
                else:
                    log.info('--------添加Section成功！--------')
                # self.template.js_execute("window.scrollTo(0,300)")
                    try:
                        self.template.js_execute("document.getElementById('right_popup').scrollLeft=1000")
                        time.sleep(1)
                        for i in range(0,5):
                            self.template.click(self.template.addQuestion_loc)
                            time.sleep(1)
                        self.template.js_execute("document.getElementById('right_popup').scrollLeft=0")
                        time.sleep(1)
                        self.template.js_execute("document.getElementById('right_popup').scrollTop=1000")
                        time.sleep(1)

                        #输入第1个问题
                        self.template.inputTo(self.template.qustion1Name_loc, 'question1')
                        self.template.inputTo(self.template.qustion1Text_loc, 'test question1')
                        self.template.select_by_index(self.template.qustion1Type_loc,0)
                        time.sleep(1)

                        #输入第2个问题
                        self.template.inputTo(self.template.qustion2Name_loc, 'question2')
                        self.template.inputTo(self.template.qustion2Text_loc, 'test question2')
                        self.template.select_by_index(self.template.qustion2Type_loc,6)
                        time.sleep(1)

                        #输入第3个问题
                        self.template.inputTo(self.template.qustion3Name_loc, 'question3')
                        self.template.inputTo(self.template.qustion3Text_loc, 'test question3')
                        self.template.select_by_index(self.template.qustion3Type_loc,7)
                        time.sleep(1)

                        #输入第4个问题
                        self.template.inputTo(self.template.qustion4Name_loc, 'question4')
                        self.template.inputTo(self.template.qustion4Text_loc, 'test question4')
                        self.template.select_by_index(self.template.qustion4Type_loc,15)
                        time.sleep(1)

                        #输入第5个问题
                        self.template.inputTo(self.template.qustion5Name_loc, 'question5')
                        self.template.inputTo(self.template.qustion5Text_loc, 'test question5')
                        self.template.select_by_index(self.template.qustion5Type_loc,18)
                        time.sleep(1)
                    except:
                        log.info('--------添加了Questions失败！--------')
                    else:
                        log.info('--------添加了5个Questions！--------')
                        try:
                            self.template.js_execute("document.getElementById('right_popup').scrollTop=0")
                            # self.template.js_execute("window.scrollTo(0,200)")
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
            self.driver.find_element('xpath', '//*[@id="set_right"]/div/div[3]/div[1]/div[2]/span')
        except:
            return False
        else:
            return True

    def verify_template(self, templateName):
        # 查询刚才创建的template是否存在
        self.template.search(templateName)
        time.sleep(2)
        try:
            target = self.driver.find_element('xpath', '//*[@id="set_right"]/div/div[3]/div[1]/div[2]/span')
            template = target.get_attribute("title")
        except:
            return False
        else:
            if template == templateName:
                return True
            else:
                return False

    def edit_template(self, templateName):
        res = self.search_template(templateName)
        if res == True:
            try:
                self.template.click(self.template.editBtn_loc)
                self.driver.implicitly_wait(60)
                time.sleep(2)
            except:
                log.info('-----打开Template编辑页面失败！----')
            else:
                time.sleep(3)
                self.template.send_keys(self.template.templateName_loc, editTemplateName)
                time.sleep(1)
                self.template.click(self.template.saveAndExitBtn_loc)
                time.sleep(3)
                log.info('-----完成Template编辑操作！是否编辑成功待验证----')
        else:
            log.info('-----未找到待编辑的Template!----')

    def copy_template(self, templateName):
        res = self.search_template(templateName)
        if res == True:
            try:
                self.template.click(self.template.copyBtn_loc)
            except:
                log.info('-----打开Template拷贝对话框失败！----')
            else:
                self.template.send_keys(self.template.copyTemplateName_loc, copyTemplateName)
                time.sleep(1)
                self.template.click(self.template.copyOKBtn_loc)
                time.sleep(2)
                log.info('-----完成Template拷贝操作！是否拷贝成功待验证----')
        else:
            log.info('-----未找到待拷贝的Template!----')

    def delete_template(self, templateName):
        res = self.search_template(templateName)
        if res == True:
            try:
                self.template.click(self.template.deleteBtn_loc)
            except:
                log.info('-----打开Templates删除对话框失败！----')
            else:
                time.sleep(1)
                self.template.click(self.template.deleteOKBtn_loc)
                time.sleep(1)
                log.info('-----完成Template删除操作！是否删除成功待验证----')
        else:
            log.info('-----未找到待删除的Template!----')

    def publish_template(self, templateName):
        res = self.search_template(templateName)
        if res == True:
            try:
                self.template.click(self.template.publishBtn_loc)
            except:
                log.info('-----打开Templates发布对话框失败！----')
            else:
                time.sleep(1)
                self.template.click(self.template.publsihOKBtn_loc)
                time.sleep(1)
                log.info('-----完成Template发布操作！是否发布成功待验证----')
        else:
            log.info('-----未找到待发布的Template!----')

    def ver_publish_and_del(self, templateName):
        try:
            # 点击 Published
            self.template.click(self.template.publish_menu_loc)
            time.sleep(3)
        except:
            log.info('Published列表未打开')
            return False
        else:
            # 搜索
            self.template.search(templateName)
            # //*[@id="set_right"]/div/div[3]/div[1]/div[2]/span
            try:
                self.driver.find_element('xpath', '//*[@id="set_right"]/div/div[3]/div[1]/div[2]/span')
            except:
                log.info('未找到发布的Template')
                return False
            else:
                time.sleep(2)
                try:
                    self.template.click(self.template.deleteBtn_loc)
                except:
                    log.info('-----打开Templates删除对话框失败！----')
                    return False
                else:
                    time.sleep(1)
                    self.template.click(self.template.deleteOKBtn_loc)
                    time.sleep(2)
                    return True


    def test01_add_template(self):
        '''添加Template'''
        self.add_template()
        res = self.verify_template(templateName)
        if res:
            log.info('-----添加Template成功！----')
        else:
            log.info('-----添加Template失败！----')
        self.assertTrue(res)

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
        '''复制Template'''
        self.copy_template(editTemplateName)
        res = self.verify_template(copyTemplateName)
        if res:
            log.info('-----拷贝Template成功！----')
        else:
            log.info('-----拷贝Template失败！----')
        self.assertTrue(res)

    @skip_dependon(depend='test03_copy_template')
    def test04_delete_template(self):
        '''删除Template'''
        self.delete_template(copyTemplateName)
        time.sleep(1)
        res = self.search_template(copyTemplateName)
        if not res:
            log.info('-----删除Template成功！----')
        else:
            log.info('-----删除Template失败！----')
        self.assertFalse(res)

    @skip_dependon(depend='test02_edit_template')
    def test05_publish_template(self):
        '''发布Template'''
        self.publish_template(editTemplateName)
        time.sleep(2)
        res = self.ver_publish_and_del(editTemplateName)
        if res:
            log.info('-----发布Template成功！----')
        else:
            log.info('-----发布Template失败！----')
        self.assertTrue(res)

if __name__ == '__main__':
    unittest.main()





